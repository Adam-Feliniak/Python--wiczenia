def decorator(function):
    def another_function():
        function()
        function()
        function()
    return another_function()

@decorator
def my_function():
    print("Hello world!")

