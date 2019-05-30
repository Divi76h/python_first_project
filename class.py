class hello:

    def __init__(self):
        print("hello")

    def __str__(self):
        print("hi")


if __name__ == "__main__":
    hl = hello()
    hl.__str__()
