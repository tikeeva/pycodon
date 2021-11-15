
# Sequence
class Sequence:

    def frame_poses(self, 
                    start_codons: Iterable[str],
                    stop_codons: Iterable[str],
                    len_seq: int = 50) -> Optional[List[Sequence]]:
        seqs: List[str] = make_sequences(seq=self.sequence,
                                         start_codons=start_codons,
                                         stop_codons=stop_codons,
                                         len_seq=len_seq)
        
        prot_frame_pos(self.sequence, start_codons=)


# utils
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
