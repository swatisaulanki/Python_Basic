def cube(num):return num*num*num
print(cube(3))


# second

def cubes(a):return a*a*a
result=cube(4)
print(result)

# if statement

# I wake up 

# if i'm hungry
    
# i eat breakfast

is_male= False
# is_male= True
if is_male:print("you are male")

else:print("you are not male")


# second

is_male=True
is_tall= True

if is_male or is_tall:
    print("you are a male or tall or both")

else:print("you neither male nor tall")


# third

def max_num(a,b,c): 
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    print(max_num(3,4,5))