fizz = 3
buzz = 7
limit = 100
for x in range(1, limit+1):
    out = ""
    if x%fizz == 0:
        out += "fizz"
    if x%buzz == 0:
        out += "buzz"
    if out == "":
        out += str(x)
    print(out)
