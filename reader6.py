#!/usr/bin/env python

import re  #import library needed to do string search
data = {}  #initialize an empty dictionary

#
#  define function that searches values in dictionary
#  
def search_dictionary_by_partial_match(dictionary, value):
  for key, value_ in dictionary.items():
    if re.search(value, str(value_)):
      print(key, value_)

#
#  Main program that reads input file and builds dictionary
#
with open("text_file.txt",'r') as fh:
    for line in fh.readlines(): #read in multiple lines
        if len(line.strip())==0:  #take care of emplty line
            continue              # Yoshi's famous continue

        if line.startswith('ACCOUNT_ID'):
            nameLine = line.strip()
            name = nameLine.split(": ")[1]
            data[name] = {}
        else:
            splitLine = line.split(":")
            variableName = splitLine[0].strip()
            value = splitLine[1].strip()
            data[name][variableName] = value


#
# Ask user for search term and print results to screen
#
My_Search_Term = input("Enter a search term:")
print("Searching for : " + My_Search_Term)

search_dictionary_by_partial_match(data, My_Search_Term)
