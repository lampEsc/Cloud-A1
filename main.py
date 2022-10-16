from random import randint
from time import time


'''max =  int(input("Please input desired size of end matrix: "))'''
max=100
n = 2
start = time()
def random_matrix(n):

    a = [[] for i in range(n)]

    for i in range(0, n*n):
        r = i % n
        a[r].append(randint(0, 10))

    return a

def multiply_matrices(a, b, n):

    result = [[] for i in range(n)]

    for i in range(0, n*n):
        r = i % n
        result[r].append(0)
    
    for i in range(len(a)):
 
        for j in range(len(b[0])):
    
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    
    return result

while n<=max:
    a = random_matrix(n)
    b = random_matrix(n)
    result = multiply_matrices(a, b, n)
    #print(result, end = "\n\n")
    if (n - 1) % 20 == 0:
        now = time()
        
        print("It took %f seconds to reach %d iterations." % (round(now - start, 5), n-1))
    n+=1

end = time()
print(round(end - start, 5), "seconds. This was how long the program took to execute.")