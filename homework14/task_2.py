def midpoint(x1, y1, x2, y2):
    tuple_middle_point = ((x1+x2) / 2, (y1+y2) / 2)
    return tuple_middle_point


def main():
   print(midpoint(10, 20, 55, 60))
   print(midpoint(100, -17, 50, 75))


if __name__ == "__main__":
    main()