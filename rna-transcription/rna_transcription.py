
def to_rna(dna):

    dna = dna.upper()

    if type(dna) != str:
        return

    dna_to_rna_map = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    rna = ''

    for nuc in dna:
        if nuc in dna_to_rna_map:
            rna += dna_to_rna_map[nuc]
        else:
            rna = ''
            break

    return rna
