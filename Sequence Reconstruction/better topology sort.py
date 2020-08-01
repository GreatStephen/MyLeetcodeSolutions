class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        adjacent = defaultdict(list)
        incoming_nodes = defaultdict(int)
        nodes = set()
        for arr in seqs:
            nodes |= set(arr)
            for i in range(len(arr)):
                if i == 0:
                    incoming_nodes[arr[i]] += 0
                if i < len(arr) - 1:
                    adjacent[arr[i]].append(arr[i + 1])
                    incoming_nodes[arr[i + 1]] += 1
        # cur是queue，存放indegree=0的点，新变成的点放进去
        # 效率远高于用list存放indegree
        cur = [k for k in incoming_nodes if incoming_nodes[k] == 0]
        res = []
        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)
            for node in adjacent[cur_node]:
                incoming_nodes[node] -= 1
                if incoming_nodes[node] == 0:
                    cur.append(node)
        if len(cur) > 1:
            return False
        return len(res) == len(nodes) and res == org