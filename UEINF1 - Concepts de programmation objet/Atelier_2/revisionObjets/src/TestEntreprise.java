import java.util.*;

public class TestEntreprise {
    public static void main(String[] args) {
        Personne p1 = new Personne("nom1", "prenom1", new GregorianCalendar(2003, 7, 9), new Adresse(300, "Jean Nicoli", "20250", "Corte"));
        Personne p2 = new Personne("nom2", "prenom2", 2004, 9, 7, 300, "Jean Nicoli", "20250", "Corte");
        System.out.println(p1);
        System.out.println(p2);

        System.out.println("\nLe nombre de personnes créées : " + Personne.getNbrPersonnes());
        System.out.println("Est-ce que p1 est plus âgée que p2 ? (true) --> " + Personne.plusAgee(p1, p2));
        System.out.println("Est-ce que p1 est égale à p2 ? (false) --> " + p1.equals(p2));

        Employe e1 = Employe.createEmploye("nom3", "prenom3", new GregorianCalendar(2003, 7, 9), new Adresse(300, "Jean Nicoli", "20250", "Corte"), new GregorianCalendar(2019, 6, 10), 10000.0);
        System.out.println(e1);

        e1.augmenterLeSalaire(10); // Augmentation de 10%
        System.out.println("\nLe nouveau salaire après augmentation : " + e1.getSalaire());
        System.out.println("Ancienneté dans l'entreprise : " + e1.calculAnnuite() + " années");

        Secretaire s1 = new Secretaire("nom4", "prenom4", new GregorianCalendar(2000, 5, 15), new Adresse(200, "de la Liberte", "12345", "Ville"), new GregorianCalendar(2018, 3, 1), 20000.0);

        Manager m1 = new Manager("nom5", "prenom5", new GregorianCalendar(1995, 2, 25), new Adresse(150, "du Progres", "67890", "Ville2"), new GregorianCalendar(2015, 10, 2), 30000.0);

        m1.attribuerSecretaire(s1);
        s1.ajouterManager(m1);

        m1.augmenterLeSalaire(10);

        System.out.println(s1);
        System.out.println(m1);

        System.out.println("\nLe nombre de personnes créées : " + Personne.getNbrPersonnes());
    }
}
