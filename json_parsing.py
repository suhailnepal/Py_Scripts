#!/usr/bin/env python3.6
import argparse
import json
import os

def input_value():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Name of the given JSON file')
    args = parser.parse_args()
    return args.filename

def converting_json_file(filename):
    try:
        file_open = open(filename)
        filecontent_read = file_open.read()
        filecontent_load = json.loads(filecontent_read)
        return filecontent_load
    except FileNotFoundError:
        print(f'The file {filename} does not exist', filename=sys.stderr)
        exit(1)

def print_statement():
    file = input_value()
    file_object = converting_json_file(file)
    for index in file_object['Reservations']:
        print(f"Hello {index['Instances']}")

print_statement()
