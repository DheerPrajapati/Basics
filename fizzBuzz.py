for i in range(1,21):
    s = ""
    if i % 3 == 0:
        s = s + "Fizz"
    if i % 5 == 0:
        s = s + "Buzz"
    if i % 5 != 0 and i % 3 != 0:
        s = s + str(i)
    print(s)