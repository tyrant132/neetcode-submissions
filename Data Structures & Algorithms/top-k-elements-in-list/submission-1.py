from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []
        pq = PriorityQueue()
        for num, freq in count.items():
            pq.put((freq, num))
            if pq.qsize()>k:
                pq.get()
        for i in range(k):
            freq, num = pq.get()
            ans.append(num)
        return ans