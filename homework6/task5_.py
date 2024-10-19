n = int(input("შეიყვანეთ მთელი რიცხვი n (0 < n < 10): "))

i = 0
while i <= n:
    # ვბეჭდავთ სივრცეებს (სხვაობის შესაქმნელად მარცხნიდან)
    print("  " * (n - i), end="")

    # მარცხნიდან მცირდება
    j = i
    while j >= 0:
        print(j, end=" ")
        j -= 1

    # მარჯვნიდან იზრდება
    k = 1
    while k <= i:
        print(k, end=" ")
        k += 1

    # გადავდივართ ახალ ხაზზე
    print()
    i += 1


  












else:
    print("not correct")