def decorator(function):
    # generic decorator to handle functions with arguments
    def envelope(*args, **kwargs):
        print("=============")
        function(*args, **kwargs)
        print("=============")
    
    return envelope

@decorator
def helloWorld(name):
    print(f"Hello {name}!")
    
helloWorld("Alice")
    
