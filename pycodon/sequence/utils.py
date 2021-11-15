from typing import Iterable, List, Set
from ..codon_dict import rna_codons, dna_codons
from itertools import product


# def make_sequences(seq: str, start_codons: Iterable[str], stop_codons: Iterable[str], len_seq: int) -> List[str]:
#     start: Set[str] = set(start_codons)
#     stop: Set[str] = set(stop_codons)
#     seqs = []
#     for i in range(len(seq)):
#         if seq[i: i+3] in start:
#             for j in range(i+3, len(seq), 3):
#                 if seq[j: j+3] in stop:
#                     if len(seq[i:j]) > len_seq:
#                         seqs.append(seq[i:j])
#                         break
#     return seqs


def make_sequences(seq: str, start_codons: Iterable[str], stop_codons: Iterable[str], len_seq:int):
    frame_poses = prot_frame_pos(seq, start_codons, stop_codons, len_seq)
    return [seq[start:stop] for start, stop in frame_poses]


def prot_frame_pos(seq: str, start_codons: Iterable[str], stop_codons: Iterable[str], len_seq:int):
    start = set(start_codons)
    stop = set(stop_codons)
    start_pos, stop_pos = [], []
    for i in range(len(seq)):
        if seq[i:(i + 3)] in start:
            start_pos.append(i)
        if seq[i:(i + 3)] in stop:
            stop_pos.append(i)
    # Checking if there is start or stop codons for correct protein generation
    if start_pos and stop_pos:
        frames_poses = [frame for frame in product(start_pos, stop_pos) if valid_frame(*frame, stop_pos, len_seq)]           
    else:
        frames_poses = []
    return frames_poses


def valid_frame(start: int, stop: int, stop_poses: List[int], len_seq:int):
    for i in stop_poses:
        if start < i < stop and (i - start) % 3 == 0:
            return False
    return stop - start > len_seq and (stop - start) % 3 == 0


def make_protein(sequence, rna) -> str:
        if rna:
            codons = rna_codons
        else:
            codons = dna_codons
        protein: str = ''
        for i in range(0, len(sequence), 3):
            triplet: str = sequence[i:i+3]
            protein += codons[triplet]
        return protein

def indexcheck(f):
    def inner(self, index, *args):
        if isinstance(index, int):
            if index < 0:
                index += len(self)
            if not (0 <= index < len(self)):
                raise IndexError('list index out of range')
        elif isinstance(index, slice):
            index = index.indices(len(self))
        else:
            raise TypeError('Not valid type of index')

        return f(self, index, *args)
    return inner