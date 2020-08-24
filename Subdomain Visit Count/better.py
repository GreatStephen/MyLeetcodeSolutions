class Solution(object):
    def subdomainVisits(self, cpdomains):
        ct = collections.Counter()
        for cp in cpdomains:
            n,s = cp.split(' ')
            ct[s] += int(n)
            for i,c in enumerate(cp):
                if c=='.':
                    ct[cp[i+1:]] += int(n)
        ans = ['%d %s' % (ct[s],s) for s in ct]
        return ans