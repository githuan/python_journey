#!/usr/bin/env python3


few_py_glossary = {
    'variable':'holds a value; sometimes, it holds an empty value.',
    'string':'considers as text within double quotes \"\" or single quote \'\'.',
    'list':'is a series of items that enclosed by square brackets [] and separate each item by a comma ",".',
    'tuple':'is an immutable list that enclosed by parenthesis () and also separate each item by comma ",".',
    'dictionary':'is a key-value pair. Think of it as a way to store any two kinds of information that can be matched up. Dictionary also separate each item by a comma ",". however, the related pair information is separated by a semi-colon ":"',
    }

print(
    "Variable: " + few_py_glossary['variable'] +
    "\nString: " + few_py_glossary['string'] +
    "\nList: " + few_py_glossary['list'] +
    "\nTuple: " + few_py_glossary['tuple'] +
    "\nDictionary: " + few_py_glossary['dictionary']
    )
