class Solution {
    public String addBinary(String a, String b) {
        String res = new String();

        int i = a.length() - 1, j = b.length() - 1;
        int carry = 0, tempvalue = 0;
        while (i >= 0 || j >= 0) {
            if (i < 0 && j >= 0) {
                tempvalue = ((b.charAt(j) - '0') + carry) % 2;
                carry = ((b.charAt(j) - '0') + carry) / 2;
                j--;
            } else if (i >= 0 && j < 0) {
                tempvalue = ((a.charAt(i) - '0') + carry) % 2;
                carry = ((a.charAt(i) - '0') + carry) / 2;
                i--;
            } else {
                tempvalue = ((a.charAt(i) - '0') + (b.charAt(j) - '0') + carry) % 2;
                carry = ((a.charAt(i) - '0') + (b.charAt(j) - '0') + carry) / 2;
                i--;
                j--;
            }

            res = String.valueOf(tempvalue) + res;

        }
        if (carry > 0)
            res = "1" + res;

        return res;
    }
}