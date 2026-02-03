def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    # دمج المصفوفتين بطريقة مرتبة
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # إضافة الباقي من arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # إضافة الباقي من arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


def find_median_sorted_arrays(nums1, nums2):
    merged = merge_sorted_arrays(nums1, nums2)
    n = len(merged)

    print(f"\nMerged Sorted Array: {merged}")

    # حساب الوسيط
    if n % 2 == 1:
        median = merged[n // 2]
    else:
        mid1 = merged[n // 2 - 1]
        mid2 = merged[n // 2]
        median = (mid1 + mid2) / 2

    print(f"Median: {median}")
    return median


# ===================== التشغيل =====================
nums1 = [int(x) for x in input("Enter first sorted array (space separated): ").split()]
nums2 = [int(x) for x in input("Enter second sorted array (space separated): ").split()]

find_median_sorted_arrays(nums1, nums2)


# ==========================================================
#                   PSEUDO-CODE
# ==========================================================
'''
FUNCTION merge_sorted_arrays(arr1, arr2)
{
    merged := []
    i := 0
    j := 0

    WHILE i < length(arr1) AND j < length(arr2) DO
        IF arr1[i] < arr2[j] THEN
            APPEND arr1[i] TO merged
            i := i + 1
        ELSE
            APPEND arr2[j] TO merged
            j := j + 1
        END IF
    END WHILE

    WHILE i < length(arr1) DO
        APPEND arr1[i] TO merged
        i := i + 1
    END WHILE

    WHILE j < length(arr2) DO
        APPEND arr2[j] TO merged
        j := j + 1
    END WHILE

    RETURN merged
}

FUNCTION find_median_sorted_arrays(nums1, nums2)
{
    merged := merge_sorted_arrays(nums1, nums2)
    n := length(merged)

    IF n IS ODD THEN
        median := merged[n // 2]
    ELSE
        median := (merged[n // 2 - 1] + merged[n // 2]) / 2
    END IF

    RETURN median
}
'''


# ==========================================================
#             TIME COMPLEXITY ANALYSIS
# ==========================================================
'''
Let:
m = length(nums1)
n = length(nums2)

- Merging two sorted arrays: O(m + n)
- Finding median: O(1)
=> Total Time Complexity: O(m + n)
=> Space Complexity: O(m + n)
'''
