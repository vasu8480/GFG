------------------------------     METHOD-1      ----------------------------------------------------
def reverseList(A, start, end):
	while start < end:
		A[start], A[end] = A[end], A[start]
		start += 1
		end -= 1
A = [1, 2, 3, 4, 5, 6]
reverseList(A, 0, 5)
print("Reversed list is" ,A)

------------------------------     METHOD-2      ----------------------------------------------------

A = [1, 2, 3, 4, 5, 6]
print( A[::-1])
