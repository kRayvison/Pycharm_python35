# a = {'A':{'aa':'asdffa'},'B':'ccccc'}
#
# if 'aa' in a['A']:
#     print (a['A'])


import re

w2 = '34A5'
a = re.findall('^\d?\D',w2)

print (a)

if a:
    w2=w2.replace(a[0],'')
print (w2)