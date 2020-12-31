a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(f"Middle two: {a[3:5]}")


colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
