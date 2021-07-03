'''
Since in each row, there are 3 elements and if we take 2 rows at a time and find all possible sum as per the 
rules there could be 6 combinations.

So, we will iterate over all the N-1 rows, and for each row, we will find all the possible sums with respect to 
the row next to the current row.

To see it lets say we consider 2 rows R1 and R2 and each having 3 cols 0,1,2
then pairing will be as follows:

R1[0] -> R2[1], R1[0] -> R2[2]
R1[1] -> R2[0], R1[1] -> R2[2]
R1[2] -> R2[0], R1[2] -> R2[1]


from these 6 comibinations we need to choose 1 for each col of next row so total 3 combinations
so we shall create a temp array of 6 and update the sum values there.

If we see in reverse for above combn,
R2[0] will be paried with R1[1], R1[2]
R2[1] "     "    "      " R1[0], R1[2]
R2[2] "     "    "      " R1[0], R1[1]

Order of update will be 
tmp[0] -> notify for R2[0] and it's pair R1[1]
tmp[1] -> notify for R2[0] and it's pair R1[2]
tmp[2] -> notify for R2[1] and it's pair R1[0]
tmp[3] -> notify for R2[1] and it's pair R1[2]
tmp[4] -> notify for R2[2] and it's pair R1[0]
tmp[5] -> notify for R2[2] and it's pair R1[1]


we will update the row next to the current row i.e (i+1)th row with sums we calculated above 
such that each column has a minimum sum. 
This will be done:
ARR[i+1][0] = minimum(temp[0], temp[1])
ARR[i+1][1] = minimum(temp[2], temp[3])
ARR[i+1][2] = minimum(temp[4], temp[5])

You can visualize it in this way that if we have two rows and we have to find the minimum sum then 
there will be 6 combinations as mentioned above and in the 2nd row, each column will have two possible 
values of sums calculated above out of which we have to consider the minimum value for each column. 
Now if we find the minimum value in the whole 2nd row then that will be our required answer.

Similarly, if we perform the above operations on N-1 rows then finally the minimum value in the last row will be our required answer.
Now when we have iterate over all the N-1 rows then our final row will contain three possible sums as per the rules. So, we find the 
minimum  of all three values present in the last row and that will be our required answer.

'''
def minSum(arr):

    n = len(arr)
    tmp = [0] * 6

    # traverse th' n-1 rows
    for i in range(n-1):

        # find all 6 combinations
        tmp[0] = arr[i+1][0] + arr[i][1]
        tmp[1] = arr[i+1][0] + arr[i][2]
        tmp[2] = arr[i+1][1] + arr[i][0]
        tmp[3] = arr[i+1][1] + arr[i][2]
        tmp[4] = arr[i+1][2] + arr[i][0]
        tmp[5] = arr[i+1][2] + arr[i][1]

        # update i+1 th row
        arr[i+1][0] = min(tmp[0], tmp[1])
        arr[i+1][1] = min(tmp[2], tmp[3])
        arr[i+1][2] = min(tmp[4], tmp[5])

    # find min from last row
    ans = min(arr[-1])

    return ans

        