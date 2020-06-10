package StaticInnerClass;

public class Intro {
    static class  nested{
        public void m1(){
            System.out.println("HEllo");
        }
    }

    public static void main(String[] args) {
        nested n = new nested();
        n.m1();
    }
}
