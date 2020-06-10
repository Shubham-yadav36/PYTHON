package Intro;

class mainInOuter {
    public static void main(String[] args) {
//       mainInOuter o = new mainInOuter();
//       mainInOuter.inner i = o.new inner();
//       i.m();

//       other way to write it
//        mainInOuter.inner oi = new mainInOuter().new inner();
//        oi.m();

//        other way to write it
        mainInOuter.inner oi;
        oi = new mainInOuter().new inner().m();
    }
    class inner{
        public inner m(){
            System.out.println("inner class");
            return null;
        }
    }
}
