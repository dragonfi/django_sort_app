def sort(sequence, weights = None):
    """Sorts a sequence of dictionaries, normalized and weighted by weight.

    To get the correct sorting order, first normalize each attribute
    (so that the lowest and highest values from each attribute count the same)
    then do a weighted sum of them as usual.

    This ensures that each attribute will have roughly the same contribution,
    regardless of the choice of base unit.

    Example:

        Weights:
            foo: 1
            bar: 2
            baz: -5

        Objects:
             id:    1      2       3
            foo:   11    101       1
            bar:   -3      5      13
            baz:  0.2   10.2     3.2

        After normalization:
             id:    1      2       3
            foo:  0.1    1.0     0.0
            bar:  0.0    0.5     1.0
            baz:  0.0    1.0     0.3

        Weighted sum (applying 1, 2, -5):
             id:    1      2       3
           wsum:  0.1   -3.0     0.5

        Final order: 2, 1, 3
    """
    if len(sequence) == 0:
        return sequence
    if weights is None:
        return sorted(sequence)
    return sorted(sequence, key=get_weight_function(sequence, weights))

def get_weight_function(sequence, weights):
    normalize = {}
    for attr in weights:
        seq = list(map(lambda x: x[attr], sequence))
        normalize[attr] = get_normalize_function(seq)

    def weight_function(elem):
        total = 0
        for attr, weight in weights.items():
            total += normalize[attr](elem[attr]) * weight
        return total
    return weight_function

def get_normalize_function(sequence):
    smallest = min(sequence)
    largest = max(sequence)
    offset = smallest
    length = largest - smallest
    def normalize(number):
        return (number - offset) / length
    return normalize
