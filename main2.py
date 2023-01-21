import re

def tokenize(code):
    tokens = re.findall(r"(\b\w+\b)|([^\w\s])|(/\*.*?\*/)|(//.*)", code)
    for token in tokens:
        if token[0] in ["int", "float", "double"]:
            print(token[0] + " => keyword")
        elif token[1]:
            print(token[1] + " => delimiter")
        elif token[2]:
            print(token[2] + " => multi-line comment")
        elif token[3]:
            print(token[3] + " => single-line comment")
        elif re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", token[0]):
            print(token[0] + " => identifier")
        elif re.match("^[+\-*/=<>!&|%^]$", token[0]):
            print(token[0] + " => operator")
        elif re.match("^[0-9]+\.[0-9]+$", token[0]):
            print(token[0] + " => Real number constant")
        elif re.match("^[0-9]+$", token[0]):
            print(token[0] + " => integer constant")

def main():
    with open("test.cpp", "r") as file:
        code = file.read()
        tokenize(code)

if __name__ == "__main__":
    main()



def main():
    with open("test.cpp", "r") as file:
        code = file.read()
        tokenize(code)

if __name__ == "__main__":
    main()
