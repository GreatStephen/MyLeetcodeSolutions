/**
 * The read4 API is defined in the parent class Reader4. int read4(char[] buf);
 */
public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return The number of actual characters read
     */
    public int read(char[] buf, int n) {

        int count = 0;
        boolean eof = false;
        char[] buf4 = new char[4];

        while (count < n && !eof) {
            int readbytes = read4(buf4);
            if (readbytes != 4) {
                eof = true;
            }
            int length = Math.min(n - count, readbytes);
            for (int i = 0; i < length; i++) {
                buf[count + i] = buf4[i];
            }
            count += length;
        }

        return count;
    }
}