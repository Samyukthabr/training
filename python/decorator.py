import time

def decorator_timer(some_function):
   

    def cover(a,b):
        t1 = time.time()
        result = some_function(a,b)
        end = time.time()-t1
        return result, end
    return cover


@decorator_timer
def my_pow(a, b):
    p = a ** b
    return p
    
    

result,executiontime = my_pow(400000 , 500000)


print("executime time:",executiontime) 

