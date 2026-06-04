numbers = [1,2,3,4,5]

# Exercise 1
def square(nums):
    sq_num = []
    for num in nums:
        num1 = num ** 2
        sq_num.append(num1)
    return sq_num

num = square(numbers)
print(f"Square of numbers is: {num}")

# Exercise 2
even = [num for num in numbers if num % 2 == 0]
print(f"Even numbers are: {even}")

# Exercise 3
dict = {"Id": 304, "Name": "Brijesh"}
keys = list(dict.keys())
values = list(dict.values())

print(f"Keys are: {keys}, Values are: {values}")

# Exercise 4
input = [1,2,2,3,4,4]

duplicate = []
sett = set(input)
for num in sett:
    # print(input.count(num))
    if input.count(num) > 1:
        duplicate.append(num)

print(f"Duplicate items are: {duplicate}")
