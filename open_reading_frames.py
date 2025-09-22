from Bio import SeqIO
from Bio.Seq import Seq


record = next(SeqIO.parse("r./rosalind_orf.txt", "fasta"))
sequence = Seq(str(record.seq))

def parse_orfs(sequence):
    proteins = set()
    stop_codons = {"TAA", "TAG", "TGA"}

    def scan_strand(seq):
        
        results = set()
        for i in range(len(seq) - 2):
            codon = str(seq[i:i+3])
            if codon == "ATG":
                sub_seq = seq[i:]
                # check if a stop codon exists
                for j in range(0, len(sub_seq) - 2, 3):
                    stop = str(sub_seq[j:j+3])
                    if stop in stop_codons:
                        prot = sub_seq.translate(table=1, to_stop=True)
                        results.add(str(prot))
                        break
        return results

    # forward strand
    proteins.update(scan_strand(sequence))
    # reverse complement
    proteins.update(scan_strand(sequence.reverse_complement()))

    return proteins


print(parse_orfs(sequence))