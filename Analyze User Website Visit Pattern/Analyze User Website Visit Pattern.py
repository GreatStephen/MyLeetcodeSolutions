class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        packed_tuple = zip(timestamp, username, website)   # ---> [(3, 'joe', 'career'),....]
        sorted_packed_tuple = sorted(packed_tuple)  # sort by timestamp (By default tuple always sorted by first item )
        
        mapping = collections.defaultdict(list)
        for t, u, w in sorted_packed_tuple:     # joe: [home, about, career]  websites in list are in ascending timestamp order
            mapping[u].append(w)
        # print(mapping)
        
        counter_dict = defaultdict(int)         # use a dict for counting
        for website_list in mapping.values():
            combs = set(itertools.combinations(website_list, 3))    # size of combination is set to 3 
            for comb in combs:
                counter_dict[comb] += 1       # Tuple as key, counter as value,  e.g. ('home', 'about', 'career') : 2
        
        ans = sorted(counter_dict, key = lambda x: (-counter_dict[x],x))
        # print(ans)
        return ans[0]
    