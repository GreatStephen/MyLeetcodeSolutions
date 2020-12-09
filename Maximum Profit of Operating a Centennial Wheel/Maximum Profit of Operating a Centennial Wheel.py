class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans, profit = -1, 0
        
        cus = customers[0]
        tempprofit, index = 0, 0
        while cus or index<len(customers):
            tempprofit += min(cus,4)*boardingCost - runningCost
            index += 1
            if tempprofit>profit:
                ans = index
                profit = tempprofit
            cus -= min(cus, 4)
            if index<len(customers):
                cus += customers[index]
        
        return ans