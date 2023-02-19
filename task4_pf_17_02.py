# from collections import deque
import queue
def lifo_queue():
    print('\t*** LAST IN FIRST OUT QUEUE ***')
    lifoQ = queue.LifoQueue()
    while True:
        length = input('please enter the length of LIFO Queue: ')
        if length.isdigit():
            for i in range(int(length)):
                lifoQ.put(input(f'Please Enter anything at psition {i+1}: '))
        else:
            print('please enter the Length in positive integer !!')
            continue
        break

    print('Extracting Elements from LIFO Queue')
    while True:
        extract = input('How much elements you want to get: ')
        if extract.isdigit():
            if extract> length:
                print('please Enter a smaller Number than the size of queue ')
                print('Size of Queue : ', lifoQ.qsize())
                continue
            else:
                for x in range(int(extract)):
                    print(lifoQ.get(), end=' ')
        else:
            print('please enter the Length in positive integer !!')
            continue
        break

    print(' \nRemaining Elements * : ', lifoQ.qsize())

if __name__ == "__main__":
    lifo_queue()
