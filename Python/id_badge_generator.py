print('Please enter the following information:')
print()
first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('Id Number: ')
hair = input('Hair color: ')
eye_color = input('Eye color: ')
month_started = input('Month you started: ')
training_completed = input('Did you complete your training? ')
print()
print('The ID Card is: ')
print('-----------------------------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(job_title.title())
print(f'ID: {id_number}')
print()
print(email_address.lower())
print(phone_number)
print()
print(f'Hair: {hair:30} Eyes: {eye_color}')
print(f'Month: {month_started:29} Training: {training_completed.title()}')
print('-----------------------------------------------------')