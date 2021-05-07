def paintTheFence(ranges, n, q):

    """
    We first calculate all the sections that are painted by all the painters given
    and store them in sections array. This time we use the method of constant range
    addtion using prefix sums. 
    
    More info here: https://www.youtube.com/watch?v=-SDHYqxI-Hc

    This method requires array of size n+1 when index begins from 0, and already we 
    have been indices starting from 1 so overall we shall need an array of n+2 size 
    """
    section = [0] * (n + 2)

    # Constant range addition 
    for i in range(q):
        section[ranges[i][0]] += 1
        # adding -1 to next idx to nullify the effect of addition
        section[ranges[i][1]+1] -= 1

    # prefix sum
    for i in range(1, n + 1):
        section[i] += section[i-1]

    # print(section)

    """Now we shall create two arrays single painter and double painter where,
    each idx of single painter array represents the number of sections from starting 
    till the i-th section that could be painted by only one painter. Similarly double
    painter, each idx represents the number of sections from starting till the i-th 
    section that could be painted by only two painters."""

    singlePainter = [0] * (n + 1)
    doublePainter = [0] * (n + 1)

    # let us consider at first all sections could be painted
    total = n 
    for i in range(1, n+1):

        # A section found which could not be painted reduce it from total
        if section[i] == 0:
            total -= 1

        elif section[i] == 1:
            singlePainter[i] += 1
        
        elif section[i] == 2:
            doublePainter[i] += 1

        # prefix sum / cummulative sum
        singlePainter[i] += singlePainter[i-1]
        doublePainter[i] += doublePainter[i-1]

    max_painted = 0

    # consider a pair of painters try removing them and see how many 
    # painted sections remain, get max from out of all

    for i in range(q):
        for j in range(i+1, q):

            curr_painted_sections = total # make a copy

            # first remove the sections painted by painter i

            # prefix method to get the value
            left_idx_i = ranges[i][0]-1
            right_idx_i = ranges[i][1]

            sections_painted_by_painter_i =  singlePainter[right_idx_i] - singlePainter[left_idx_i]
            curr_painted_sections = curr_painted_sections - sections_painted_by_painter_i

            #  now remove sections painted by painter j
            # prefix method to get the value
            left_idx_j = ranges[j][0]-1
            right_idx_j = ranges[j][1]

            sections_painted_by_painter_j =  singlePainter[right_idx_j] - singlePainter[left_idx_j]
            curr_painted_sections = curr_painted_sections - sections_painted_by_painter_j

            # while removing the sections, it is possible that there might be common sections
            # which overlap in painter i,j. So these sections are subtracted twice, hence we 
            # need to find out common section between the two and add it again
            left_common = max(left_idx_i+1, left_idx_j+1)
            right_common = min(right_idx_i, right_idx_j)

            # common section available
            if right_common >= left_common:
                # add once the common section
                curr_painted_sections += singlePainter[right_common] - singlePainter[left_common-1]

                #  since we are removing the two painters we must also remove it from 
                # double painted section
                curr_painted_sections -= doublePainter[right_common] - doublePainter[left_common-1]

            max_painted = max(max_painted, curr_painted_sections)

    return max_painted

    




# TAKING INPUT

# length of fence and no of painters
N, Q = map(int, input().split())
painting_ranges = []

for i in range(Q):
    rng = [int(x) for x in input().split()]
    painting_ranges.append(rng)

ans = paintTheFence(painting_ranges, N, Q)
print(ans)