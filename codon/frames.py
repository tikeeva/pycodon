from itertools import product


def prot_frame(seq: str):
    start = {'ATG',}
    start_bacteria = {'ATG', 'TTG', 'CTG', 'GTG'}
    stop = {'TAA', 'TGA', 'TAG'}
    start_pos, stop_pos = [], []
    for i in range(len(seq)):
        if seq[i:(i + 3)] in start:
            start_pos.append(i)
        if seq[i:(i + 3)] in stop:
            stop_pos.append(i)
    print(start_pos, stop_pos)

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
