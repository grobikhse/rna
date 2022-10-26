def to_rna(dna_strand):
    return dna_strand.replace('A','U').replace('C','g').replace('G','c').replace('T','A').replace('g','G').replace('c','C')
