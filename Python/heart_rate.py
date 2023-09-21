"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# Get the age of the person
age = int(input('Please enter your age:'))
# Calculate Max heart rate based off the age of the person
maximum_heart_rate = 220 - age
# Calculate Lower heart rate besed off the age of the person
lower_heart_rate = maximum_heart_rate *.65
# Calculate Upper heart rate besed off the age of the person
upper_heart_rate = maximum_heart_rate *.85
print(f'When you exercise to strengthen your heart, you should keep your heart rate between {lower_heart_rate:.0f} and {upper_heart_rate:.0f} beats per minute')

