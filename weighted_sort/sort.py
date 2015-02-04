def sort(sequence, weights = None):
    if weights is None:
        return sorted(sequence)
    return sorted(sequence, key=get_weight_function(sequence, weights))

def get_weight_function(sequence, weights):
    def weight_function(elem):
        total = 0
        for attr, weight in weights.items():
            total += elem[attr] * weight
        return total
    return weight_function
