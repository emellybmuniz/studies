import functools # Is used to fix the name issue in decorators

def decorator(function):
    # @functools.wraps(function)
    def envelope(*args, **kwargs):
        print("=============")
        if not isinstance(args[0], str):
            raise ValueError("Argument must be a string")
        result = function(*args, **kwargs)
        print("=============")
        return result
    
    return envelope

@decorator
def helloWorld(name):
    print(name)
    return name.upper()
    
result = helloWorld('Emelly')
print(result) # prints "EMELLY"

print(helloWorld.__name__)  # prints "envelope"
# How to fix the name issue? With @functools.wraps



