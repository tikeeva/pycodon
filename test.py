from collections import defaultdict
from itertools import product
from dataclasses import dataclass
from typing import Optional, List


# triplet = 'WCC'
# triplet = list(map(iupac_nucleotides.get, triplet))
# triplet = list(product(*triplet))
# triplets = list(map(''.join, triplet))
# codons = [Codon(trip) for trip in triplets]
# print(codons)

# print(f'[{"".join(codon.value for codon in codons)}]')



# @dataclass
# class Node:
#     n: int
#     next_: Optional[List[int]] = None

# node = Node(10)
# print(node)

# my_dict = defaultdict(str)

# my_dict[1] += 'd'
# my_dict[1] +='ab'
# print(my_dict)

# seq = 'AAGCCTCTGTCAGCTCAGCCTCCAAAGGAGCCAGCGTCTCCCCAGTTCCTGAAATCCTGGGTGTTGCCTGCCAGTCGCCATGAGAACTTCCTACCTTCTGCTGTTTACTCTCTGCTTACTTTTGTCTGAGATGGCCTCAGGTGGTAACTTTCTCACAGGCCTTGGCCACAGATCTGATCATTACAATTGCGTCAGCAGTGGAGGGCAATGTCTCTATTCTGCCTGCCCGATCTTTACCAAAATTCAAGGCACCTGTTACAGAGGGAAGGCCAAGTGCTGCAAGTGAGCTGGGAGTGACCAGAAGAAATGACGCAGAAGTGAAATGAACTTTTTATAAGCATTCTTTTAATAAAGGAAAATTGCTTTTGAAGTATA'
# seq = 'GCACGTATGCCCCCGTCTAGCCGTATGGCCTACCGTGGTGCA'
# def cut_seq(seq: str) -> List[str]:
#     seqs: List[str] = []
#     for i in range(len(seq)):
#         ak = seq[i:i+3]
#         if ak == 'ATG':
#             seqs.append(seq[i:])
#     return seqs

# print(cut_seq(seq))

# print(list(product(*[[0], [1,2], [3,4], [5]])))

def data_from_file(file: str) -> str:
    with open(file) as f:
        first_row: str = f.readline()
        if first_row.startswith('>'):
            first_row = f.readline()
        next_row: str = f.readline()
        while next_row:
            first_row += next_row
            next_row = f.readline()
    return first_row.replace('\n', '').replace(' ', '')

print(data_from_file('data/sequence_6.fa'))