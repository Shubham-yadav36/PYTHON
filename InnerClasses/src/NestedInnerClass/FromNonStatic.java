package NestedInnerClass;

public class FromNonStatic {
        int x=10;
        static int y=20;
        public void m1(){
            class inner{
                public void m2(){
                    System.out.println(x);
                    System.out.println(y);
                }
            }
            inner i = new inner();
            i.m2();
        }

    public static void main(String[] args) {
        FromNonStatic s = new FromNonStatic();
        s.m1();
    }
}
