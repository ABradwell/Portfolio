class Car:
      def __init__(self,brand='ford', color='red', pilote='person',speed = 0):
            self.brand = brand
            self.color = color
            self.pilote = pilote
            self.speed = speed
      def choice_driver(self,name):
            self.pilote = name
      def accelerate(self,flow,duration):
            addspeed = flow * duration
            if self.pilote != 'person':
                  self.speed = self.speed + addspeed
            else:
                  print('This car does not have a driver!')
                  
      def display_all(self):
            print(self.color, self.brand, ' driven by', self.pilote, ', speed =  ', self.speed, 'm/s.')
      def  __repr__(self):
            return (str(self.brand) + ":" + str(self.color) + ":" + str(self.pilote) + ":" + str(self.speed))
