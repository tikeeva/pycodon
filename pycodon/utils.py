def data_from_file(file: str) -> str:
    with open(file) as f:
        first_row: str = f.readline()
        if first_row.startswith('>'):
            first_row = f.readline()
        next_row: str = f.readline()
        while next_row:
            first_row += next_row
            next_row = f.readline()
    return first_row.replace('\n', '').replace(' ', '')
