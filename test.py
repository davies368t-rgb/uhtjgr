try:
    num=int(input("input a number: "))
    print(num)

except ValueError:
    print("Exception", ValueError)