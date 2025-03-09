#### map function ####
#### Code 1 ####
def multiple_number(x):
    return x*2

str_list = [1,2,3,4,5,6,7,8,10]
str_map = map(lambda x:x*2,str_list)
str_multiple = map(multiple_number,str_list)

print(list(str_map))
print(set(str_multiple))

#### Code 2 ####
words = ["banana", "apple", "kiwi", "strawberry"]

words_map = map(lambda x: len(x), words)
print("lenght - > ",list(words_map))

#### range function ####
#### Code 3 ####
rng = range(2,22,3)
print(list(rng))
#### Code 4 ####
rng = range(20,0,-2*2)
print(list(rng))

#### filter function ####
#### Code 5 ####
words = ['apple','banana','cherry','orange','kiwi','melon','mango']

filter_words =filter(lambda x: len(x) > 5, words)
print(list(filter_words))

#### Code 6 ####
### sum function ###
number = [1,2,3,4,5,6,7,8,9,10]
sum_number = sum(number)
print(sum_number)

#### Code 7 ####
### sorted function ###
number = [1,2,3,4,5,6,7,8,9,10]

sorted_number = sorted(number,reverse=
                       True)
print(sorted_number)

#### Code 8 ####
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25},{"name": "Khn", "age": 12}]
sorted_by_age = sorted(people, key=lambda x: x["age"])
print(sorted_by_age)

# the key parameter in the sorted() function can be used with any iterable (lists, tuples, sets, etc.), not just dictionaries. It works by applying a function to each element before sorting.
#### Code 9 ####
data = [(1, 5), (3, 2), (2, 8), (4, 1)]
sorted_data = sorted(data, key=lambda x: x[1])  # Sort by second element
print(sorted_data)


#### Code 10 ####
words = ["banana", "apple", "kiwi", "strawberry"]
sorted_words = sorted(words, key=len)
print(sorted_words)

#### Code 11 ####
### emumarate function ###
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

#### zip function ####
#### Code 12 ####
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(combined)

#### Code 13 ####
with open("input.txt", "w") as file:
    file.write("Hello, world!\n")

with open("input.txt", "r") as file:
    content = file.read()
    print(content)


### list comprehension ###
#### Code 14 ####
squareOne = [x**2 for x in range(10)]
print(squareOne)
#### Code 15 ####
squreTwo =["even " + str(x)  for x in range(100) if x % 2 == 0] 
print(squreTwo)

##########Positional Arguments###########
#### Code 16 ####
def greeting(name,age):
  #  print(f"Hello {name } , Age {age}")
    return f"Hello {name} , Age {age}"


print(greeting("Jhon",25))
#### Code 17 ####
#Example 2: Default Arguments
def greeting(name,age=25):
    return f"Hello {name} , Age {age}"

print(greeting("Jhon"))
print(greeting("Jhonny",32))
#### Code 18 ####
###Example 3: Keyword Arguments 
def describe_car(make, model, year):
    print(f"The car is a {year} {make} {model}.")

describe_car(make="Toyota", model="Corolla", year=2022)  # ✅ Clear & readable
describe_car(year=2023, model="Civic", make="Honda")  # ✅ Order doesn't matter

###
#### Code 19 ####
def sum_of_number(*args):
    x = sum(args)
    return x
print(sum_of_number(1,2,3,4,5,6,7,8,9,10))
### sum of number using lambda function
#### Code 20 ####
sum_of_number = lambda *args: sum(args)
print(sum_of_number(1,2,3,4,5,6,7,8,9,10))
## sum of number using for loop
def sum_of_number(*args):
    x = 0
    for i in args:
        x += i
    return x

print(sum_of_number(1,2,3,4,5,6,7,8,9,10))

####**kwargs allows a function to accept any number of named arguments.
#### Code 21 ####
def testing_kwargs(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)


testing_kwargs(name="Jhon",age=25,city="New York")  
#### Code 22 ####
###
def describe_person(**kwargs):
    print("Kwargs:", kwargs)  # Shows the dictionary of arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=30, country="USA")
describe_person(name="Bob", job="Engineer", salary=50000)

####You can combine *args (for multiple positional arguments) and **kwargs (for multiple keyword arguments).
#### Code 23 ####
def display_info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

display_info(1, 2, 3, name="Alice", age=25)

### unpacking 
#### Code 24 ####
def complicated_func(a,b,c,d=True,e=False):
    print(a,b,c,d,e)

complicated_func(*[1,2,3],**{"d":True,"e":False})

### 
#### Code 25 ####
def calculate_total(*args, **kwargs):
    discount = kwargs["discount"]
    sum_total = sum(args) - discount
    print("Total ", sum(args))
    print("After discount: ", sum_total)

calculate_total(10,20,30,discount=5)
#### Code 26 ####
def calculate_total(*args, **kwargs):
    discount = kwargs.get("discount", 0)  # Default discount = 0 if not provided
    sum_total = sum(args) - discount
    print("Total:", sum(args))
    print("After discount:", sum_total)

# Example Calls
calculate_total(10, 20, 30, discount=5)  # ✅ Works with discount
calculate_total(50, 50)  # ✅ Works without discount


