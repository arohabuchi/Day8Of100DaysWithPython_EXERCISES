########################################## DAY 8 ##################################################
#TOPIC 1: Variable scope and binding
#nonlocal:this add a scope override to the inner scope

#python code can refer to a namein any encloing scope, but it can only bindor rebind name in two scope:
#1. local scope
#2. global scope

###################### Local scope #####################################
def counter():
    num=0
    def increment():
        nonlocal num
        num = num+1
        print(num)
    return  increment()

counter()


############################ Global variable ############################################

p=30
def cd():
    global p
    print(p)
    p = 90
    print(p)
cd()

#################################### Diff between nonlcal and global ##############################
#nonlocal belong to an enclosing function but at the same time above the function of it applicattion
#global variable is out/above tthe enclosing function

p=9
def cg():
    num=0
    def inc():
        nonlocal num
        global p
        num=num+3
        p=p+4
        print(p)
        print(num)
    return inc()
cg()

############################### local variable #######################
#thi bounded inside a function and i accessible within that function by default
def goo():
    a="food"
    print(a)
goo()

############################## del function ########################
#it removes a variable from a scope

def de():
    v=90
    del v
   #print(v)

############## name clashes #############
# when to variable name clashes the local variable overrides  the global variable
f=11
def ccz():
    global f
    print(f)
    f=8
    print(f)
ccz()



#####################################################################################################################
####################################################### TOPIC 2 #########################################################
######################################################## CONDITION STATEMENT #############################################

# TERNARY OPERATORS (<, >)
n= 4
if n>2:
    print(n)

# if, elif, else statement

if n == 7:
    print(n)
elif n >7:
    print("greater than ")
elif n==4:
    print("n=4")
elif n<4:
    print("n<4")
else:
    print("n not a valid number")

###################################### True value #############################
#All values in python evaluate tto true except FALSE, NONE, 0, "", '',  (), [], {}, and uer defined method to return false

###############################OTHER value #######################
# and, or, is

####################### COMPARISM == ################
#CHAIN COMPARISM
x,y,z=1,2,4
N=x<y>z
#greater/less (>,<)
if x>0:
    pass
if y<x:
    pass

#not equal to !=
if x != 0:
    pass

#equal to ==
if x ==y:
    pass


#################################################################################################################################
#################################################### LOOPS ######################################################################

#BREAK AND CONTINUE IN LOOP
#break is use to break out of a loop
i=0
while i<10:
    print(i)
    if i==7:
        print("break out")
        break
    i+=1

#with continues it will skip to the next loop count

for i in range(1,9):

    if i == 7:
        print("jump 7")
        continue
    print(i)
    i += 1

################################## FOR LOOPS #############################################
for i in [1,1,2,3,4,3,4,5,6,7]:
    print(i)

#iterating over a list
for i in ['leo','ike','otti','obi']:
   print(i)


#iterating over dictionary
d={'a': 1,'c': 3,'v': 7,'n':9}

#print only the keys
for key in d.keys():
    print(key)

#print only the values
for v in d.values():
    print(v)

#print both key and values
for k,v in d.items():
    print(k ,":" ,v)


#iterating over a list and printing the first letter

lst =['leo','ike','otti','obi']
for f in lst:
    print(f[:1])

##################### while loop #########################
i = 0
while i <4:
    print(i)
    i = i +1
#loop till infinity
while True:
    pass
    # print("infinity here e go...") # BAD PRACTICE

