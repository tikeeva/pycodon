from .codon_dict import rna_codons, dna_codons


class Codon:

    def __init__(self, 
                 triplet: str, 
                 rna: bool = False) -> None:

        self.triplet: str = triplet
            
        if not rna:
            self.value: str = dna_codons[triplet]
        else:
            self.value: str = rna_codons[triplet]

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Codon):
            if self.value == o.value:
                return True
        return False
