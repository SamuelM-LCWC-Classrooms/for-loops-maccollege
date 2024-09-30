from random import randrange

def task_1(): # Lottery ticket generator
    ticket = []
    for i in range(6):
        num = randrange(1, 50)
        ticket.append(num)
    return ticket

def task_2(): # Countdown
    num = int(input("Enter a number less than 100."))
    output = []
    for i in range(100, num - 1, -1):
        num2 = i
        output.append(num2)
    return output

    

def task_3():
    people_cars = {
        "Adam": "Volvo",
        "Kate": "BMW",
        "Mark": "BMW",
        "Hannah": "Ford",
        "Max": "Volvo",
        "Celine": "Fiat"
    }

    car_make_lengths = ()
    for i in people_cars.values():
        wordlength = len(i)
        place = list(car_make_lengths)
        place.append(wordlength)
        car_make_lengths = tuple(place)
        
        
    # Code here
    print("There will be 3 different sizes of key rings.")
    return car_make_lengths

print(task_3())