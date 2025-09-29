from Bio import SeqIO
from Bio.Seq import Seq


record = next(SeqIO.parse(./rosalind_pmch.txt", "fasta"))
seq= Seq(str(record.seq))


def factorial(n):
    f = 1
    for i in range(n):
        f *= (i+1)
    return f

def perfect_match(seq):
    
    A = seq.count('A')
    C = seq.count('C')
    
    
    return factorial(A) * factorial(C)
print(perfect_match(seq))
