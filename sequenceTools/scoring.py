def matchQuality(seq1, seq2):
    '''
    Inputs: seq1 and seq2 are strings describing matched genome reads
    Return: score describing the quality of the match, based on:
    
    +1 for every matching pair of characters
    -1 for every mismatch
    +0 anytime there is a gap, represented by -
    '''
    
    score = 0
    
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            score = score +1
        elif seq1[i] == '-' or seq2[i] == '-':
            score = score
        else:
            score = score -1
            
    return score
