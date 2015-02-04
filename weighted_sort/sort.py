def sort(sequence, weights = None):
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
