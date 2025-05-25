# fruits = ["apple", "banana", "cherry"]
# fruits[1] = "apple"  # You can change elements
# print (fruits)

# coordinates = (10, 20)
# coordinates[0] = 5  # ❌ Error! Tuples cannot be changed
# print(coordinates)

# numbers = {1, 2, 3, 2}
# numbers.add(5)
# print(numbers)  # Output: {1, 2, 3}

# person = {"name": "Alice", "age": 30}
# for value in person.values():
#     print(value)  # Output: Alice

# print(int("5"))
# print(int(3.9)) 
    # ❓
# print(str(3.14))      # ❓
# print(bool([]))       # ❓
# print(int
# ("8.5")) 
\
    
# age =18
# name = 'Alice'

# if age > 18 and name =='Alice':
#     print("Already an adult")
# elif age == 18 and name == 'Sebastian':
#     print("young adult")     
# elif age < 18 or name == 'Alice':
#     print("Hi, I am Alice")
# else: 
#     print("none of the above")  

fruits = ["apple", "banana", "cherry", "kiwi"]
for fruit in fruits:
    formatted_name= fruit.capitalize()
    
    vowel_count = 0
    for letter in fruit.lower(): 
        if letter in "aeiou":
           vowel_count += 1
    
    print(f"{formatted_name} has {vowel_count} vowels")
