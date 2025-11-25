import numpy as np

def count_values_in_bins(data, bin_edges):
    
    # Use numpy.histogram with right-inclusive last bin
    counts, _ = np.histogram(data, bins=bin_edges)
    
    # Adjust last bin to be inclusive on the right
    last_bin_mask = (data == bin_edges[-1])
    counts[-1] += np.sum(last_bin_mask)
    
    return counts
