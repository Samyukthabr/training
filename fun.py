import time

def time_it(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"Function '{func.__name__}' took {(end_time - start_time):.6f} seconds to execute.")

        return result

    return wrapper

@time_it

def my_function(input_str):

    output_str = input_str.upper()

    return output_str

user_input = input("Enter a string: ")

result = my_function(user_input)


