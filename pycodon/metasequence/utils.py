from typing import Dict, List
from collections import defaultdict
from ..codon_dict import iupac_nucleotides

def make_nucleotides(nucl: str) -> List[str]:
    return [i for i in iupac_nucleotides[nucl]]

def validation(seq: str) -> None:
    diff = set(seq) - set(iupac_nucleotides.keys())
    if diff:
        raise ValueError(f'There are invalid nucleotides in sequence: {diff}. Or invalid path {seq}')

def get_ambiguous_nucleotides(seq) -> Dict[str, List[int]]:
    ambiguous_nucleotides: Dict[str, List[int]] = defaultdict(list)
    for i, nucl in enumerate(seq):
        if not nucl in 'ACGTU':
            ambiguous_nucleotides[nucl].append(i)
    return dict(ambiguous_nucleotides)
