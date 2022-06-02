#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    print(f"{i:c}" if i % 2 == 0 else chr(i-32), end='')
