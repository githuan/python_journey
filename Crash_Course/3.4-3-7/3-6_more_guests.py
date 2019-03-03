#!/usr/bin/env python3


guests = ['emma watson', 'jennifer lawrence', 'blake lively']

upcomming_sched = "May 14, 2019 for "
statement = "The following celebrities will be able to join us on "
additional_statement = "Adding more celebrity will be able to join us on "
previous_statement = "The previous celebrities could join us on "
where = "coachella music festival:"

print(previous_statement + upcomming_sched + where.title() + "\n" + guests[0].title() + "\n" + guests[1].title() + "\n" + guests[2].title())

guests.insert(0, 'megan fox')
print("\n" + additional_statement + upcomming_sched + where.title() + "\n" + guests[0].title())

guests.insert(2, 'taylor swift')
print("\n" + additional_statement + upcomming_sched + where.title() + "\n" + guests[2].title())

guests.append('jessica biel')
print("\n" + additional_statement + upcomming_sched + where.title() + "\n" + guests[-1].title())

print("\n" + statement + upcomming_sched + where.title() + "\n" + guests[0].title() + "\n" + guests[1].title() + "\n" + guests[2].title() + "\n" + guests[3].title() + "\n" + guests[4].title() + "\n" + guests[5].title())
