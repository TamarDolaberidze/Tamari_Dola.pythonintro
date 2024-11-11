def cel_to_far(cel):
    return cel * 9/5 + 32

def far_to_cel(far):
    return (far - 32) * 5/9

def main():
    result1 = cel_to_far(30)
    print(f"Farengeit is {result1}")

    result2 = far_to_cel(70)
    print(f"Celsius is {result2}")
    

if __name__ == "__main__":
    main()  