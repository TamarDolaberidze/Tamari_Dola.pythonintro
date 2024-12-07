def num_collection(n):
    sequence = [n]
    while n != 1:
        if n %2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence

def cached_collection(n, cache):
    if n in cache:
        return cache[n]
    
    sequence = [n]

    while n != 1:
        if n %2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    
    cache[n] = sequence

    return sequence



def main():
    cache = {}

    n = int(input("enter a number: "))

    print(num_collection(n))
    print(cached_collection(n, cache))

if __name__ == "__main__":
    main()