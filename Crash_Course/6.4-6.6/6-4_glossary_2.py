#!/usr/bin/env python3


few_py_glossary = {
    'variable':'holds a value; sometimes, it holds an empty value.',
    'string':'considers as text within double quotes \"\" or single quote \'\'.',
    'list':'is a series of items that enclosed by square brackets [] and separate each item by a comma ",".',
    'tuple':'is an immutable list that enclosed by parenthesis () and also separate each item by comma ",".',
    'dictionary':'is a key-value pair. Think of it as a way to store any two kinds of information that can be matched up. Dictionary also separate each item by a comma ",". however, the related pair information is separated by a semi-colon ":"',
    'if':'A conditional test of boolens "True" or "False". We can test multiple condition with "and" or "or" word',
    'elif':'Works in conjunction with "if". It will only execute a block of code of "if" or "elif" meets the requirement',
    'item()':'Method item() is pairing up with for loop to iterate through dictionary list',
    'key() and value()':'These two methods will for loop will iterate through dictionary list. key() will iterate through key; value () will iterate through value',
    'sorted() and set()':'combines sortet() with for loop to get keys in order. Method set() combine with for loop to avoid repetative result for values',
    }

for word, definition in few_py_glossary.items():
    print(word + ": " + definition.capitalize())
