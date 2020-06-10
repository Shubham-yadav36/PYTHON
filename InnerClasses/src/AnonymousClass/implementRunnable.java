package AnonymousClass;

public class implementRunnable {
    public static void main(String[] args) {
        Runnable r = new Runnable() {
            @Override
            public void run() {
                for(int i=0;i<10;i++){
                    System.out.println("Runnable");
                }
            }
        };
        Thread t = new Thread(r);
        t.start();
    }
}
