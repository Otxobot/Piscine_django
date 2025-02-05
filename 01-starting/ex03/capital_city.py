import sys

def dictio_func(state: str):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    key = states.get(state)

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    if not key:
        print("Unknown state")
        return
    print(capital_cities.get(key))

if __name__ == '__main__':
    n = len(sys.argv)
    if (n < 2):
        exit()
    dictio_func(sys.argv[1])

