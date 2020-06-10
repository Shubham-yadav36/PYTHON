package NestedInnerClass;

public class Ex {
    public static void main(String[] args) {
        NClass n = new NClass();
        n.m2();
    }
}
class NClass{
    public void m2(){
        class NSum{
             public void sum(int x, int y){
                 int sum;
                 sum = x+y;
                 System.out.println(sum);
             }
        }
        NSum s = new NSum();
        s.sum(20,30);
        s.sum(20,50);
        s.sum(80,10);
    }
}