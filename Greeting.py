import time

name = input("Enter your name:")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)


hour = int(time.strftime('%H'))#convert the %H to int because it is string

if(4<=hour<12):
    print("Good Morning",name)
elif(12<=hour<5):
    print("Good Afternoon",name)
elif(5<=hour<=7):
    print("Good Evening",name)
else:
    print("Good Night",name)
