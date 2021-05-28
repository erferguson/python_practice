# AND : both need to be TRUE
# has_high_income = True
# has_good_credit = False

# if has_high_income and has_good_credit:
#     print('Eligible for loan')

# OR : at least one needs to be TRUE
has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print('Eligible for loan')

# NOT : 
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('Eligible for loan!')

# EXAMPLE
weight = input('What is your weight? ')
weight_type = input('(L)bs or (K)g ')
if weight_type.upper() == 'L':
    converted_weight = int(weight) * .45
    print(f'Your {weight}lbs equals {converted_weight} kilos.')

if weight_type.upper() == 'K':
    converted_weight = int(weight) / .45
    print(f'Your {weight}kg equals {converted_weight} pounds.')