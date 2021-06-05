# This script takes a (txt) log file and filters out the final error message as required. 

#!/usr/bin/env python3
import argparse
import json
import os
import sys
import datetime

def input_value():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Name of the given JSON file')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    return args.filename

def open_file(filename):
    list_to_append = []
    data = open(filename, "r")
    data_list = data.readlines()
    for line in data_list:
        if line.startswith("Error"):
            list_to_append.append(line)
    return list_to_append

def filter_errors():
    filename = input_value()
    now = datetime.datetime.now()
    file_to_open = open('errors.txt', 'a')
    lines_with_error = open_file(filename)
    for lines in lines_with_error:
        if "exception_1" in lines:
            continue
        if "exception_2" in lines:
            continue
        if "exception_3" in lines:
            continue
        else:
            print(lines, end="")
            file_to_open.write(lines)

filter_errors()
