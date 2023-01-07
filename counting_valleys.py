def countingValleys(steps, path):
    count = 0
    num_valleys = 0
    
    for i in range(steps):
        if path[i] == 'D':
            count-=1
        else:
            count+=1
            if count == 0:
                num_valleys+=1
    return num_valleys
