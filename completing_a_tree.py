# First row is number of nodes, n

# Make target of n-1 

# Each row after is an edge

# Count edges

# Subtract edges from value for n

filename = "./rosalind_tree.txt"

def determine_min_edges(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f:
            row = line.strip('\n')
            rows.append(row)
    return rows
        
    
rows = determine_min_edges(filename)

n = rows.pop(0)


rows_split = [i.split(' ') for i in rows]



edges_needed = int(n) - 1 - (len(rows_split))

print(edges_needed)