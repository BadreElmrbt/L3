public class TestEntier {
    public static void main(String[] args) {
        Entier entier1 = new Entier(0, 10);
        System.out.println("Valeur initiale : " + entier1.getValeur());
        entier1.incremente();
        System.out.println("Après incrémentation : " + entier1.getValeur());
        entier1.incremente(3);
        System.out.println("Après incrémentation par pas de 3 : " + entier1.getValeur());
        entier1.set(8);
        System.out.println("Après set : " + entier1.getValeur());
        entier1.set(15);
        System.out.println("Après set hors des bornes 0 13: " + entier1.getValeur());

        
        EntierFou entierFou1 = new EntierFou(0, 10, 5);

        System.out.println("Valeur initiale : " + entierFou1.getValeur());
        System.out.println("Niveau de folie : " + entierFou1.getNiveauDeFolie());

        entierFou1.incremente();
        System.out.println("Après incrémentation : " + entierFou1.getValeur());   
    }
}
