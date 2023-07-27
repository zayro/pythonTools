import time

def my_decorator_name(name):
    def my_custome_decorator(function):
        def wrapper(*args, **kwargs):
            print('Name:', name)
            return function(*args, **kwargs)

        return wrapper

    return my_custome_decorator


@my_decorator_name('CodigoFácilito')
def suma(a, b):
    c = a + b
    print("c", c)
    return c


suma(10, 3)


def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        total = time.time() - start
        print(total, 'seconds')
        return result

    return wrapper


@measure_time
def suma(a, b):
    time.sleep(1)
    return a + b


print(suma(10, 20))
