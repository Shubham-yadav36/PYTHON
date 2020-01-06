x = 10 # global
def set():
    global x
    x = 90  # local
    print(x)


set()
print(x)