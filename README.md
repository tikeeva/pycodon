# pycodon 0.1.1
Проект группы студентов КФУ лаборатории Хемоинформатика и молекулярное моделирование.

Проект дает возможность проводить операции с последовательностями ДНК и РНК in pythonic way. 
## Установка
Для установки запустите следующую команду 
```bash
pip install pycodon
```
## Описание проекта

Пока разработано два класса: `Sequence` и `Metasequence`.


**Metasequence** - класс, экземпляр которого содержит в себе все последовательности нуклеотидов с учетом их неоднозначности, причем в графовом виде. Экземпляр Metasequence подходит как для ДНК, так и для РНК.

*Методы Metasequence*

1. Создание всех возможных последовательностей посредством обработки неоднозначных нуклеотидов:
```python
metaseq.make_sequences()
```

2. Поиск позиций неоднозначных нуклетидов
```python
metaseq.ambiguous_nucleotides()
```

3. Расчет длины последовательности:
```python
metaseq.count_nucleotides()
```

**Sequence** - класс, экземпляр которого является строко-подобным, содержит в себе строго одну последовательность нуклеотидов, исключая неоднозначности, что позволяет расширить функционал строк с учетом необходимости проведения различных модернизаций: транскрипций, трансляций, расчета рамок считывания и т.д. 

*Методы Sequence*

1. Транскрипция последовательности, как из ДНК в РНК, так и наоброт:
```python
seq.transcription()
```

2. Расчет количества каждого нуклеотида в последовательности:
```python
seq.nucleotide_counter
```


3. Поиск рамки считывания ДНК последовательности:
```python
seq.make_frames()
```
4. Трансляция последовательности в белок:
```python
seq.protein
```

5. Длина белковой последовательности:
```python
seq.aminoacids()
```
Для чтения файлов используйте функцию
```python
from pycodon import read_file

read_file('path/to/file')
```