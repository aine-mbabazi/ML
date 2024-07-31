import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) 

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)


max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(80)
max_heap.insert(90)
max_heap.insert(20)
max_heap.insert(5)
print(max_heap.extract_max())  
print(max_heap.peek())    

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) 

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
           
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)


min_heap = MinHeap()
min_heap.insert(108)
min_heap.insert(120)
min_heap.insert(3)
print(min_heap.extract_min()) 
print(min_heap.peek()) 



class ListNode:
   def __init__(self, value=0, next=None):
       self.value = value
       self.next = next


   def __lt__(self, other):
       return self.value < other.value


def merge_k_sorted_lists(lists):
   min_heap = []
   # Initialize the heap with the head of each list
   for l in lists:
       if l:
           heapq.heappush(min_heap, l)
  
   # Create a dummy node to help with result construction
   dummy = ListNode()
   current = dummy
  
   while min_heap:
       # Extract the smallest element
       node = heapq.heappop(min_heap)
       current.next = node
       current = current.next
       # If there are more elements in the same list, add the next element to the heap
       if node.next:
           heapq.heappush(min_heap, node.next)
  
   return dummy.next


# Helper function to print the linked list
def print_linked_list(node):
   while node:
       print(node.value, end=" -> ")
       node = node.next
   print("None")


# Example usage
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))


lists = [list1, list2, list3]
merged_list = merge_k_sorted_lists(lists)
print_linked_list(merged_list)

# Qn 1
# Given N sectors and two integers P and Q, our task is to find Q closest sectors to P sector.


def find_closest_sectors(sectors, p, q):
    # Create a max heap to store the closest sectors
    max_heap = []
    
    for sector in sectors:
        # Calculate the distance from the current  to P
        distance = abs(sector - p)
        
        # Push the negative distance and sector into the max heap
        # We use negative distance to simulate a max heap in Python's min heap implementation
        heapq.heappush(max_heap, (-distance, sector))
        
        # If the heap exceeds size Q, remove the farthest sector
        if len(max_heap) > q:
            heapq.heappop(max_heap)
    
    # Extract the sectors from the heap and sort them
    closest_sectors = [sector for _, sector in max_heap]
    
    return closest_sectors

# Example usage
sectors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = 4
q = 3

result = find_closest_sectors(sectors, p, q)
print(f"The {q} closest sectors to sector {p} are: {result}")

# Qn 2
# Given an array containing N integers, our task is to:Create min-heap with 1 based indexing.
# Remove the element present at index k from the heap created in the first step using Decrease key method.
class MinHeap:
    def __init__(self, array):
        # Initialize the heap with the given array
        self.heap = [0] + array  # Add a dummy value at index 0 for 1-based indexing
        self.size = len(array)
        self.build_heap()

    def build_heap(self):
        # Build the heap from the array
        for i in range(self.size // 2, 0, -1):
            self.heapify(i)

    def heapify(self, index):
        # Maintain the min-heap property
        smallest = index
        left = 2 * index
        right = 2 * index + 1

        if left <= self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right <= self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)

    def decrease_key(self, index, new_value):
        # Decrease the key at the given index
        if index < 1 or index > self.size:
            raise IndexError("Index out of bounds")
        self.heap[index] = new_value
        while index > 1 and self.heap[index // 2] > self.heap[index]:
            # Swap with parent
            self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index //= 2

    def remove_at_index(self, index):
        # Remove the element at the specified index using decrease key
        if index < 1 or index > self.size:
            raise IndexError(" out of bounds")
        # Decrease the key to a very small value
        self.decrease_key(index, float('-inf'))
        # Remove the minimum element (which is now at index 1)
        self.pop()

    def pop(self):
        # Remove and return the minimum element from the heap
        if self.size < 1:
            raise IndexError("Empty heap")
        min_element = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heapify(1)
        return min_element

    def __str__(self):
        return str(self.heap[1:self.size + 1])  # Return the heap without the dummy value

# Example usage
array = [3, 1, 6, 5, 2, 4]
min_heap = MinHeap(array)
print("Original Min-Heap:", min_heap)

k = 3  # Index to remove (1-based)
min_heap.remove_at_index(k)
print(f"Min-Heap after removing element at index {k}:", min_heap)

#Qn 3
# Given a string str, find first K non-repeating characters in lexicographical order, 
# if all the characters are repeating then print "Not Exist" without quotes.

from collections import Counter

def first_k_non_repeating_characters(s, k):
    # Count the frequency of each character
    char_count = Counter(s)
    
    # Create a min-heap for non-repeating characters
    min_heap = []
    
    # Filter non-repeating characters and add them to the heap
    for char, count in char_count.items():
        if count == 1:
            heapq.heappush(min_heap, char)
    
    # Extract the first K non-repeating characters from the heap
    result = []
    while min_heap and len(result) < k:
        result.append(heapq.heappop(min_heap))
    
    # Check if we have enough non-repeating characters
    if len(result) < k:
        print("Not Exist")
    else:
        print("".join(result))

# Example usage
input_string = "girlsforgirls"

k = 3
first_k_non_repeating_characters(input_string, k)

#Qn 4
# Given an array containing N integers, our task is to create a min-heap using the elements 
# of the given array and sort the array in descending order using heap sort



def heap_sort_descending(arr):
    # Step 1: Build a min-heap from the array
    heapq.heapify(arr)  
    
    # Step 2: Extract elements from the heap and store them in a sorted array
    sorted_array = []
    while arr:
        # Pop the smallest element from the heap
        smallest = heapq.heappop(arr)
        sorted_array.append(smallest)
    
    # Step 3: Reverse the sorted array to get it in descending order
    sorted_array.reverse()
    
    return sorted_array

# Example usage
input_array = [5, 3, 8, 4, 1, 2]
sorted_array = heap_sort_descending(input_array)
print("Sorted array in descending order:", sorted_array)

# Qn 5
# Given an array arr[] of N distinct elements and a number K, 
# where K is smaller than the size of the array. Find the K’th smallest element in the given array.



def kth_smallest_min_heap(arr, k):
    # Create a min-heap from the array
    min_heap = arr[:]
    heapq.heapify(min_heap)  # Transform the list into a heap in-place

    # Extract the smallest element k times
    for _ in range(k - 1):
        # Remove the smallest element
        heapq.heappop(min_heap)  

    # The K'th smallest element is now at the root of the heap
    return heapq.heappop(min_heap)

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
result = kth_smallest_min_heap(arr, k)
print(f"The {k}th smallest element is: {result}")
