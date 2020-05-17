"""
find max  A[j] - A[i]; j>i
    (i,j)
"""

def solution(arr):
  if len(arr) < 2:
    return (-1,)
  
  n = len(arr)
  maxsofar = arr[-1]
  index_maxsofar = n-1 
  ans = -float('inf')

  iindex = None
  jindex = None

  # traverse array from right -> left
  for i in range(n-2, -1, -1):
    if maxsofar - arr[i] > ans:
      ans = maxsofar - arr[i]
      iindex = i
      jindex = index_maxsofar
    
    if arr[i] > maxsofar:
      maxsofar, index_maxsofar = arr[i], i
  return (iindex, jindex, ans)
  
