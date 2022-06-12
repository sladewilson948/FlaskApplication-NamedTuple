#so far we know that a named tuple can return us a dictionary if we are able to define a tuple first and thjen convert it to a dictionary. A dictionary is nothing a but a json dcumnet so lets make a python flask application that does just the same takes our details and retuner a json document and return it as teh details as output on a webpage

from flask import Flask, jsonify
from collections import namedtuple

class GenerateDocument:

    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
    
    def make_tuple(self):
        my_tuple = namedtuple("Tuple", ["Name", "Age", "City", "Country"])
        tuple_1 = my_tuple(self.name, self.age, self.city, self.country)
        return tuple_1
    
    def create_dictionary(self, get_tuple):
        new_dict = get_tuple._asdict()

        return new_dict

app = Flask(__name__)


@app.route("/")
def index():
    name = input("Enter name here : ")
    age = int(input("Enter age here : "))
    city = input("Enter city here : ")
    country = input("Enter country here : ")
    obj1 = GenerateDocument(name, city,age, country)
    my_dict = obj1.create_dictionary(obj1.make_tuple())

    return jsonify(my_dict)

if __name__ == "__main__":
    app.run()