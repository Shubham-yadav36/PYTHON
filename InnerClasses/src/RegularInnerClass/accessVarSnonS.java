package RegularInnerClass;

public class accessVarSnonS {
    String name= "shubh";
    String lname= "yadav";
    class inner{
        public void m1(){
            System.out.println(name);
            System.out.println(lname);
        }
    }

    public static void main(String[] args) {
        new accessVarSnonS().new inner().m1();
    }
}
