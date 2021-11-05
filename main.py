from pathlib import Path
from codon.metasequence import Metasequence
from codon.utils import data_from_file

if __name__ == '__main__':

    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / 'data'
    filepath = str(DATA_DIR / 'Sequence1.txt')
    seq: str = data_from_file(file=filepath)

    # s = Sequence(sequence=seq)
    #print(s.nucleotide_counter)
    # print(s.codon_counter.get('G'))
    m = Metasequence(seq)
    print(m.make_sequences())

