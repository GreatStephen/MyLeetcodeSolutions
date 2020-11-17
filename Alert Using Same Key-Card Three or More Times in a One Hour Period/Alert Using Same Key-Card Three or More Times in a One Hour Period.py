class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def minutes(time):
            hour, minute = time.split(':')
            return int(hour)*60+int(minute)


        d = {}
        names = set()
        for i in range(len(keyName)):
            if keyName[i] not in d:
                d[keyName[i]] = []
            d[keyName[i]].append(minutes(keyTime[i]))
        for name in d.keys():
            times = sorted(d[name])
            for i in range(len(times)-2):
                if times[i+2]-times[i]<=60:
                    names.add(name)

        # print(names)
        return sorted(list(names))