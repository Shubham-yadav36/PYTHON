package ClassAndInterface;

public class classinsideInterface {
    public static void main(String[] args) {
        vehicle.defaultconfig vc = new vehicle.defaultconfig();
        System.out.println(vc.getnofwheel());

        bus b = new bus();
        System.out.println(b.getnofwheel());
    }
}
interface vehicle{
    public int getnofwheel();
    class defaultconfig{
        public int getnofwheel(){
            return 2;
        }
    }
}
class bus implements vehicle{
    @Override
    public int getnofwheel(){
        return 8;
    }
}