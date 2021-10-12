
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

odd_number = []
evn_number = []
# iterating each number in list
for num in range(start, end + 1):

    # checking condition
    if num % 2 != 0:
        odd_number.append(num)
    if num % 2 == 0:
        evn_number.append(num)

print("\n odd number : \n")
for number in odd_number:
    print(number, end=",")

print("\n evn number :\n")
evn_number = evn_number[::-1]
for number in evn_number:
    print(number, end=",")
