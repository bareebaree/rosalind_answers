"""
Simple answer to recurrence problem on Rosalind.
"""

# Replace n and k with values from Rosalind.
n = 0
k = 0


def recursion(n,k):

    f = [1, 1]
    
    while len(f) < n:     
        result = f[-1]+ f[-2]*k
        f.append(result)
        
    return(f[-1]) 

print(recursion(n,k))
