"""Restaurant rating lister."""


# put your code here
import sys

import_file = open(sys.argv[1], "r")

def create_sorted_dictionary_of_restaurant_ratings(rated_restaurants_from_source, rated_restaurants_by_users):
    """ Creates sorted dictionary of restaurant ratings. """

    restaurant_ratings_by_name = {}

    for line in rated_restaurants_from_source:
        name, rating = line.strip().split(":")
        restaurant_ratings_by_name[name] = rating

    for entry in rated_restaurants_by_users:
        # line = " ".join(line)
        # line = line.strip().split(",")
        # print(line)
        name = entry[0]
        rating = entry[1]
        restaurant_ratings_by_name[name] = rating

    return sorted(restaurant_ratings_by_name.items())


def print_ratings(sorted_dictionary):
    """ Print out sorted ratings dictionary. """

    for line in sorted_dictionary:
        print("{} is rated at {}".format(line[0], line[1]))

def ask_user_restaurant_rating():
    user_restaurant_ratings_list = []
    print("Follow the prompts below, when you are finished enter 'quit' into 'Name of restaurant' prompt.")
    while True:
        restaurant_name = input("Name of restaurant: ").title()
        if restaurant_name == "Quit":
            break
        restaurant_rating = input("{}'s rating: ".format(restaurant_name))
        user_restaurant_ratings_list.append((restaurant_name, restaurant_rating))
    return user_restaurant_ratings_list
    #print(" ".join(user_restaurant_ratings_list))
    #print(user_restaurant_ratings_list)    


user_input_dictionary = ask_user_restaurant_rating()
sorted_ratings = create_sorted_dictionary_of_restaurant_ratings(import_file, user_input_dictionary)

(print_ratings(sorted_ratings))