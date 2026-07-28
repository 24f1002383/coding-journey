def to_rna(dna_strand):
    transcription = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    
    rna = ""
    for x in dna_strand:
        rna += transcription[x]
    return rna