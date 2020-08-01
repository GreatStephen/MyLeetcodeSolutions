class Solution {
    public List<String> letterCombinations(String digits) {
        if(digits.length()==0) return new ArrayList<String>();
        List<String> list = new ArrayList<String>();
        Map<Character, String> map = new HashMap<>();
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");
        
        String s = map.get(digits.charAt(0));
        for(int i=0; i<s.length(); i++){
            list.add(s.substring(i,i+1));
        }
        list = nextNumber(map, list, digits.substring(1));
        return list;
        
    }
    
    public List<String> nextNumber(Map<Character, String> map, List<String> list, String digits)
    {
        if(digits.length()==0) return list;
        String s = map.get(digits.charAt(0));
        int listsize = list.size();
        for(int i=0; i<listsize; i++){
            String temp = list.get(0);
            list.remove(0);
            for(int j=0; j<s.length(); j++){
                list.add(temp+s.substring(j,j+1));
            }
        }
        
        list = nextNumber(map, list, digits.substring(1));
        return list;
    }
}