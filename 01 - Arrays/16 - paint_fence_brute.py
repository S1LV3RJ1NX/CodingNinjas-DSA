# Brute Force approach to paint the fence

def paintTheFence(ranges, n, q):
    
    """
    First we create a section array which will denote 
    number of painters that will paint a given section.
    Then we iterate over all possible pairs of painters
    and remove the sections painted by them. Finally,
    consider the max count retured by a particular pair.
    """

    # considering ranges from 1 based indexing
    section = [0] * (n+2) 

    for rng in ranges:
        left, right = rng 
        # right range must also be considered
        for j in range(left, right+1):
            section[j] += 1

    # print(section)

    # Consider every possible pair and remove them
    max_painted = -float('inf')
    painted = None

    # Considering first pair
    for i in range(q):
        left, right = ranges[i][0], ranges[i][1]

        # copy section array to painted array
        painted = section[:] 

        # remove i-th painter
        for k in range(left, right+1):
            painted[k] -= 1

        # Considering second pair 
        for j in range(i+1, q):
            
            left_second, right_second = ranges[j][0], ranges[j][1]

            # remove j-th painter
            for k in range(left_second, right_second+1):
                painted[k] -= 1

            # count painted sections
            paint_count = 0

            for paint in painted:
                if paint > 0:
                    paint_count += 1

            max_painted = max(max_painted, paint_count)
    
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