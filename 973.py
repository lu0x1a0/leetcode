
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapSort(points,k)
    
def heapSort(arr,k):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # One by one extract elements
    for i in range(n-1, n-k, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        #print(arr)
    return arr[-k:]
def heapify(arr, n, i):
    smallest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and euclid(*arr[smallest]) < euclid(*arr[l]):
        smallest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and euclid(*arr[smallest]) < euclid(*arr[r]):
        smallest = r

    # Change root, if needed
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, smallest)    
def euclid(x,y):
    return x**2+y**2