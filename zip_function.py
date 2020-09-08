#! /usr/bin/env python3

friends = ['Rolf' , 'Bob' , 'Jen' , 'Anne']
time_since_seen = [3,7,15,11]
long_timers = dict(zip(friends,time_since_seen))
print(long_timers)

long_timers = list(zip(friends,time_since_seen,[1,2,3,4,5]))
print(long_timers)

