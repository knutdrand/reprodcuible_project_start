"""Main module."""
def count_gc(seq):
    """Count the number of G's and C's in a sequence."""
    seq = seq.upper()
    return seq.count('G') + seq.count('C')
