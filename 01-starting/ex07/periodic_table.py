def parse_input_file(input_file):
    elements = {}
    for line in input_file:
        name, properties = line.strip().split('=')
        properties_dict = {}

        for prop in properties.split(','):
            key, value = prop.split(':')
            properties_dict[key.strip()] = value.strip()
        
        elements[int(properties_dict['number'])] = properties_dict
    
    return elements

def main():
    input_file = open('periodic_table.txt', 'r')
    elements = parse_input_file(input_file)
    input_file.close()

    positions = {
        1: (1, 1), 2: (1, 18),
        3: (2, 1), 4: (2, 2), 5: (2, 13), 6: (2, 14), 7: (2, 15), 8: (2, 16), 9: (2, 17), 10: (2, 18),
        11: (3, 1), 12: (3, 2), 13: (3, 13), 14: (3, 14), 15: (3, 15), 16: (3, 16), 17: (3, 17), 18: (3, 18),
        19: (4, 1), 20: (4, 2), 21: (4, 3), 22: (4, 4), 23: (4, 5), 24: (4, 6), 25: (4, 7), 26: (4, 8), 27: (4, 9), 28: (4, 10), 29: (4, 11), 30: (4, 12), 31: (4, 13), 32: (4, 14), 33: (4, 15), 34: (4, 16), 35: (4, 17), 36: (4, 18),
        37: (5, 1), 38: (5, 2), 39: (5, 3), 40: (5, 4), 41: (5, 5), 42: (5, 6), 43: (5, 7), 44: (5, 8), 45: (5, 9), 46: (5, 10), 47: (5, 11), 48: (5, 12), 49: (5, 13), 50: (5, 14), 51: (5, 15), 52: (5, 16), 53: (5, 17), 54: (5, 18),
        55: (6, 1), 56: (6, 2), 72: (6, 4), 73: (6, 5), 74: (6, 6), 75: (6, 7), 76: (6, 8), 77: (6, 9), 78: (6, 10), 79: (6, 11), 80: (6, 12), 81: (6, 13), 82: (6, 14), 83: (6, 15), 84: (6, 16), 85: (6, 17), 86: (6, 18),
        87: (7, 1), 88: (7, 2), 104: (7, 4), 105: (7, 5), 106: (7, 6), 107: (7, 7), 108: (7, 8), 109: (7, 9), 110: (7, 10), 111: (7, 11), 112: (7, 12), 113: (7, 13), 114: (7, 14), 115: (7, 15), 116: (7, 16), 117: (7, 17), 118: (7, 18)
    }

    output_file = open('periodic_table.html', 'w')

    output_file.write('<html lang="en">\n')
    output_file.write('<head>\n')
    output_file.write('<title>Periodic Table</title>\n')
    output_file.write('<meta charset="utf-8">\n')
    output_file.write('<style>\n')
    output_file.write('table{ border-collapse: collapse; }\n')
    output_file.write('td { border: 1px solid black; padding: 10px; text-align: center; }\n')
    output_file.write('</style>\n')
    output_file.write('</head>\n')
    output_file.write('<body>\n')
    output_file.write('<table>\n')

    for row in range(1, 8):
        output_file.write('<tr>\n')
        for col in range(1, 19):
            element = None
            for number, pos in positions.items():
                if pos == (row, col):
                    element = number
                    break
            if element:
                properties = elements[element]
                output_file.write('<td style="border: 1px solid black; padding: 10px;">\n')
                output_file.write(f'<h4>{element}</h4>\n')
                output_file.write('<ul>\n')
                output_file.write(f'<li>No {properties["number"]}</li>\n')
                output_file.write(f'<li>{properties["small"]}</li>\n')
                output_file.write(f'<li>{properties["molar"]}</li>\n')
                output_file.write(f'<li>{properties["electron"]} electron</li>\n')
                output_file.write('</ul>\n')
                output_file.write('</td>\n')
            else:
                output_file.write('<td></td>\n')
        output_file.write('</tr>\n')

    output_file.write('</table>\n')
    output_file.write('</body>\n')
    output_file.write('</html>\n')

    output_file.close()



if __name__ == '__main__':
    main()

