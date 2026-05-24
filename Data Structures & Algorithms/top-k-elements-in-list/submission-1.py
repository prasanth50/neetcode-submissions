class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hash_map = {}
        res = []
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        print(hash_map)
        sorted_dict = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        print(sorted_dict)

        for key,value in sorted_dict.items():
            if k > 0:
                res.append(key)
                k = k - 1
        return (res)


        