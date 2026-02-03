#  Median of Two Sorted Arrays (Python)

This project implements a Python solution to find the median of two sorted arrays.

The approach used is based on merging the two arrays first, then computing the median from the merged sorted array.  
The project is written in a clear and educational style, making it ideal for learning algorithm fundamentals.

---

## Features

- Accepts two sorted arrays from user input
- Merges both arrays into a single sorted array
- Calculates the median:
  - Middle element if total length is odd
  - Average of two middle elements if total length is even
- Prints:
  - The merged sorted array
  - The calculated median
- Includes:
  - Pseudo-code
  - Time & space complexity analysis

---

##  How It Works

Given two sorted arrays nums1 and nums2:

1. Merge both arrays while maintaining sorting order
2. Determine the total length of the merged array
3. If the length is:
   - Odd → median is the middle element
   - Even → median is the average of the two middle elements

---

## Example Run

Enter first sorted array (space separated): 1 3
Enter second sorted array (space separated): 2

Merged Sorted Array: [1, 2, 3]
Median: 2


Example with even length:

Enter first sorted array (space separated): 1 2
Enter second sorted array (space separated): 3 4

Merged Sorted Array: [1, 2, 3, 4]
Median: 2.5


---

##  Technologies Used

- Language: Python 3
- Concepts:
  - Arrays / Lists
  - Two-pointer technique
  - Conditional logic
  - Algorithm analysis

---

##  Pseudo-Code
FUNCTION merge_sorted_arrays(arr1, arr2)
i ← 0, j ← 0
merged ← empty list

WHILE i < length(arr1) AND j < length(arr2)
    IF arr1[i] < arr2[j]
        ADD arr1[i] TO merged
        i++
    ELSE
        ADD arr2[j] TO merged
        j++
ADD remaining elements

RETURN merged
FUNCTION find_median_sorted_arrays(nums1, nums2)
merged ← merge_sorted_arrays(nums1, nums2)
n ← length(merged)

IF n is odd
    RETURN merged[n // 2]
ELSE
    RETURN (merged[n // 2 - 1] + merged[n // 2]) / 2

---

## Complexity Analysis

Let:
- m = length of first array  
- n = length of second array  

- Time Complexity:
  - Merging arrays: O(m + n)
  - Finding median: O(1)
  - Total: O(m + n)

- Space Complexity:
  - Merged array storage: O(m + n)

---

##  Educational Use

This project is suitable for:
- Computer Science & Engineering students
- Practicing array manipulation
- Understanding median calculation
- Interview preparation (classic problem)

---

##  License

This project is open for educational and personal use.
