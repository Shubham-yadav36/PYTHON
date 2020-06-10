package AnonymousClass;

import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.nio.file.WatchEvent;

public class UseofAnonymous {
    public static void main(String[] args) {
        Frame f = new Frame();
        f.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                for(int i=0;i<10;i++){
                    System.out.println("I am close"+i);
                    System.exit(0);
                }
            }
        });
        f.add(new Label("i create jarFile"));
        f.setSize(500,500);
        f.setVisible(true);
    }
}
