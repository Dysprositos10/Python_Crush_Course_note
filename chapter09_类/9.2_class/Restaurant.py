class Restaurants():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print('The name of the restaurant is '+self.restaurant_name.title())
        print('The type of the restaurant is '+self.cuisine_type.title())
    def open_restaurant(self):
        print('The '+self.restaurant_name+' is open')
    def set_number_served(self,people):
         self.number_served=people
         print('There are '+str(self.number_served)+' people')
    def increment_number_served(self,increment_people):
        self.number_served += increment_people
        print('There should be '+str(self.number_served)+' guest today')