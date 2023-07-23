def find_maximum_sum_subarray(A, B, C):
    left = 0
    max_sum = 0
    current_sum = 0

    for right in range(len(C)):
        current_sum += C[right]

        while current_sum > B:
            current_sum -= C[left]
            left += 1

        max_sum = max(max_sum, current_sum)

    return max_sum

A=int(input())
B=int(input())
C=list(map(int, input().split()))
print(find_maximum_sum_subarray(A,B,C))