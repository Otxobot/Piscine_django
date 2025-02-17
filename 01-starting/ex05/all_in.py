import sys

def get_item(dict: dict, target: str):
    for key, item in dict.items():
        if key.upper() == target.upper():
            return item
    return None


def get_key(dict: dict, target: str):
    for key, item in dict.items():
        if item.upper() == target.upper():
            return key
    return None


def print_state_or_city(string: str):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    value = get_item(states, string)
    key = get_key(capital_cities, string)
    if value:
        print(capital_cities.get(value),
              "is the state of", get_key(states, value))
    elif key:
        print(capital_cities.get(key), "is the capital of", get_key(states, key))
    else:
        print(string, "is neither a capital city nor a state")

def main():
    n = len(sys.argv)
    if (n < 2):
        return
    strings = sys.argv[1].split(",")
    for string in strings:
        string = string.strip()
        if string == "":
            continue
        print_state_or_city(string)

if __name__ == '__main__':
    main()