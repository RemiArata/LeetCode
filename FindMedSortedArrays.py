
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        self.merged = []
        self.merge(nums1, nums2)
        idx = len(self.merged) // 2
        if len(self.merged) % 2 == 0:
            return (self.merged[idx] + self.merged[idx - 1]) / 2
        else:
            return self.merged[idx]

    def merge(self, nums1, nums2):
        i, j = 0, 0

        for _ in range(len(nums1) + len(nums2)):
            if i == len(nums1):
                break
            if j == len(nums2):
                break

            if nums1[i] <= nums2[j]:
                self.merged.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                self.merged.append(nums2[j])
                j += 1
        
        if i == (len(nums1)):
            self.merged.extend(nums2[j: len(nums2)])
        else:
            self.merged.extend(nums1[i: len(nums1)])

