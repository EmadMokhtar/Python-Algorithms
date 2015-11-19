##TODO: check the functions name
##TODO: find optimization the 2nd merge
def CopyMergeSort(A):
    """
    Merge sort list A and return sorted list
    This algorithm has an issue with storage
    """
    if len(A) < 2:
        return A

    mid = len(A)/2
    left = CopyMergeSort(A[:mid])
    right = CopyMergeSort(A[mid:])

    i = j = 0

    B= []

    while len(B) < len(A):
        if j >= len(right) or (i < mid and left[i] < right[j]):
            B.append(left[i])
            i+=1
        elif j < len(right):
            B.append(right[j])
            j+=1


    return B


def MergeSort(A):
    """
    Merge sort A in place
    """
    copy = list(A)

    mergesort_array(copy, A, 0, len(A))

def mergesort_array(A, result, start, end):
    """
    Mergesort array in memory with given range
    """
    #Sorting
    if end - start < 2:
        return

    if end - start == 2:
        if result[start] > result[end-1]:
            result[start], result[end-1] = result[end-1], result[start]
            return

    mid = (end + start) / 2
    mergesort_array(result, A, start, mid)
    mergesort_array(result, A, mid, end)

    # Merging
    i = index = start
    j = mid

    while index < end:
        if  j >= end or ( i < mid and A[i] < A[j]):
            result[index] = A[i]
            i += 1
        else:
            result[index] = A[j]
            j += 1
        index += 1