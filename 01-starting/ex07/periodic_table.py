
def parse_input_file(input_file):
    elements = {}
    for line in input_file:
        name, properties = line.strip().split('=')
        properties_dict = {}

        for prop in properties.split(','):
            key, value = prop.split(':')
            properties_dict[key.strip()] = value.strip()
        
        elements[name.strip()] = properties_dict
    
    return elements

def main():
    input_file = open('periodic_table.txt', 'r')
    elements = parse_input_file(input_file)
    input_file.close()


    output_file = open('periodic_table.html', 'w')

    # Write the HTML header
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

    for name, properties in elements.items():
        output_file.write('<tr>\n')
        output_file.write('<td style="border: 1px solid black; padding: 10px;">\n')
        output_file.write(f'<h4>{name}</h4>\n')
        output_file.write('<ul>\n')

        # Writing element properties in list format
        output_file.write(f'<li>No {properties["number"]}</li>\n')
        output_file.write(f'<li>{properties["small"]}</li>\n')
        output_file.write(f'<li>{properties["molar"]}</li>\n')
        output_file.write(f'<li>{properties["electron"]} electron</li>\n')


        output_file.write('</ul>\n')
        output_file.write('</td>\n')
        output_file.write('</tr>\n')

    output_file.write('</table>\n')
    output_file.write('</body>\n')
    output_file.write('</html>\n')

    output_file.close()



if __name__ == '__main__':
    main()

