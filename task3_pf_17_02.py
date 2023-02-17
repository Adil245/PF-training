def list_sorting():
    li = []
    while True:
            length = input("Enter The length of List:")
            if length.isdigit():
                for i in range(0,int(length)):
                    while True:
                        try:
                            num = int(input(f'Enter Number at index {i} : '))
                            li.append(num)
                            break
                        except ValueError:
                            print('Please try to enter right keyword.')
                        continue
            else:
                print('please Enter the length in positive numbers.')
                continue
            break

    
    li.sort()
    print('Sorted List : ', li)
    while True:
        decision = str(input('Do you want to append a number in list yes/no :')).lower()
        if decision == 'no':
            print(li)
            break
        elif decision =='yes':
            while True:
                try:
                    appended_num = int(input('Enter a number : '))
                    li.append(appended_num)
                    li.sort()
                    print(li)
                
                except ValueError:
                    print('please enter an integer value, Decide Again!! ')
                    continue
                break
        else:
            print('OOPs!! please enter right keyword.')
            continue
            
    

list_sorting()

