#!/usr/bin/env python3
friends=['Rolf','Bob','Jen','Anne']
time_since_seen=[3,7,15,11]

long_timers={
    friends[i]:time_since_seen[i]
    for i in range(len(friends))
}
print(long_timers)

long_timers=dict([('Rolf',3),('Bob',7),('Jen',15),('Anne',11)])
print(long_timers)
