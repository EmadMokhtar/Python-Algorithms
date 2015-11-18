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