fruits=["Apple","Banana","Cherry"]
print(fruits[0])
print(fruits[1]) #index 0 is the first and -1 is the last
print(fruits[2])

print("---------------------------")

for fruit in fruits:
    print(fruit)


fruits.append("orange")
print(fruits)

fruits.remove("Banana")
print(fruits)