import java.util.*;

public class Secretaire extends Employe {
    private List<Manager> managers;

    public Secretaire(String nom, String prenom, GregorianCalendar dateNaissance, Adresse adresse, GregorianCalendar dateEmbauche, double salaire) {
        super(nom, prenom, dateNaissance, adresse, dateEmbauche, salaire);
        this.managers = new ArrayList<>();
    }

    public void ajouterManager(Manager manager) {
        if ((managers.size() < 5) && (!managers.contains(manager))) {
            managers.add(manager);
            manager.attribuerSecretaire(this);
        } else {
            System.out.println("Une secrétaire ne peut avoir plus de 5 managers.");
        }
    
    }
    
    public void supprimerManager(Manager manager) {
        managers.remove(manager);
        manager.attribuerSecretaire(null);
    }

    @Override
    public void augmenterLeSalaire(double pourcentage) {
        double bonusManagers = managers.size() * 0.1;
        super.augmenterLeSalaire(pourcentage + bonusManagers);
    }

    public List<Manager> getManagers() {
        return managers;
    }

    public String toString() {
        StringBuilder result = new StringBuilder(super.toString());
        result.append("\nManager(s) : ");
        for (Manager manager : managers) {
            result.append(manager.getPrenom()).append(" ").append(manager.getNom()).append(", ");
        }
        if (!managers.isEmpty()) {
            result.delete(result.length() - 2, result.length());
        }
        return result.toString();
    }
}
