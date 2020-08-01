import java.util.HashMap;
import java.util.Map;

class Solution {
    public String minWindow(String s, String t) {
        if (s.length() == 0 || t.length() == 0)
            return "";

        Map<Character, Integer> map = new HashMap();
        Map<Character, Integer> countmap = new HashMap();
        for (int i = 0; i < t.length(); i++) {
            if (!map.containsKey(t.charAt(i)))
                map.put(t.charAt(i), 1);
            else
                map.replace(t.charAt(i), map.get(t.charAt(i)) + 1);
        }
        int desired = map.size();

        int targetl = -1, targetr = s.length();
        int l = 0, r = 0;
        int uniquekey = 0;
        while (r <= s.length() - 1) {
            if (map.containsKey(s.charAt(r))) {
                if (!countmap.containsKey(s.charAt(r)))
                    countmap.put(s.charAt(r), 1);
                else
                    countmap.replace(s.charAt(r), countmap.get(s.charAt(r)) + 1);
                if (countmap.get(s.charAt(r)).intValue() == map.get(s.charAt(r)).intValue())
                    uniquekey++;
            }

            while (uniquekey == desired) {
                if (r - l + 1 < targetr - targetl + 1) {
                    targetl = l;
                    targetr = r;
                }
                if (countmap.containsKey(s.charAt(l))) {
                    countmap.replace(s.charAt(l), countmap.get(s.charAt(l)) - 1);
                    if (countmap.get(s.charAt(l)) < map.get(s.charAt(l)))
                        uniquekey--;
                }

                l++;
            }

            r++;
        }
        if (targetl == -1)
            return "";
        else
            return new String(s.substring(targetl, targetr + 1));
    }
}