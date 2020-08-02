#!/usr/bin/python3

"""
Import json object into class
"""
import sys
import json
from typing import List
from lead import Lead
from contact import Contact


def data_filter(data: dict) -> dict:
    """
        data validation
        change the data into None datatype if the string is 'None'
        change the ['phone'] into int
    """
    new_data: dict = {}
    if data['name'] == 'None':
        new_data['name'] = None
    else:
        new_data['name'] = data['name']

    if data['email'] == 'None':
        new_data['email'] = None
    else:
        new_data['email'] = data['email']

    if data['phone'] == 'None':
        new_data['phone'] = None
    else:
        new_data['phone'] = int(data['phone'])

    return new_data


def to_string(lst: List[dict]) -> bool:
    """
    print the variables of every class in list
    """
    for node in lst:
        node.to_string()


def main():
    """ main CLI entry """
    if len(sys.argv) < 2:
        sys.exit('Please provide .json file')

    # empty contact list and lead list
    contactsList: List[Contact] = []
    leadsList: List[Lead] = []

    # open all .json files
    for arg in sys.argv[1:]:
        with open(arg) as file:
            data = json.load(file)
            #print(type(data['contacts'][0]['phone'])) # test
            # put it in contact list if it's contact data
            if data['contacts']:
                data = data['contacts']
                # loop through every single data in the list,
                # put them into contactsList
                for index in data:
                    # filter the data
                    filtered: dict = data_filter(index)
                    contactsList.append(Contact(filtered['name'],
                                                filtered['email'],
                                                filtered['phone']))

    # end of for loops
    to_string(contactsList)



if __name__ == '__main__':
    main()
