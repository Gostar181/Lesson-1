import random
from asyncio import wait_for


class Human:

    def __init__(self, name="Human", job=None, car=None, Pet = None):
        self.name = name
        self.money = 100
        self.job = job
        self.car = car



def work(self):
    self.money += self.job.salary
    print(f"{self.name}Worked for 8 hours and get{self.job.salary}$")




class Auto:

    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        print(f"Names of {self.brand} passengers:")
        for passenger in self.passengers:
            print(passenger.name)

job_list = {
"Java developer":
{"salary":50, "gladness_less": 10 },
"Python developer":
{"salary":40, "gladness_less": 3 },
"C++ developer":
{"salary":45, "gladness_less": 25 },
"Rust developer":
{"salary":70, "gladness_less": 1 },
}

class job:
   def __init__(self, job_list):
       self.job = random.choice(list(job_list))
       self.salary = job_list[self.job]["salary"]

class Pet:
   def __init__(self, name = "Baton"):
       self.name = name
       self.hungry = 50
       self.hungry = random.choice(1,100)

if ():
    Pet.hungry >= 49
else:
    print(f" Baton is hungry, buy food for your pet!")
    work.money = 90
    print("Tou paid 10$ for food")

sasha = Human("Sasha", job(job_list))


kate = Human("Kate")
car = Auto("Mercedes")
car.add_passengers(sasha)
car.add_passengers(kate)
car.print_passengers_names()

#