public class ManipRobot {
    public static void main(String[] args) throws Exception {
        Robot r1 = new Robot("Toto",10,20,3);
        Robot r2 = new Robot("Titi");

        r1.deplacer();
        r1.modifOrientation(4); //OUEST
        r1.deplacer();

        r2.deplacer();
        r2.modifOrientation(2); //EST
        r2.deplacer();

        System.out.println(r1);
        System.out.println(r2);
    }
}
