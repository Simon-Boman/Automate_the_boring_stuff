spam = 42 # global variable (in global scope). Created when program starts, destroyed when program ends. 

def eggs():
    spam = 35345 #local variable (in local scope). They are temporary. Only exist in eggs - created when function is called, destroyed when function returns.   
    print(spam)
#on execution of function, starts by looking in local scope, if local variable by name spam doesnt exist, we will use global.
#so, if we have an assignment statement in function = local variable!!!!
#if no assignment statemenet, i.e. we would have print(spam) = global variable!!!!


#will print local variable spam = 35345.
#if we comment out the local variable assignment, it will print global variable spam = 42.
eggs()



# if want to change value of global variable inside function:
def eggs2():
    global eggs #defines eggs in this function to always refer to the global eggs - dont create separate local eggs! 
    eggs = 'Hello'
    print(eggs)

eggs2()

print(eggs)

# isolate code - so the cause of bugs limited to a particular area of the program. 
# local scopes let you treat functions as black boxes - all that matters are your parameters in and the return value.
# easier to track and find bugs, if something is going wrong inside function, or with global variable. 