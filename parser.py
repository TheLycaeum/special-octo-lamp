def total_weights(fname):
    total = 0
    with open(fname) as f:
        for i in f:
            _, weight = i.split(":")
            total += int(weight)
    return total
            
