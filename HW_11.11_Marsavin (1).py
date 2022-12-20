import csv 
import json 

def read_data(file_name):
    file = open(file_name, 'r')
    content = file.read().splitlines()
    return content
    
def write_data(file_name, content):
    file = open(file_name, "w")
    file.write(content)
    file.close()

def space(whitespace_count):
    return whitespace_count * ' '

def format(key, value):
    return space(4) + quotes(key) + ': ' + value
    
def quotes(data):
    return '"' + data + '"'

def value_type(value):
    if len(value) == 0:
        return 'null'
    if value.isalpha():
        if value !='True' and value !='False':
            return quotes(value)
        return value.lower()
    else:
        return value

def convert_content(csv_content, spliterator=','):
    if len(csv_content) < 2:
        return '[]'
    keys = csv_content[0].split(spliterator)
    result = '[' + '\n'
    row_count = len(csv_content[1:])

    for row_i, row in enumerate(csv_content[1:]):
        result += space(2) + '{' + '\n'
        values = row.split(spliterator)
        zipped_key_value = dict(zip(keys, values))
        len_my_dict = len(zipped_key_value)

        for key_i, key in enumerate(zipped_key_value):
            result += format(key, value_type(zipped_key_value[key]))
            if key_i + 1 != len_my_dict:
                result += ','
            result += '\n'

        result += space(2) + '}'
        if row_i + 1 != row_count:
            result += ','
        result += '\n'
    result += ']'
    return result

def convert(input_file_path, output_file_path):
    csv_content = read_data(input_file_path)
    json_result = convert_content(csv_content)
    write_data(output_file_path, json_result)

convert('input.csv', 'output.json')
