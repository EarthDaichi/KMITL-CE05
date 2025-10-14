name = {'Hideaki','Tomohisa','Masaki','Ninomiya','Sho','Ryo','Yuta'}
print(f"{"-"*7} Display 1st time {"-"*7}")
for x in name:print(x, end=" ")

name.add('Hiroki')
name.add('Kato')
print(f"\n{"-"*7} Display 2nd time {"-"*7}")
for x in name:print(x, end=" ")