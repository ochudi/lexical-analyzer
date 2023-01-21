import re

def tokenize(code):
    tokens = re.findall("\b\w+\b|[^\w\s]", code)
    for token in tokens:
        if token in ["int", "float", "double"]:
            print(token + " => keyword")
        elif re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", token):
            print(token + " => identifier")
        elif re.match("^[+\-*/=<>!&|%^]$", token):
            print(token + " => operator")
        elif re.match("^[0-9]+\.[0-9]+$", token):
            print(token + " => Real number constant")
        elif re.match("^[0-9]+$", token):
            print(token + " => integer constant")
        else:
            print(token + " => delimiter")

def main():
    with open("test.cpp", "r") as file:
        code = file.read()
        tokenize(code)

if __name__ == "__main__":
    main()
