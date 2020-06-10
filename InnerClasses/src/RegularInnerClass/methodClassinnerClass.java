package RegularInnerClass;

class methodClassinnerClass {
    class inner{
        public void m1(){
            System.out.println("inner class");
        }
    }
    public void m2(){
        System.out.println("Outer class");
        inner i = new inner();
        i.m1();
    }

    public static void main(String[] args) {
        methodClassinnerClass o = new methodClassinnerClass();
        o.m2();
    }
}
