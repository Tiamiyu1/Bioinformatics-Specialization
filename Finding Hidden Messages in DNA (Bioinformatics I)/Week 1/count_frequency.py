# Count Frequency
def pattern_count(text, pattern): # the text and pattern as parameters
    count = 0  # indexing from 0
    for i in range(len(text) - len(pattern)): # loop through the text length until pattern length 
        if text[i:i+len(pattern)] ==pattern: # slice 3 letters starting from 0 to 2, 1-3, 2-4 and so on...
            count += 1 # add 1 to count if any of the slices matches the pattern 
    return count # finally return the count value