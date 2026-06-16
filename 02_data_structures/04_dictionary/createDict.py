names = ['john', 'ala', 'ilia', 'sudan', 'mercy'] 
marks = [100, 200, 150, 80, 300]
res=dict()
for x in names:
    for y in marks:
        res[x]=y
print(res)