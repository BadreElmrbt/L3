import java.util.*;

public class Manager extends Employe {
    private Secretaire secretaire;

    public Manager(String nom, String prenom, GregorianCalendar dateNaissance, Adresse adresse, GregorianCalendar dateEmbauche, double salaire) {
        super(nom, prenom, dateNaissance, adresse, dateEmbauche, salaire);
    }

    public static Manager creerManager(String nom, String prenom, GregorianCalendar dateNaissance, Adresse adresse, GregorianCalendar dateEmbauche, double salaire){
        GregorianCalendar ajd = new GregorianCalendar();
        int age = ajd.get(Calendar.YEAR) - dateNaissance.get(Calendar.YEAR);
        if (age >= 16 && age <= 65) {
            return new Manager(nom,prenom,dateNaissance,adresse, dateEmbauche, salaire);
        }
        return null;
    }

    public void attribuerSecretaire(Secretaire secretaire) {
        this.secretaire = secretaire;
        if (secretaire != null) {
            secretaire.ajouterManager(this);
        }
    }

    @Override
    public void augmenterLeSalaire(double pourcentage) {
        if (pourcentage > 0) {
            int anciennete = calculAnnuite();
            this.salaire *= (1 + (pourcentage + (0.5 * anciennete)) / 100);
        }
    }

    public String toString() {
        return super.toString() + "\nSecrétaire : " + (secretaire != null ? secretaire.getPrenom() + " " + secretaire.getNom() : "Aucune");
    }
}
