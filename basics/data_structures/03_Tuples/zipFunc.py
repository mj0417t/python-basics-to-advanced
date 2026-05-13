a=[1,2,3]
b=['a','b','c']

res=zip()
print(list(res))

res=zip(a)
print(list(res))

res=zip(a,b)
print(dict(res))

names=['hiro','millei','tariq']
score=[23,3445]
res=zip(names,score)
print(list(res))

#unzipping data

shop=[('KFC',3),('Wow',2)]
franchise, outlet = zip(*shop)
print("Franchise: ", franchise)
print("Outlets: ",outlet)
