def cut_cake(part):
    try:
        return "На каждого по {} части".format(1/int(part))
    except (ZeroDivisionError, TypeError, ValueError):
        return "С ума сошли?"

part = input("На сколько человек будете делить пирог?" )  
#print(f"{cut_cake(part)}")

x = [1,2,3]
#print(x[10])

def do_something(x):
    print(x)

x=0
while x < 10:
    do_something(x)
    x += 1
   