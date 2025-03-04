# Yeah, I know. What I'm doing is super basic. I haven't coded in years, since I've been working
# as an IT Technician / IT Support / System Administrator. I'm doing this for practice.

# If / Else statements
# Notice the indentation. Means that everything indented under/after the colon belongs under the
# if statement. Notice the IDE automatically indents the line too.

a = True
if a:
    print("This is true!")
    #print("Another block of text") if we added, this also belongs to the if statement
#print("Always print this") if we add another code here, it is always executed

# Another iteration just to make it clearer
a = False
if a:
    print("This is true!")
else:
    print("This is false!")

########################################################################################################

# For loops
a = [5,6,7,8,9]
for item in a:
    print(item)
# You can choose any word you want in place of "item" in this context

########################################################################################################

# While Loop is similar to for loop, except that it doesn't iterate over items in list
# It just keeps looping until the Boolean you pass is false
# The loop will not end if you don't have something to iteratively change the value
a = 0
while a < 5:
    print(a)
    a = a + 1

########################################################################################################


















