
def open_file():
    file = open("numbers.txt", 'r')
    for line in file.readlines():
        print_line(line)
    file.close()

def print_line(line: str):
    numbers = line.split(",")
    for number in numbers:
        print(number)

if __name__ == '__main__':
    open_file()