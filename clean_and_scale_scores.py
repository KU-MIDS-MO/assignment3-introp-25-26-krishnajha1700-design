
    
import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
   
    # Step 1: Clip values to the range [min_score, max_score]
    clipped = np.clip(scores, min_score, max_score)

    # Step 2: Scale linearly to [0, 1]
    scaled = (clipped - min_score) / (max_score - min_score)

    return scaled.astype(float)
