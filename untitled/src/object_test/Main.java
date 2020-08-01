package object_test;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args){
        ArrayList<Integer> list = new ArrayList<Integer>(){{
            add(0);
        }};

        Main m = new Main();
        m.test_arraylist(list);

        int a=0;
        m.test_int(a);
        System.out.println(list);
        System.out.println(a);

    }

    public void test_arraylist(ArrayList<Integer> list){
        list.add(1);
    }

    public void test_int(int a){
        a++;
    }
}
