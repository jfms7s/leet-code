class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        max_pos = size - 1
        current = 0
        for i in range(len(flowerbed)):

            if flowerbed[i] == 0 and (i==0 or flowerbed[i - 1] == 0) and (i == max_pos or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                current += 1


        return current >= n