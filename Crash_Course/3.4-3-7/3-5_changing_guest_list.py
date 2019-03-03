#!/usr/bin/env python3


guests = ['emma watson', 'jennifer lawrence', 'blake lively']

upcomming_sched = "May 14, 2019 for "
statement = "The following celebrities will be able to join us on "
removal_statement = "The following celebrities will not be able to join us on "
previous_statement = "The previous celebrities could join us on "
where = "coachella music festival:"

print(previous_statement + upcomming_sched + where.title() + "\n" + guests[0].title() + "\n" + guests[1].title() + "\n" + guests[2].title())
print("\n" + removal_statement + upcomming_sched + where.title() + "\n" + guests[1].title())

guests[1] = 'megan fox'

print("\n" + statement + upcomming_sched + where.title() + "\n" + guests[0].title() + "\n" + guests[1].title() + "\n" + guests[2].title())
