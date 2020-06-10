package RegularInnerClass;

public class levelOfvariableAccessing {
    int i=10;
    class inner{
        int i =100;
        public void m1(){
            int i = 1000;
            System.out.println(i);
            System.out.println(this.i);  // System.out.println(inner.i)
            System.out.println(levelOfvariableAccessing.this.i);
        }
    }

    public static void main(String[] args) {
        new levelOfvariableAccessing().new inner().m1();
    }
}
