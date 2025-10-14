x = {100,200,300,400,500}
y = {200,400,600}
z = {100,200}

print('x union y : ', x.union(y))
print('y union z : ', y.union(z))
print('x intersection y : ', x.intersection(y))
print('y intersection z : ', y.intersection(z))
print('x difference z : ', x.difference(z))
print('z is subset x : ', z.issubset(x))
print('x is superset z : ', x.issuperset(z))