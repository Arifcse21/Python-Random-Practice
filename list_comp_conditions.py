#! /usr/bin/env python3


friends=["Rolf","ruth","charlie","Jen"]
guests=["Jose","Bob","Rolf","Charlie","michael"]

friends_lower=[f.lower() for f in friends]

present_friends=[
        name.title() for name in guests if name.lower() in friends_lower

]

print(present_friends)


friends_title=set(f.title() for f in friends)
guests_title=set(g.title() for g in guests)

print(friends_title.intersection(guests_title))
