class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort the products, and Binary Search the bisect_left the prefix
        products.sort()
        # print(products)
        res, idx = [], 0
        for i in range(1,len(searchWord)+1):
            p = searchWord[:i]
            idx = bisect.bisect_left(products, p, lo=idx)
            res.append([w for w in products[idx:idx+3] if w.startswith(p)])
        return res