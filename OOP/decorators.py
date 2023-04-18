def decorator(function):
    def another_function():
        print("Przed wywołaniem")
        print("Po wywołaniu")
    return another_function()

@decorator
def my_function():
    print("Hello world!")

