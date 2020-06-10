package NestedInnerClass;

public class LocalVariableAccess {
    public void m1(){
        final int x=20;
        class inner{
            public void m2(){
                System.out.println(x);
            }
        }
        inner i = new inner();
        i.m2();
    }

    public static void main(String[] args) {
        LocalVariableAccess l = new LocalVariableAccess();
        l.m1();
    }
}
