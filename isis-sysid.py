import re

val = input("Enter IP: ")
ip = (val)
padded_octets = [f'{x:>03}' for x in ip.split('.')]
joined_octets = ''.join(padded_octets)
re_split = '.'.join(re.findall('....', joined_octets))
result = '.'.join(['49.0000', re_split, '00'])

print(result)
