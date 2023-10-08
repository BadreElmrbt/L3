import java.util.*;

public class Employe extends Personne {
    public double salaire;
    private GregorianCalendar dateEmbauche;

    public Employe(String nom, String prenom, GregorianCalendar dateNaissance, Adresse adresse, GregorianCalendar dateEmbauche, double salaire){
		super(nom,prenom,dateNaissance,adresse);
        this.dateEmbauche = dateEmbauche;
        this.salaire = salaire;
	}

    public static Employe createEmploye(String nom, String prenom, GregorianCalendar dateNaissance, Adresse adresse, GregorianCalendar dateEmbauche, double salaire){
        GregorianCalendar ajd = new GregorianCalendar();
        int age = ajd.get(Calendar.YEAR) - dateNaissance.get(Calendar.YEAR);
        //System.out.println(age);
        if (age >= 16 && age <= 65) {
            return new Employe(nom,prenom,dateNaissance,adresse, dateEmbauche, salaire);
        }
        
        return null;
    }

    public void augmenterLeSalaire(double pourcentage){
        if (pourcentage > 0){
            salaire *= (1+(pourcentage/100));
        }
    }

    public int calculAnnuite(){
        GregorianCalendar ajd = new GregorianCalendar();
        int annees = ajd.get(Calendar.YEAR) - dateEmbauche.get(Calendar.YEAR);
        return annees;
    }

    public double getSalaire() {
        return salaire;
    }

    public void setSalaire(double salaire) {
        this.salaire = salaire;
    }

    @Override
    public String toString() {
        return super.toString() + 
        "\nEmbauché(e) le : "+ dateEmbauche.get(Calendar.DAY_OF_MONTH)+
		"-"+dateEmbauche.get(Calendar.MONTH)+
		"-"+dateEmbauche.get(Calendar.YEAR) +
        "\nSalaire = " + salaire + " euros";
    }
}