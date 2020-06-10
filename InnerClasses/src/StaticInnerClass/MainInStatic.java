package StaticInnerClass;

public class MainInStatic {
    static class inner{
        public static void main(String[] args){
            System.out.println("static clsss");
        }
    }

    public static void main(String[] args) {
        System.out.println("Main");
    }
}
