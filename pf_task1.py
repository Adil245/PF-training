def students():
    while True:
        try:
            tot = int(input('Enter the Total Number of students: '))
            mth = int(input('Enter the number of math students: '))
            bio = int(input('Enter the number of Bio students: '))
            if (mth+ bio)> tot:
                return 'student of math and bio should not exceed the Totla students'
            else:
                return 'student without math and bio ||', tot-(mth+bio), ' Student with math and bio:', mth+bio
        except ValueError:
            print('please enter integer values. Enter Again: ')
            continue

print(students())