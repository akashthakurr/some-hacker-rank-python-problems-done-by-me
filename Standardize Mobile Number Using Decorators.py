def wrapper(f):
    def fun(l):
        # complete the function  
        f([f'+91 {i[-10:-5]} {i[-5::]}' for i in l])
    return fun