Для проверки нужно скопировать код из соответствующей ячейки и вставить в файл [main.py](main.py)

1. Транскрипция. Sequence1 перевести код ДНК в код РНК:
```python
sequences = read_file('path/to/file').make_sequences()
sequence = sequences[0]
rna = sequence.transcription()
print(rna)
```
2. Трансляция. Sequence1 перевести в код белка:
```python
sequences = read_file('path/to/file').make_sequences()
sequence = sequences[0]
print(sequence.protein)
```

3. Посчитать встречаемость:

    а) каждой аминокислоты:
    ```python
    sequences = read_file('path/to/file').make_sequences()
    sequence = sequences[0]
    counts = sequence.nucleotide_counter
    freq = {k: v/len(sequence)) for k, v in counts.items()}
    print(freq)
    ```
    б) GС (почему GС -они дают три водородные связи и дают термоустойчивость ДНК, это важно для отжига праймеров для ПЦР):
    ```python
    print(freq['G'] + freq['C'])
    ```

4. Сравнить в двух белках по Sequence2 и Sequence3:

    а) GС-состав
    ```python
    # do same thing
    ```
    б) Встречаемость кодонов для глицина (G) и аланина (А)
    ```python
    freq['G'], freq['A']
    ```

5. В ДНК последовательностях Sequence1_1, Sequence1_2, Sequence1_3  обнаружить неоднозначные нуклеотиды и определить варианты изменения белкового кода и вывести результирющие белковые последовательности.
```python
s1 = read_from_file('path/to/file')
print(s1.ambiguous_nucleotides)

seqs = s1.make_sequences()
print(set(seq.protein for seq in seqs))
```

6. В последовательности Sequence4 найти старт и стоп кодоны, определить рамку считывания, количество аминокислот в белке и вывести последовательность белка.
```python
s4 = read_from_file('path/to/file')
seqs = s4.make_sequences()
start = ['ATG']
stop = ['TAA', 'TGA', 'TAG']
for seq in seqs:
    frames = seq.make_frames(start_codons=start, stop_codons=stop)
    for frame in frames:
        print(frame.aminoacids)
        print(frame.protein)
```

7. В модифицированном геноме вируса гриппа человека (sequence 6) по «смысловой» цепочке ДНК:
    1. найти неоднозначности прочтений нуклеотидов и определить их положение
    ```python
    s6 = read_file('path/to/file')
    ```
    2. Определить сколько белков закодировано в последовательности
    ```python

    ```
    3. Вывести варианты последовательностей закодированных белков с указанием положения в геноме (начало старт кодона и конец рамки считывания, т.е. исключая стопкодон). 
    ```python

    ```
8. Сделать то же по «антисмысловой» цепочке ДНК
```python

```
9. Картировать геном бактериофага Sequence 7(см. 1 и 2)
```python

```
10. Картировать геном бактерии Sequence 8 (см. 1 и 2)Start codons in bacteria : ATG, TTG, CTG, GTG
```python
start_bacteria = {'ATG', 'TTG', 'CTG', 'GTG'}
```