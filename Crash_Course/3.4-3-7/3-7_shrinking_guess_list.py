#!/usr/bin/env python3


guests = ['emma watson', 'jennifer lawrence', 'blake lively']

upcomming_sched = "May 14, 2019 for "
statement = "The following celebrities will be able to join us on "
additional_statement = "Adding more celebrity will be able to join us on "
cancel_statement = "Celebrity has cancelled ticket on "
previous_statement = "The previous celebrities could join us on "
final_statement = "No celebrity could join us on "
where = "coachella music festival:"

print(previous_statement + upcomming_sched + where.title() + "\n" + guests[0].title() + "\n" + guests[1].title() + "\n" + guests[2].title())

guests.insert(0, 'megan fox')
print("\n" + additional_statement + upcomming_sched + where.title() + "\n" + guests[0].title())

guests.insert(2, 'taylor swift')
print("\n" + additional_statement + upcomming_sched + where.title() + "\n" + guests[2].title())

guests.append('jessica biel')
print("\n" + additional_statement + upcomming_sched + where.title() + "\n" + guests[-1].title())

print("\n" + statement + upcomming_sched + where.title() + "\n" + guests[0].title() + "\n" + guests[1].title() + "\n" + guests[2].title() + "\n" + guests[3].title() + "\n" + guests[4].title() + "\n" + guests[5].title())

print("\n" + cancel_statement + upcomming_sched + where + "\n" + guests.pop(0).title())
print("\n" + cancel_statement + upcomming_sched + where + "\n" + guests.pop(1).title())
print("\n" + cancel_statement + upcomming_sched + where + "\n" + guests.pop(1).title())
print("\n" + cancel_statement + upcomming_sched + where + "\n" + guests.pop().title())

print("\n" + cancel_statement + upcomming_sched + where + "\n" + guests[0].title() + " and " + guests[1].title())
del guests[0]
del guests[0]

print("\n" + final_statement + upcomming_sched + where.title())
print(guests)
