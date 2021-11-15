from __future__ import annotations

from collections import Counter
from typing import Iterable, List, Optional, Union

from .utils import make_protein, make_sequences, indexcheck, prot_frame_pos, valid_frame
from collections import abc

class Sequence(abc.Sequence):

    def __init__(self, 
                 sequence: str,
                 rna: bool = False) -> None:
        self.sequence: str = sequence
        self.rna: bool = rna
        self._prot: str = ''

    @indexcheck
    def __getitem__(self, index: int) -> Union[Sequence, str]:
        if isinstance(index, int):
            return self.sequence[index]
        else:   # if index is tuple of indices
            return Sequence(sequence=''.join(self[i] for i in range(*index)),
                            rna=self.rna)

    def __contains__(self, x: object) -> bool:
        if not isinstance(x,  (Sequence, str)):
            raise TypeError(f'Must be str or Sequence')
        if isinstance(x, str):
            return x in self.sequence
        return x.sequence in self.sequence

    def __repr__(self) -> str:
        return self.sequence

    def __str__(self) -> str:
        return self.sequence

    def __len__(self) -> int:
        return len(self.sequence)

    def index(self, other: object) -> int:
        if not isinstance(other, (str, Sequence)):
            raise ValueError
        if isinstance(other, Sequence):
            return self.sequence.index(other.sequence)
        return self.sequence.index(other)


    @property
    def nucleotide_counter(self) -> Counter:
        return Counter(self.sequence)

    
    def make_frames(self, 
                    start_codons: Iterable[str],
                    stop_codons: Iterable[str],
                    len_seq: int = 50) -> Optional[List[Sequence]]:
        seqs: List[str] = make_sequences(seq=self.sequence,
                                         start_codons=start_codons,
                                         stop_codons=stop_codons,
                                         len_seq=len_seq)
        if seqs:
            return [Sequence(seq, rna=self.rna) for seq in seqs]
        return []
    

    @property
    def protein(self) -> str:
        if not self._prot:
            if len(self.sequence) % 3:
                raise ValueError(f'Length of sequence must be divided by 3')
            self._prot = make_protein(self.sequence, rna=self.rna)
        return self._prot


    def transcription(self) -> str:
        if self.rna:
            return self.sequence.replace('U', 'T')
        return self.sequence.replace('T', 'U')


    def aminoacids(self) -> Counter:
        return Counter(self.protein)
        