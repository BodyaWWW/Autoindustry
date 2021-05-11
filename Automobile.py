# create class Auto

class Automobile:

    #Function which turn on the engine

    def __init__(self):
        try:
            self.motor = True
            print('Motor is working now...')
        except Exception:
            print('Something is going wrong!')

    # Function which find different problems with car(engine,transmition,etc)
    def say_about_car_problem(self,problem1,problem2,problem3,problem4):
        problem1 = True
        problem2 = True
        problem3 = True
        problem4 = True

        if self.problem1 == problem1:
            print('You have problem 1! We are fixing it now...')
        elif self.problem2 == problem2:
            print('You have problem 2! We are fixing it now...')
        elif self.problem3 == problem3:
            print('You have problem 3! We are fixing it now...')
        elif self.problem4 == problem4:
            print('You have problem 4! We are fixing it now...')
        else:
            print('Your car is fully OK.')


    def privet(self):
     pass

print('hi')
print("пока")


mazda_cx = Automobile()
mazda_cx.motor = False
mazda_cx.problem2 = True
mazda_cx.problem1 = False
mazda_cx.problem3 = False
mazda_cx.problem4 = True


mazda_cx.say_about_car_problem(mazda_cx.problem2,mazda_cx.problem1,mazda_cx.problem3,mazda_cx.problem4)
