class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"

    # built this function so the pytest can compare the result of the main2 function with the Number class
    def __eq__(self, other):
        return self.value == other.value
