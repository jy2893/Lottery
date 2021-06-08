#猜年龄
def prompt1():
    age = float(input('Enter an age: '))
    if age < 25:
        print("too young, guess a little bigger")
        prompt1()
    elif age > 25:
        print("too old, guess a little younger")
        prompt1()
    elif age == 25:
        print("you are right")
prompt1()



