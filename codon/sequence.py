import os
from collections import Counter, defaultdict
from typing import Dict, List

from .codon import Codon
from .utils import data_from_file, make_codon, validation, get_ambiguous_nucleotides, make_multisequence


class Sequence():

    def __init__(self, 
                 sequence: str,
                 rna: bool = False) -> None:
        self.sequence = sequence
        self.rna = rna


    def __repr__(self) -> str:
        return self.sequence

    def __str__(self) -> str:
        return self.sequence

    def __len__(self) -> int:
        return len(self.sequence)

    @property
    def nucleotide_counter(self) -> Counter:
        return Counter(self.sequence)

    # @property
    # def all_sequences(self) -> List[str]:
    #     if not self.multisequence:
    #         self.multisequence =  make_multisequence(self.levels, self.content)
    #     return self.multisequence
    
    # @property
    # def ambiguous_nucleotides(self) -> List[str]:
    #     if not self.amb_nucleotides:
    #         self.amb_nucleotides = get_ambiguous_nucleotides(self.seq)
    #     return self.amb_nucleotides
