from datetime import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        print("Function Name:", func.__name__)
        print("Input Arguments:", args)

        result = func(*args, **kwargs)

        print("Output:", result)
        print("Timestamp:", datetime.now())
        print("----------------------")

        return result

    return wrapper


@logger
def add(a, b):
    return a + b


@logger
def multiply(a, b):
    return a * b


# Calling functions
add(10, 20)
multiply(5, 4)