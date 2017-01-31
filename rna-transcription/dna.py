def to_rna(dna=''):
#for Python 3.1+
    return s.translate(str.maketrans("GCTA", "CGAU"))