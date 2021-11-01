from collections import defaultdict
from typing import Dict, List, Tuple
from itertools import product

from .codon_dict import iupac_nucleotides
from .codon import Codon


def validation(seq: str) -> None:
    diff = set(seq) - set(iupac_nucleotides.keys())
    if diff:
        raise ValueError(f'There are invalid nucleotides in sequence: {diff}. Or invalid path {seq}')
    if len(seq) % 3:
        raise ValueError(f'Sequence must have length divisible by 3. Sequence length equals {len(seq)}')


def data_from_file(file: str) -> str:
    with open(file) as f:
        first_row: str = f.readline()
        if first_row.startswith('>'):
            first_row = f.readline()
    return first_row


def make_codon(triplet: str, rna: bool) -> List[Codon]:
    codons: List[Codon] = []
    if not set(triplet) - set('ACGT'):
        codons.append(Codon(triplet, rna=rna))
    else:
        triplets: List[str] = list(map(iupac_nucleotides.get, triplet))
        triplets: List[Tuple[str, str, str]] = list(product(*triplets))
        triplets: List[str] = list(map(''.join, triplets))
        for trip in triplets:
            codon: Codon = Codon(trip, rna=rna)
            if not codon in codons:
                codons.append(codon)
    return codons


def get_ambiguous_nucleotides(seq) -> Dict[str, List[int]]:
    ambiguous_nucleotides: Dict[str, List[int]] = defaultdict(list)
    for i, nucl in enumerate(seq):
        if not nucl in 'ACGTU':
            ambiguous_nucleotides[nucl].append(i)
    return dict(ambiguous_nucleotides)



def make_multisequence(levels: List[List[int]], content: Dict[int, str]) -> List[str]:
    paths: Tuple[Tuple[int, ...]] = tuple(product(*levels))
    multisequence: List[str] = []
    for i, path in enumerate(paths):
        multisequence.append('')
        for node in path:
            multisequence[i] += content[node]
    return multisequence
