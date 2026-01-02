def decorator(function):
    print("Do something before the function is called")
    print("=============")
    function()
    print("=============")
    
    return function

@decorator
def helloWorld():
    print("Hello, World!")
    
