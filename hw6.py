

def area_triangle(h, w):
    return 0.5 * h * w





def distance(a,b):
    result = 0
    for i in range(len(a)):
        result += (a[i] - b[i])**2
    return result ** 0.5



    
    
    
def count(n):
    if n > 0 :
        print(n)
        return count(n-1)
    else :
        return 'zero!!'

    
    
    
    

area_triangle_ld = lambda h, w: 0.5 * h * w
