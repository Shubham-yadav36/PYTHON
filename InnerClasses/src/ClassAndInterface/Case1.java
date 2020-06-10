package ClassAndInterface;

public class Case1 {
    public static void main(String[] args) {
        class1 c1 = new class1();
        c1.m1();
        class2 c2 = new class2();
        c2.m2();
    }
     
}
interface outer{
    public void m1();
    interface inner{
        public void m2();
    }
}
class class1 implements outer{
    public void m1(){
        System.out.println("Outer class implements");
    }
}
class class2 implements outer.inner{
    public void m2(){
        System.out.println("inner class implements");
    }
}