import numpy as np

with open("./rosalind_prtm.txt", "r") as f:
    seq = f.read()

def calculate_protein_mass(seq):
    array = []
        # Average residue masses in daltons (no H2O, standard values)
    aa_masses = {
        "A": 71.03711,   # Alanine
        "C": 103.00919,  # Cysteine
        "D": 115.02694,  # Aspartic acid
        "E": 129.04259,  # Glutamic acid
        "F": 147.06841,  # Phenylalanine
        "G": 57.02146,   # Glycine
        "H": 137.05891,  # Histidine
        "I": 113.08406,  # Isoleucine
        "K": 128.09496,  # Lysine
        "L": 113.08406,  # Leucine
        "M": 131.04049,  # Methionine
        "N": 114.04293,  # Asparagine
        "P": 97.05276,   # Proline
        "Q": 128.05858,  # Glutamine
        "R": 156.10111,  # Arginine
        "S": 87.03203,   # Serine
        "T": 101.04768,  # Threonine
        "V": 99.06841,   # Valine
        "W": 186.07931,  # Tryptophan
        "Y": 163.06333   # Tyrosine
    }
    
    for i in seq:
        if i in aa_masses:
            array.append(aa_masses[i])
    array = np.array(array, dtype=object) 
    array_sum = np.sum(array)
    return array_sum

print(calculate_protein_mass(seq))