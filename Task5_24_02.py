# 1st Function(write a method with take key, value from the user and add that value in the list.. if key is already filled should return message to user to chose another key. length of list will be 10)
def Key_value():
    print('**function 1**')

    li_val =[]
    li_key =[]
    i=0

    while (i<10):
        idx = input(f'Pease enter the **key** for position {i+1}: ')
        
        val = input(f'please enter a **value** for position {i+1}: ')
        if idx not in li_key:
            li_val.append(val)
            li_key.append(idx)
            i=i+1
        else: 
            print('Error: Key already exists please **Enter Again**')
            continue
    
    return li_val
# 2nd Function (write a method with fixed length of list 5. if user enter more then 5th value in the list bottom value should be removed and new value should be added at the top of list)
#  For 2nd and 3rd we will use same list li[]
li = []
def queue():
    print('**function 2**')
    
    for i in range(5):
        val = input(f'Enter {i} value: ')
        li.append(val)
    print(li[::-1])
    while True:
        ques = input('Do you want to add a value in Queue *yes/No*: ').lower()
        if ques == 'no':
            return li[::-1]
        elif ques == 'yes':
            new_val = input('Enter a value to append : ')
            li.append(new_val) 
            li.pop(0)
            return li[::-1]
        else:
            print('Wrong Entery! Enter again')
            continue


# 3rd Function (write a method with list of random numbers, when user add new value methode will check if the value already exist in list return message "value already in the list other wise add the value in the list and display back the list till that value)
def list_searching():
    print('**Function 3**')
    print('**Check A value is in list or not**')
    val = input('Enter A Value : ')
    # for i in range(li):
    if val in li:
        print('Value is alredy there.')
        return li
    else:
        li.append(val)
        return li


import random
def table(rows, cols):
    print('**Function 4**')
    for i in range(rows):
        for j in range(cols):
            r= random.randint(10,20)
            print(r,  end=" ")
        print(" ")


    

[[1,2,3],[2,4,5]]


if __name__ == '__main__':
    print(Key_value())
    print(queue())
    print(list_searching())
    rows = int(input('Enter Rows: '))
    cols = int(input('Enter columns: '))
    table(rows, cols)
