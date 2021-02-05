class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for ball in range(lowLimit, highLimit+1):
            n = ball
            num = 0
            while n:
                num += n%10
                n //= 10
            # print(num)
            if num not in boxes:
                boxes[num] = 0
            boxes[num] += 1
        # print(boxes)
        return max(boxes.values())