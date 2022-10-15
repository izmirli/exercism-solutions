"""DNA to RNA transcription."""
DNA2RNA = str.maketrans('GCTA', 'CGAU')


def to_rna(dna_strand: str) -> str:
    """Return its RNA complement to given DNA.

    :param dna_strand: the DNA strand to make RNA for
    :return: the transcribed RNA strand
    """
    return dna_strand.translate(DNA2RNA)
