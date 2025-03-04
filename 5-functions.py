# Yeah, I know. What I'm doing is super basic. I haven't coded in years, since I've been working
# as an IT Technician / IT Support / System Administrator. I'm doing this for practice.

# Values inside the parenthesis of function is called arguments
# naming functions: start with lowercase letter, you can't start with a number
# we use def (short for definition) to define a function
# you can use underscore, not just in the beginning
# just like in if and loop statements, colon means we indent, it belongs to the statement of function
def multiply_by_three(argunment01):
    return 3 * argunment01
# in functions, we usually return something, a result

print(multiply_by_three(3))


def multiply(value01, value02):
    return value01 * value02
print(multiply(10, 89))

# another example
a = [1,2,3]
def appendFour(myList):
    myList.append(4)

appendFour(a)
print(a)
# you don't always want to return a value, you can use it for later















