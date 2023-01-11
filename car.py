class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print('Car started')

    def increase_speed(self, delta = 0):
        if self.started:
            self.speed += delta
            print('Speed increased')
        else:
            print('Car isn\'t started')

    def stop(self):
        self.speed = 0
        print('Stopped')

car = Car()
car.increase_speed()
car.start()
car.increase_speed(5)
car.stop()