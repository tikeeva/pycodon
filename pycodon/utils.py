from typing import Dict, List, Tuple, Set
from itertools import product



def data_from_file(file: str) -> str:
    with open(file) as f:
        first_row: str = f.readline()
        if first_row.startswith('>'):
            first_row = f.readline()
    return first_row







def make_multisequence(levels: List[List[int]], content: Dict[int, str]) -> List[str]:
    paths: Tuple[Tuple[int, ...]] = tuple(product(*levels))
    multisequence: List[str] = []
    for i, path in enumerate(paths):
        multisequence.append('')
        for node in path:
            multisequence[i] += content[node]
    return multisequence




def make_frames(seq: str, start: Set[str]):
    start = {'ATG',}
    start_bacteria = {'ATG', 'TTG', 'CTG', 'GTG'}
    stop = {'TAA', 'TGA', 'TAG'}
    start_pos, stop_pos = [], []
    for i in range(len(seq)):
        if seq[i:(i + 3)] in start:
            start_pos.append(i)
        if seq[i:(i + 3)] in stop:
            stop_pos.append(i)

    # Checking if there is start or stop codons for correct protein generation
    if start_pos and stop_pos:
        frames = [frame for frame in product(start_pos, stop_pos) if valid_frame(*frame, stop_pos)]           
    else:
        return None
        
    return frames


def valid_frame(start, stop, stop_set):
    for i in stop_set:
        if start < i < stop and (i - start) % 3 == 0:
            return False
    return stop - start > 50 and (stop - start) % 3 == 0