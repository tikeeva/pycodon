from pathlib import Path
from pycodon.metasequence import Metasequence
from pycodon.sequence import Sequence
from pycodon.utils import data_from_file

if __name__ == '__main__':

    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / 'data'
    filepath = str(DATA_DIR / 'Sequence1.txt')
    seq: str = data_from_file(file=filepath)

    # s = Sequence(sequence=seq)
    #print(s.nucleotide_counter)
    # print(s.codon_counter.get('G'))
    m = Sequence(seq)
    print(m)
    print('TACA' in m)

