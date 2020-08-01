/**
 * The read4 API is defined in the parent class Reader4. int read4(char[] buf);
 */

 // Error: Read4() will read a '\u0000' as the first char
 
public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return The number of actual characters read
     */
    static char[] buf4 = new char[4];
    static int index=0; // point to the unread chars
    static int unread=0; // number of unread chars in buf4

    public int read(char[] buf, int n) {
        
        int count=0;
        boolean eof=false;

        while(count<n){
            while(unread!=0){
                // System.out.println(buf4[index]);
                buf[count]=buf4[index];
                count++;
                index++;
                unread--;
                if(index>=4) index=0;
                if(count>=n) return count;
            }
            if(eof) return count;

            // read another 4 chars
            buf4[0]='';
            int readbytes = read4(buf4);
            unread=readbytes;
            System.out.println(buf4[0]);
            
            if(readbytes!=4){
                eof=true;
            }
            
        }

        return count;
    }
}