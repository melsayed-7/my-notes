#!/usr/bin/python3


def dna_complement(s):
    dict_comp = {"A": "T", "T": "A", "G": "C", "C": "G"}
    comp = "".join(dict_comp[k] for k in reversed(s))
    return comp


print(dna_complement("AAAACCCGGT"))
