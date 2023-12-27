class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        look_up = defaultdict(int)
        nums1 = []
        nums2 = []
        for i in range(len(arr2)):
            look_up[arr2[i]] = i + 1
        for i in range(len(arr1)):
            if arr1[i] in look_up:
                nums1.append(arr1[i])
            else:
                nums2.append(arr1[i])
        for i in range(len(nums1) - 1):
            for j in range(len(nums1) - i - 1):
                if look_up[nums1[j]] > look_up[nums1[j + 1]]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
        for i in range(len(nums2) - 1):
            for j in range(len(nums2) - i - 1):
                if nums2[j] > nums2[j + 1]:
                    nums2[j], nums2[j + 1] = nums2[j + 1], nums2[j]
        return nums1 + nums2

        