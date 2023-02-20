import pytest
from classes import FASTQ_file
#from trombosis import *


fq_file = "RB26976_S16_L001_R2_001.fastq"
fq_file_error = "RB1gf13d3_R3.fastq"
Fq_class = FASTQ_file(fq_file)
Fq_class_er = FASTQ_file(fq_file_error)

def test_get_sample_number(get_sample_number):
    assert Fq_class.get_sample_number(fq_file) == "S16"
