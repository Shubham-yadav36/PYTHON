package StaticInnerClass;

public class OuterClassStatic {
    public static void main(String[] args) {
        outer.inner n = new outer.inner();
        n.m1();
    }
}
class outer{
    static class inner{
        public void m1(){
            System.out.println("Hello");
        }
    }
}