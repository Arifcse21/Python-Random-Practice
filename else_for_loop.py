#! /usr/bin/env python3

cars=['ok','ok','ok','ok','ok']

for status in cars:
    if status=='faulty':
        print('Faulty car skipped! ')
        #continue
        break
    print(f'this car is {status}')
    print('shipping new car to customer!')

else:
    print('All cars built successfullu. No faulty cars!')




