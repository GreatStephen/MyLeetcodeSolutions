class Solution {
    public String multiply(String num1, String num2) {
        int length1 = num1.length();
        int length2 = num2.length();

        int offset = 0;
        int carry = 0, tempvalue = 0;
        int i, j;
        String value = new String();
        for (j = length2 - 1; j >= 0; j--) {
            carry = 0;
            String num = new String();
            for (i = length1 - 1; i >= 0; i--) {
                tempvalue = (((num2.charAt(j) - '0') * (num1.charAt(i) - '0') + carry) % 10);
                String tempnum = String.valueOf(tempvalue);
                num = tempnum + num;
                carry = ((num2.charAt(j) - '0') * (num1.charAt(i) - '0') + carry) / 10;

            }
            if (carry > 0)
                num = String.valueOf(carry) + num;
            for (int m = 0; m < offset; m++)
                num += "0";
            offset++;
            // System.out.println("value="+value);
            // System.out.println("num="+num);
            value = plus(value, num);

        }

        // System.out.println(value);
        // delete all the leading '0's
        while (value.charAt(0) == '0') {
            if (value.length() > 1)
                value = value.substring(1);
            else
                break;
        }
        return value;
    }

    public String plus(String value, String num) {
        String res = new String();
        if (value.length() == 0)
            return num;
        else {
            int i = value.length() - 1, j = num.length() - 1;
            int carry = 0, tempvalue = 0;
            while (i >= 0 || j >= 0) {
                if (i < 0 && j >= 0) {
                    tempvalue = ((num.charAt(j) - '0') + carry) % 10;
                    carry = ((num.charAt(j) - '0') + carry) / 10;
                    j--;
                } else if (i >= 0 && j < 0) {
                    tempvalue = ((value.charAt(i) - '0') + carry) % 10;
                    carry = ((value.charAt(i) - '0') + carry) / 10;
                    i--;
                } else {
                    tempvalue = ((value.charAt(i) - '0') + (num.charAt(j) - '0') + carry) % 10;
                    carry = ((value.charAt(i) - '0') + (num.charAt(j) - '0') + carry) / 10;
                    i--;
                    j--;
                }

                res = String.valueOf(tempvalue) + res;

            }
            if (carry > 0)
                res = String.valueOf(carry) + res;
        }
        return res;
    }
}