n = 10
def countdown(n):
    if n <= 0:
        print("Boom!")
    else:
        print(n)
        countdown(n-1)

print(countdown(n))