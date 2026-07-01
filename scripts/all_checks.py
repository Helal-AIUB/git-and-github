print("Hello")
def abc(a):
    if a%2 == 0:
        print("Even")
    else:
        print("Odd")
def greater(a):
    if a > 10 :
        print("Greter then 10")
    else:
        print("less then or equal 10")
def function(exit):
    if exit == 0:
        return
    else:
        exit -=1
def disk():
    print("disk full")
abc(5)
greater(11)
greater(8)
function(2)