s='gfg'
it=iter(s)
# print(next(it))
# print(next(it))
# print(next(it))

#iterate until StopIteration is raised
while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of Iteration")
        break