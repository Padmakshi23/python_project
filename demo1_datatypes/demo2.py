colour = ["red", "green", "yellow", "blue"]
print(colour)
print(colour[2])
print(type(colour))

colour.append("red")
print(colour)

colour.insert(1, "black")

print(colour)

colour.append("red")
print(colour)

colour.remove(colour[2])
print(colour)
print(len(colour))

colour.pop()
print(colour)

# dict

record = {
    "student_name": "padmakshi",
    "student_mai_id": "pj.@gmailcom",
    "marks": [90, 67, 89.97, 40],
    "sport": {
        "inside": "chess",
        "outside": "hockey"
    }
}
print(record)
all_marks = record["marks"]
print(all_marks[3])
print(record["sport"]["outside"])
