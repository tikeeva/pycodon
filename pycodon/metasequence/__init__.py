from collections import defaultdict, Counter
from itertools import product
from typing import Dict, List

from ..sequence import Sequence

from .utils import get_ambiguous_nucleotides, make_nucleotides, validation


class Metasequence:

    def __init__(self, sequence: str, rna: bool = False) -> None:
        validation(seq=sequence)
        self.seq: str = sequence        
        self.rna = rna
        self._amb_nucleotides: Dict[str, List[int]] = []
        self._content: Dict[int, str] = defaultdict(str)
        n = 0
        level: List[int] = [n]
        self._levels: List[List[int]] = [level]
        next_level: List[int] = []

        for nucl in sequence:
            nucleotides: List[str] = make_nucleotides(nucl)
            if len(nucleotides) == 1 and len(level) == 1:
                self._content[n] += nucleotides[0]
            else:
                for nucl_ in nucleotides:
                    n += 1
                    next_level.append(n)
                    self._content[n] += nucl_
                self._levels.append(level)
                level = next_level
                next_level = []

    def make_sequences(self) -> List[Sequence]:
        sequences: List[Sequence] = []
        paths = product(*self._levels)
        for path in paths:
            seq = ''
            for node in path:
                seq += self._content[node]
            sequences.append(Sequence(seq, rna=self.rna))
        return sequences

    @property
    def ambiguous_nucleotides(self):
        if not self._amb_nucleotides:
            self._amb_nucleotides = get_ambiguous_nucleotides(self.seq)
        return self._amb_nucleotides


    @property
    def count_nucleotides(self) -> Counter:
        Counter(self.seq)