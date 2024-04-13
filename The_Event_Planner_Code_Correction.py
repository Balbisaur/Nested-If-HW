attendees = int(input("Enter number of attendees: "))

if attendees >= 100:
    print('large hall')
elif attendees <= 100:
    print('conference room')

attendees = input('Are you vegetarian: yes or no?')

if attendees == "yes":
    print('reccomend veggie delight caterers')
elif attendees == "no":
    print('reccomend gourmet caterers')