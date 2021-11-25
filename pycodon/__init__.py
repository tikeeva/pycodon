'''pycodon'''

__version__ = '0.1.1'
import os

from .metasequence import Metasequence
from .utils import data_from_file

def read_file(filepath: str):
    if not os.path.isfile(filepath):
        raise ValueError(f'Path to file {filepath} is invalid')
    data: str = data_from_file(filepath)
    return Metasequence(data)
