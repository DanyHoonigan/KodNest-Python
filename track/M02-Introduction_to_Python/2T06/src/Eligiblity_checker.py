marks = int(input())
attendance = int(input())
status = input()
    
if marks>=60:
    if attendance >=75:
        if status == 'yes':
            print("Eligible for admission")
        else:
            print("Not Eligible for admission")
    else:
        print("Not Eligible for admission")
else:
    print("Not Eligible for admission")