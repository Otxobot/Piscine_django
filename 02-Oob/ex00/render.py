import sys
import os
import re
import settings

def replace_variables(filename: str):
    with open(filename, "r") as file:
        template_text = file.read()

    matches = re.findall(r"\{(\w+)\}", template_text)
    for match in matches:
        if hasattr(settings, match):
            template_text = re.sub(rf"\{{{match}\}}", getattr(settings, match), template_text)

    return template_text

def main():
    n = len(sys.argv)
    if (n != 2):
        print("Incorrect number of arguments")
        exit(1)
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("Error: File does not exist")
        exit(1)
    name, ext = os.path.splitext(filename)
    if ext != ".template":
        print("Error: Wrong file extension")
        exit(1)
    output_filename = name + ".html"

    template_text = replace_variables(filename)

    with open(output_filename, "w") as output_file:
        output_file.write(template_text)
    

if __name__ == '__main__':
    main()