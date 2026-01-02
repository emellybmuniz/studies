def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
if __name__ == "__main__":
    gen = simple_generator()
    for value in gen:
        print(value)