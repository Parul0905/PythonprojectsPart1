def num_people():
    num = int(input('Enter number of people in the group: '))
    
    names = []
    for i in range(1, num + 1):
        name = input(f'Enter name of person {i}: ')
        names.append(name)
    
    total_bill = float(input('Enter total bill amount: '))
    
    each_person_owes = round(total_bill / num, 2)
    
    for name in names:
        print(f'{name} owes {each_person_owes}')

num_people()
