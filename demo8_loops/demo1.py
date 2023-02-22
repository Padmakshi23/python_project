for a in range(1,10):
    print (a)


colors = ["red", "green", "yellow", "blue", "green"]

for i in range(0, len(colors)
               ):
    print(colors[i])

numbers = [45, 98, 75, 65, 24, 88, 74, 56, 75]

for i in range(0, len(numbers)):
    if numbers[i] <= 50:
        print(numbers[i])

for i in range(0, len(numbers)):
    if numbers[i] ==24:
        print(numbers[i])
        break

for i in range(0, len(numbers)):
    if numbers[i] == 24:
        continue
    print(numbers[i])
