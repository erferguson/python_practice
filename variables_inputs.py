price = 10 # integer
rating = 4.9 # float
name = 'Fitz' # string
is_published = True # boolean
# print(price, rating, name, is_published) 

first_name = 'John'
last_name = 'Smith'
age = 20
new_patient = True

if new_patient:
    print(f'Our new patient, {first_name} {last_name}, is {age} years old.')
else:
    print(f'Welcome back, {first_name} {last_name}!')

# INPUT -- asks for something, then returns it
# ----
# name = input('What is your name? ') 
# fav_color = input('Share your favorite color: ')

# print(f'Hi, {name}. We understand that your favorite color is {fav_color}. ')

birth_year = input('birth year: ')
age = 2021 - int(birth_year)
print(age)

weight = input('What is your weight in lbs? ')
convert = int(weight) / 2.205  # * .45
print(convert)


