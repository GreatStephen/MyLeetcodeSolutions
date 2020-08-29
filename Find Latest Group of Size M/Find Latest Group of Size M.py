class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # 特别巧妙的方法。准备一个长度为len(arr)+2的list，代表每个位置所在的1的宽度。第一个和最后一个永远为0，等于控制两个边界
        # 但是，只有连续1的最左和最右两个元素是实时表示长度的。中间的数字不予更新
        # 对每个置1的pos，检查它左右两侧的group长度。注意，pos-1和pos+1都是左右两个group的边界，所以代表了实时长度。
        # 然后left+right+1等于左右合并之后的group长度。仍然更新边界pos-left和pos+right。
        # 这个题就是通过左右边界来合并group
        if m==len(arr):
            return len(arr)
        length = [0]*(len(arr)+2)
        ans = -1
        for i,pos in enumerate(arr):
            left, right = length[pos-1], length[pos+1]
            length[pos] = length[pos-left] = length[pos+right] = left+right+1
            if left==m or right==m:
                ans = i
        return ans