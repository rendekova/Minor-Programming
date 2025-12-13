def ask_name():
    # do not change code below
    yourname = input("What's your name? ")
    return yourname


def say_hello(s):
    print(f"My name is, my name is, my name is {s}")

if __name__ == "__main__":
    # do not change code below
    myname = ask_name()
    say_hello(myname)
