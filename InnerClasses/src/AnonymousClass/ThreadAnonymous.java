package AnonymousClass;

public class ThreadAnonymous {
    public static void main(String[] args) {
        Thread t = new Thread(){
            public void run(){
                for(int i=0;i<10;i++){
                    System.out.println("this is the thread class");
                }
            }
        };
        t.start();
    }
}
