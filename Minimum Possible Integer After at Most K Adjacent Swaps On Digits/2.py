class Solution:
    def minInteger(self, num: str, k: int) -> str:
        map = collections.defaultdict(list)
        for i,c in enumerate(num):
            map[c].append(i)
        
        idx, pick_idx= 0, []
        for idx in range(len(num)):
            for target in range(10):
                if target<=int(num[idx]) and map[str(target)]:
                    insert_pos = bisect.bisect_right(pick_idx, map[str(target)][0])
                    num_on_the_right = len(pick_idx)-insert_pos
                    move_length = map[str(target)][0]+num_on_the_right-idx
                    if move_length>=0 and move_length<=k:
                        k-=move_length
                        target_pos = map[str(target)][0]
                        pick_idx.insert(insert_pos, target_pos)
                        target_pos+=num_on_the_right                        
                        num = num[0:idx]+num[target_pos]+num[idx:target_pos]+num[target_pos+1:]
                        map[str(target)].pop(0)
                        if len(map[str(target)])==0: del map[str(target)]          
                        break    
                                        
            if k==0: break  # no jumps left
        return num