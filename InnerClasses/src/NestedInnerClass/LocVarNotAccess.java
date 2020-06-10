package NestedInnerClass;

class LocVarNotAccess {
    public void m1(){
        int x=30;
        class inner{
            public void m2(){
                System.out.println(x);
            }
        }
        inner i =new inner();
        i.m2();
    }
    public static void main(String[] args) {
        LocVarNotAccess l = new LocVarNotAccess();
        l.m1();
    }
}
