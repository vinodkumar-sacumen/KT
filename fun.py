# write a python function to create list and print that list where the values are square of numbers between 1 and 20

# def printList():
#     list_ = list()       #create empty list to append values

#     for val in range(1,21):
#         list_.append(val**2)

#     print(list_)

#     #fucntion call
# printList()



# write function decorators

def to_capital(fun):
    def inner():
        a = fun()
        return a.upper()
    return inner


# @to_capital
def greet():
    return "fork demo"
print(greet())
