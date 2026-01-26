import os

class FileIterator: 
    def __init__(self, filename):
        # Check if the file exists, if not, create it
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                pass  
        self.file = open(filename, 'r')

    def __iter__(self): 
        return self # tells Python what object to iterate over, in this case, the FileIterator instance itself
        
    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()


# usage example
if __name__ == "__main__":
    for line in FileIterator('example.txt'): # type: ignore
        print(line)
