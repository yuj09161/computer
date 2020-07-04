import os

with open('computer.circ','r') as file:
    data=file.readlines()

os.rename('./computer.circ','./computer_back.circ')

for a in range(8):
    data.insert(1718+a,
        '\n    '.join((
            ' '*6+'<comp lib="0" loc="(150,%d)" name="Pin">' %(30+30*a),
            '<a name="tristate" val="false"/>',
            '<a name="label" val="%s"/>' %('C'+str(a)),
            '</comp>'
        ))
    )
for b in range(8):
    data.insert(1718+b,
        '\n    '.join((
            '<comp lib="0" loc="(150,%d)" name="Pin">' %(30+30*(b+8)),
            '<a name="tristate" val="false"/>',
            '<a name="label" val="%s"/>' %('D1'+str(b)),
            '</comp>'
        ))
    )
for c in range(8):
    data.insert(1718+c,
        '\n    '.join((
            '<comp lib="0" loc="(150,%d)" name="Pin">' %(30+30*(c+16)),
            '<a name="tristate" val="false"/>',
            '<a name="label" val="%s"/>' %('D2'+str(c)),
            '</comp>'
        ))
    )

print(data)

with open('computer.circ','w') as file:
    for line in data:
        file.write(line)
