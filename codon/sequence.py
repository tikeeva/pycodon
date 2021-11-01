import os
from collections import Counter, defaultdict
from typing import Dict, List, Tuple
from itertools import product

from .codon import Codon
from .utils import data_from_file, make_codon, validation, get_ambiguous_nucleotides, make_multisequence


class Sequence():

    def __init__(self, 
                 sequence: str,
                 rna: bool = False) -> None:

        if os.path.isfile(sequence):
            sequence = data_from_file(sequence)

        validation(sequence)

        self.seq: str = sequence


        self.content: Dict[int, str] = defaultdict(str)
        self.multisequence: List[str] = []
        self.amb_nucleotides: Dict[str, List] = {}

        n = 0
        level: List[int] = [n]
        self.levels: List[List[int]] = [level]
        next_level: List[int] = []

        for i in range(0, len(sequence), 3):
            triplet = sequence[i:i+3]
            codons: List[Codon] = make_codon(triplet, rna=rna)

            if len(codons) == 1 and len(level) == 1:
                c: Codon = codons[0]
                self.content[n] += c.value
            else:
                for c in codons:
                    n += 1
                    next_level.append(n)
                    self.content[n] += c.value
                self.levels.append(level)
                level = next_level
                next_level = []

    def __repr__(self) -> str:
        return '\n'.join(self.all_sequences)

    def __str__(self) -> str:
        return ''.join(self.seq)

    def __len__(self) -> int:
        return len(self.multisequence[0])

    @property
    def nucleotide_counter(self) -> Counter:
        return Counter(self.seq)

    @property
    def all_sequences(self) -> List[str]:
        if not self.multisequence:
            self.multisequence =  make_multisequence(self.levels, self.content)
        return self.multisequence
    
    @property
    def ambiguous_nucleotides(self) -> List[str]:
        if not self.amb_nucleotides:
            self.amb_nucleotides = get_ambiguous_nucleotides(self.seq)
        return self.amb_nucleotides
