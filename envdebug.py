def greet(a):
    for i in range(a):
        print("Good Morning", i + 1)


"""debug start"""
pdb.set_trace()
greet(5)
