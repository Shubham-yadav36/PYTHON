package NestedInnerClass;

public class FromStatic {
    int x=10;
    static int y=20;
    public static void m1(){
        class inner{
            public void m2(){
//                System.out.println(x);
                System.out.println(y);
            }
        }
        inner i = new inner();
        i.m2();
    }

    public static void main(String[] args) {
        FromStatic s = new FromStatic();
        s.m1();
    }
}
