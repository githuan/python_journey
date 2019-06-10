#!/usr/bin/env python3


def build_person(first_name, last_name, middle_name='', age=None):
    """Return a dictionary of information about a person.""" 
    person = {'first': first_name, 'middle': middle_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jim', 'hendrix','' , '33')
print(musician)

librarian = build_person('john', 'doe', 'lee')
print(librarian)

cook = build_person('lea', 'sand', 'green', '19')
print(cook)

electrician = build_person('aleksandr', 'mikhailov', 'anastasia', '24')
print(electrician)

geometrist = build_person('ben', 'schmidt', 'becker', '28')
print(geometrist)
