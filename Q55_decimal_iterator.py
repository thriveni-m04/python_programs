
# Q55. User-Defined Iterator for Decimal Values

class NumberIterator:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration

        value = self.current
        self.current = round(self.current + self.step, 10)

        return value


# Create iterator
numbers = NumberIterator(0.0, 1.0, 0.25)

# Display values
for num in numbers:
    print(num)
