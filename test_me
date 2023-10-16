#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

print("-- Create a new amenity --")
my_amenity = Amenity()
my_amenity.name = "City center everything near you"

print("-- Create a new city --")
new_city = City()
new_city.new_city = "606308"
new_city.name = "Salem"

print("-- Create a new place --")
new_place = Place()
new_place.city_id = "606308"
new_place.user_id = "irafajs"
new_place.name = "Irafasha"
new_place.description = "south of the city"
new_place.number_rooms = 67
new_place.number_bathrooms = 100
new_place.max_guest = 67
new_place.price_by_night = 100
new_place.latitude = 3.4576
new_place.longitude = 7.9876
new_place.amenity_ids = 4

print("-- Create a new state --")
new_state = State()
new_state.name = "East_South"

print("-- Create a review --")
new_review = Review()
new_review.place_id = "Kigali"
new_review.user_id = "89"
new_review.text = "they have poor hygiene"
