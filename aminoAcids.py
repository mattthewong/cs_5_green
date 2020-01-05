# support file for Computing for Biologists by Ran Libeskind-Hadas and Eliot Bush
from aminoAcids import *
aa = ['F','L','I','M','V','S','P','T','A','Y',
      '|','H','Q','N','K','D','E','C','W','R',
      'G']

codons = [['TTT', 'TTC'],
          ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
          ['ATT', 'ATC', 'ATA'],
          ['ATG'],
          ['GTT', 'GTC', 'GTA', 'GTG'],
          ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
          ['CCT', 'CCC', 'CCA', 'CCG'],
          ['ACT', 'ACC', 'ACA', 'ACG'],
          ['GCT', 'GCC', 'GCA', 'GCG'],
          ['TAT', 'TAC'],
          ['TAA', 'TAG', 'TGA'],
          ['CAT', 'CAC'],
          ['CAA', 'CAG'],
          ['AAT', 'AAC'],
          ['AAA', 'AAG'],
          ['GAT', 'GAC'],
          ['GAA', 'GAG'],
          ['TGT', 'TGC'],
          ['TGG'],
          ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
          ['GGT', 'GGC', 'GGA', 'GGG']]
def compBase(N):
    if N == 'A':
        N = 'T'
        return N
    
    elif N == 'T': 
        N = 'A'
        return N
    
    elif N == 'C':
        N = 'G'
        return N
    
    elif N == 'G':
        N = 'C'
        return N
    else: 
        if N != 'A' or N != 'T' or N != 'C' or N != 'G':
            N = 'error'
            return N
            
def reverse(s):
    storeletter = ""
    for i in s:
        storeletter = i + storeletter 
    return storeletter
          
              
