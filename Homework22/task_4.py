class ExtendedList(list):
    def min(self):
        if not self:
            return None
        return min(self)

    def max(self):
        if not self:
            return None
        return max(self)

def main():
    numbers = ExtendedList([10, 5, 6, 13, 27])

    print("Numbers:", numbers)
    print("Minimum value:", numbers.min())
    print("Maximum value:", numbers.max())


if __name__ == "__main__":
    main()