# main.py
def hello_world():
    return "Hello from Ryan Phillips"

def greet_person(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("What is your name? ")
    print(hello_world())
    print(greet_person(name))