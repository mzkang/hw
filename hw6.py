

def area_triangle(h, w):
    return 0.5 * h * w





def distance(a,b):
    result = 0
    for i in range(len(a)):
        result += (a[i] - b[i])**2
    return result ** 0.5



    
    
#============??????????????????????return.....??????????????????/=============================

def count(n):
    if n > 0 :
        print(n)
        return count(n-1)
    else :
        return 'zero!!'
    
x = count(5)
print()
print(x)
#=============================================================================================
    
    
def count(n):
    if n > 0 :
        print(n)
        count(n-1)
    else :
        print('zero!!')

x = count(5)
print()
print(x)    
    
    

area_triangle_ld = lambda h, w: 0.5 * h * w
