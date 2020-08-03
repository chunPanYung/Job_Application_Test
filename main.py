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


def filter_registrant(contact: List[Contact], lead: List[Lead],
                      registrant: List):
    """
    1) Check to see if registrant's phone or email matche contact list,
       update with new info if it doesn't exists.
    2) Repeat for lead list.
    3) If it's matched with lead list, remove from lead list and add to contact
       list
    4) If no match from lead list, simply add them to contact list
    """
    # cycle through each node in registrant list
    for node_reg in registrant:
        filtered = data_filter(node_reg)
        added: bool = False
        # check with contact list first
        for node_contact in contact:
            # if the registrant's email or phone is matched with contact list
            # (excluding 'None' matches with 'None'),
            # try updating it if empty in the node
            if (
                    (node_contact.get_email() == filtered['email'] and
                     filtered['email'] is not None)
                    or
                    (node_contact.get_phone() == filtered['phone'] and
                     filtered['phone'] is not None)
            ):  # end of if condition
                node_contact.set_email(filtered['email'])
                node_contact.set_phone(filtered['phone'])
                added = True
        # check with lead list
        for node_lead in lead:
            # if the registrant's email or phone is matched with lead list
            # (excluding 'None' matches with 'None'),
            # try updating them if it's there's new value
            if (
                    (node_lead.get_email() == filtered['email'] and
                     filtered['email'] is not None)
                    or
                    (node_lead.get_phone() == filtered['phone'] and
                     filtered['phone'] is not None)
            ):  # end of if condition
                node_lead.set_name(filtered['name'])
                node_lead.set_email(filtered['email'])
                node_lead.set_phone(filtered['phone'])
                # append it into contact list and remove them from lead list
                contact.append(node_lead)
                lead.remove(node_lead)
                added = True
        # if added: bool is still False here, it means it doesn't find match
        # in both lead and contact list.  Add them directly into contact list
        if not added:
            contact.append(Contact(filtered['name'],
                                   filtered['email'],
                                   filtered['phone']))



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
            # put it in contact list if it's contact data
            if 'contacts' in data:
                # loop through every single data in the list,
                # put them into contactsList
                for node in data['contacts']:
                    # filter the data
                    filtered: dict = data_filter(node)
                    contactsList.append(Contact(filtered['name'],
                                                filtered['email'],
                                                filtered['phone']))
            # put it in lead list if it's lead data
            if 'leads' in data:
                # loop through every single data in the list,
                # put them into contactsList
                for node in data['leads']:
                    # filter the data
                    filtered: dict = data_filter(node)
                    leadsList.append(Lead(filtered['name'],
                                          filtered['email'],
                                          filtered['phone']))
            # filter data in registrants .json
            if 'registrants' in data:
                filter_registrant(contactsList, leadsList, data['registrants'])


    # end of for loops
    print('===CONTACT LIST===')
    to_string(contactsList)
    print('===LEADS LIST===')
    to_string(leadsList)



if __name__ == '__main__':
    main()
