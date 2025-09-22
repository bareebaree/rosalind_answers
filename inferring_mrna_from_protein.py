import numpy as np

with open("./rosalind_mrna.txt", "r") as f:
    string = f.read()


def enumuerate_rna(string):
    array = []
    codon_count = {
    "F": 2,  # Phenylalanine
    "L": 6,  # Leucine
    "I": 3,  # Isoleucine
    "M": 1,  # Methionine
    "V": 4,  # Valine
    "S": 6,  # Serine
    "P": 4,  # Proline
    "T": 4,  # Threonine
    "A": 4,  # Alanine
    "Y": 2,  # Tyrosine
    "H": 2,  # Histidine
    "Q": 2,  # Glutamine
    "N": 2,  # Asparagine
    "K": 2,  # Lysine
    "D": 2,  # Aspartic acid
    "E": 2,  # Glutamic acid
    "C": 2,  # Cysteine
    "W": 1,  # Tryptophan
    "R": 6,  # Arginine
    "G": 4,  # Glycine
    "*": 3   # Stop codons (UAA, UAG, UGA)
    }
    for i in string:
        if i in codon_count:
            array.append(codon_count[i])
    array = np.array(array, dtype=object)   # cast as object to avoid interger overflow
    array_prod = np.prod(array)%1000000     
    return array_prod
    
print(enumuerate_rna(string))
            

    

