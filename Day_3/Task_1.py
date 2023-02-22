age1 = int(input('enter age1: '))
age2 = int(input('enter age2: '))
age3 = int(input('enter age3: '))


if age1 < age2 and age1 < age3:
    print("Smith is younger")

elif age2 < age3 and age2 < age1:
    print("John is younger")

elif age3 < age1 and age3 < age2:
    print("Henry is younger")

elif age1 == age2 == age3:
    print ("Smith, John and Henry are of same age")

else :
    print("Invalid!!")