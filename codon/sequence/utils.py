from typing import Iterable, List, Set
from ..codon_dict import rna_codons, dna_codons

def make_sequences(seq: str, start_codons: Iterable[str], stop_codons: Iterable[str]) -> List[str]:
    start: Set[str] = set(start_codons)
    stop: Set[str] = set(stop_codons)
    seqs = []
    for i in range(len(seq)):
        if seq[i: i+3] in start:
            for j in range(i+3, len(seq), 3):
                if seq[j: j+3] in stop:
                    seqs.append(seq[i: j])
    return seqs

def make_protein(self, sequence, rna) -> str:
        if rna:
            codons = rna_codons
        else:
            codons = dna_codons
        protein: str = ''
        for i in range(0, len(sequence), 3):
            triplet: str = sequence[i:i+3]
            amino_acid: str = codons[triplet]
            protein += amino_acid
        return protein
