"""Protein Translation exercise"""

CODON = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP',
}


def proteins(strand: str) -> list:
    """Translate RNA sequences into proteins.

    :param strand: RMA strand
    :return: list of amino acids
    """
    codons = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    protein = []
    for cur_codon in codons:
        if cur_codon not in CODON:
            raise ValueError("Invalid RNA strand - contain "
                             f"'{cur_codon}' that isn't at codons list.")
        if CODON[cur_codon] == 'STOP':
            break
        protein.append(CODON[cur_codon])

    return protein
