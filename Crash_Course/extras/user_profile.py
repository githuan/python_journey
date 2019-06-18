#!/usr/bin/env python3


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user:"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile01 = build_profile('rachel', 'smith',
                             location='new york',
                             field='physics')
user_profile02 = build_profile('thuan', 'nguyen',
                             location='new york',
                             field='aws devops')
user_profile03 = build_profile('tharos', 'victok',
                             location='moscow',
                             field='scientist',
                               race='caucasian')
user_profile04 = build_profile('elena', 'kovic',
                             location='ukriane',
                             field='scientist',
                               race='caucasian',
                               currency='$')
user_profile05 = build_profile('Bo', 'Ino',
                             location='north carolina',
                             field='enery engineer',
                               age='35',
                               religious='buddish')


print(user_profile01)
print(user_profile02)
print(user_profile03)
print(user_profile04)
print(user_profile05)
