import os
import requests
import tarfile
import re
import csv 
import shutil
from Bio import SeqIO 

# Change directory 
os.chdir('/Users/ryanstevens/Documents/github/py_string_matchers/data/seq_alignments/')
temp_folder = './temp'
os.mkdir(temp_folder)

# Pull Feb 2021 Data with sequence alignments from Homstrad website 
# Note: We will delete both the zipped and unzipped tar file 
r = requests.get('https://mizuguchilab.org/homstrad/data/homstrad_ali_only_2021_Feb_1.tar.gz',stream=True)
local_filename = 'temp.tar.gz'
with open(local_filename, 'wb') as f:
    for chunk in r.raw.stream(1024, decode_content=False):
        if chunk:
            f.write(chunk)

# Get all files with protein sequence alignments 
sequences_tarfile = tarfile.open(local_filename,'r:gz')
for member in sequences_tarfile.getmembers():
    if re.search('.ali$',member.name) is not None:
        member.name = os.path.basename(member.name)
        sequences_tarfile.extract(member, temp_folder)

# Create csv file where each row is pairs of protein sequences
with open('seq_alignment.csv','w') as outfile:
    writer = csv.writer(outfile)
    for file in os.listdir(temp_folder):
        records = list(SeqIO.parse(os.path.join(temp_folder,file),"pir"))
        for i in range(0,len(records)):
            for j in range(i,len(records)):
                unalign_prot_1 = records[i].seq.ungap()._data
                unalign_prot_2 = records[j].seq.ungap()._data
                align_prot_1 = records[i].seq._data
                align_prot_2 = records[j].seq._data
                writer.writerow([unalign_prot_1,unalign_prot_2,align_prot_1,align_prot_2])

# Delete tar file + temporary data
shutil.rmtree(temp_folder)
os.remove(local_filename)


