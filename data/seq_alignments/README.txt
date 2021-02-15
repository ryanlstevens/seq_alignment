Sequence alignment data `seq_alignment.csv` contains pairs of homologous protein sequences 
pulled from [HOMSTRAD](https://mizuguchilab.org/homstrad/Doc/Info.html#begin).
We use the data dump from [Feb 1, 2021](https://mizuguchilab.org/homstrad/data/homstrad_ali_only_2021_Feb_1.tar.gz).
The data was constructed using BioPython, the script 
to recreate this file is available in this folder
as `create_seq_alignment.py`. 

The data is in csv format, where each row is a homolgous protein sequence pair. 
The first two columns are the unaligned protein sequences, 
and the next two columns are the aligned sequences where '_' 
represents a "gap". 
   
Thus, the way to use this data is to align the first two columns, 
 and compare the alignment to the second two columns.

