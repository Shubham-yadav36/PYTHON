package AnonymousClass;

public class AnnonymourInsideArguement {
    public static void main(String[] args) {
        new Thread(new Runnable(){
            public void run() {
                for(int i=10;i<10;i++){
                    System.out.println("Hello");
                }
            }
        }).start();
    }
}
