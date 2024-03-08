#!/usr/bin/env python

print("I am from GitHub")

def reverse_complement(sequence):
    """Reverse complement a DNA sequence"""
    revcomp = "" 
    complement_bases = {"A":"T", "C":"G", "G":"C", "T":"A"}
    for nt in sequence[::-1]:
        revcomp += complement_bases[nt]
    return revcomp
