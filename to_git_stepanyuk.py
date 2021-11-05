# То что у нее называлось rna_codons это на самом деле антикодоны поэтому так переименовал тот словарь.

rna_anticodons = {"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "UGU":"C", "UGC":"C",
    "GAU":"D", "GAC":"D",
    "GAA":"E", "GAG":"E",
    "UUU":"F", "UUC":"F",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
    "CAU":"H", "CAC":"H",
    "AUA":"I", "AUU":"I", "AUC":"I",
    "AAA":"K", "AAG":"K",
    "UUA":"L", "UUG":"L", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "AUG":"M", "AAU":"N", "AAC":"N",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "AGU":"S", "AGC":"S",
    "ACU":"U", "ACC":"U", "ACA":"U", "ACG":"U",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "UGG":"W",
    "UAU":"Y", "UAC":"Y",
    "UAA":"_", "UAG":"_", "UGA":"_"}


def f_dna_to_irna(seq_dna):
    dna_to_rna = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    seq_irna = str()
    for n in seq_dna:
        seq_irna += dna_to_rna[n]
    print(seq_irna)
    return seq_irna


def f_irna_to_mrna(seq_irna):
    irna_to_mrna = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    seq_mrna = str()
    for n in seq_irna:
        seq_mrna += irna_to_mrna[n]
    print(seq_mrna)
    return seq_mrna


def f_mrna_to_protein(seq_mrna):
    seq_protein = str()
    for letter_index in range(len(seq_mrna)):
        if letter_index % 3 == 0:
            codon = seq_mrna[letter_index:letter_index+3]
            seq_protein += rna_anticodons[codon]
    return seq_protein