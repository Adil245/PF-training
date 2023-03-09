from collections import Counter

import traceback
from flask import Flask, render_template
from flask import request


class ML:
    def __init__(self):
        self.avaliable_models = {
            "face_detection": "/additional_drive/ML/face_detection",
            "car_detection": "/additional_drive/ML/car_detection",
            "shoe_detection": "/additional_drive/ML/shoe_detection",
            "cloth_detection": "/additional_drive/ML/cloth_detection",
            "signal_detection": "/additional_drive/ML/signal_detection",
            "water_level_detection": "/additional_drive/ML/water_level_detection",
            "missile_detection": "/additional_drive/ML/missile_detection"
        }
        self.loaded_models_limit = 2
        self.loaded_models = {
            model: self.load_weights(model)
            for model in list(self.avaliable_models)[:self.loaded_models_limit]
        }
        self.request_counters = Counter()

    def load_weights(self, model):
        return self.avaliable_models.get(model, None)

    def load_balancer(self, new_model):
        # your code here
        # update the request counters for each loaded model
        for model in self.loaded_models:
            self.request_counters[model] += 1
        # find the least frequently requested model
        least_frequent_model = min(self.request_counters, key=self.request_counters.get)
        # unload the least frequent model and load the new one
        del self.loaded_models[least_frequent_model]
        self.loaded_models[new_model] = self.load_weights(new_model)
        # reset the request counter for the unloaded model
        self.request_counters[least_frequent_model] = 0
        # print(self.loaded_models)


app = Flask(__name__)
ml = ML()


@app.route('/', methods=['GET'])
def get_loaded_models():
    loaded_models = ml.loaded_models.keys()
    return render_template('index.html', loaded_models=loaded_models)


@app.route('/process_request', methods=['GET', 'POST'])
def process_request():
    try:
        model = request.form["model"]
        if model not in ml.loaded_models:
            ml.load_balancer(model)
        return "processed by " + ml.loaded_models[model]
    except:
        return str(traceback.format_exc())


if __name__ == "__main__":
    app.run(debug=True)
