def multiplication_table_generator(num):
    for num in range(1, 11):
        yield [f"{num} * {i} = {num * i}" for i in range(1, 11)]
        
for table in multiplication_table_generator(num=0):
    for line in table:
        print(line)