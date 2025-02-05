import sys

def get_key_from_value(dict: dict, value):
    for key, item in dict.items():
        if item == value:
            return key
    return None

def dictio_func(city: str):
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    value = get_key_from_value(capital_cities, city)
    if not value:
        print("Unknown capital city")
        return
    print(get_key_from_value(states, value))
    

if __name__ == '__main__':
    n = len(sys.argv)
    if (n < 2):
        exit()
    dictio_func(sys.argv[1])