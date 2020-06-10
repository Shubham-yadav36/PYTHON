package StaticInnerClass;

public class StaticWithVar {
    public static void main(String[] args) {
        test.inner n = new test.inner();
        n.m4();
    }
}
class test{
    int x=90;
    static int y=80;
    static class inner {
        public void m4() {
//            System.out.println(x);
            System.out.println(y);
        }
    }
}