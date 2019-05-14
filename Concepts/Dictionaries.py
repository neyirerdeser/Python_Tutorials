import random
import sys
import os

# or maps (maps key to data)

# you cant join maps like lists

super_villains = {'fiddler' : 'isaac',
                  'pied piper' : 'thomas',
                  'weather wizard': 'mark'}
print(super_villains['weather wizard'])
del super_villains['fiddler'] # just like lists

super_villains['pied piper'] = 'hartley'
len(super_villains)

print(super_villains.get('pied piper'))
print(super_villains.keys())
print(super_villains.values())
