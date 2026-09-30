s = input("enter the text ").strip()

if s == "":
    print("the input is empty.")
else:
    c = len(s)
    w = len(s.split())
    p = s.count(" ")
    n = 0

    for x in s:
        if x == "." or x == "!" or x == "?":
            n += 1

    print("chars:", c)
    print("words:", w)
    print("lines:", n)
    print("spaces:", p)
