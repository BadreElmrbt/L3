import java.util.*;

public class De {
    //Attributs
    private String nom;
    private int nbFaces;
    private static int nombreDesCrees = 0;
    private static Random r = new Random();

    //Constructeurs
    public De(String nom, int nbFaces) {
        this.nom = nom;
        if (nbFaces >= 3 && nbFaces <= 120) {
            this.nbFaces = nbFaces;
            nombreDesCrees++;
        } else {
            System.err.println("Erreur : Le nombre de faces doit être compris entre 3 et 120.");
            System.exit(1);
        }
    }

    public De() {
        this("Dé n°" + (nombreDesCrees), 6);
    }

    public De(int nbFaces) {
        this("Dé n°" + (nombreDesCrees), nbFaces);
    }

    public De(String nom) {
        this(nom, 6);
        
    }

    //Getters
    public static int getNombreDesCrees() {
        return nombreDesCrees;
    }

    public int getNbFaces() {
        return nbFaces;
    }

    public String getNom() {
        return nom;
    }

    //Setters
    public void setNbFaces(int nbFacesNew) {
        if (nbFacesNew >= 3 && nbFacesNew <= 120) {
            this.nbFaces = nbFacesNew;
        } else {
            System.err.println("Erreur : Le nombre de faces doit être compris entre 3 et 120.");
        }
    }

    //Méthodes
    public int lancer() {
        return r.nextInt(nbFaces) + 1;
    }

    public int lancer(int nbLancers) {
        int meilleurLancer = lancer();
        for (int i = 1; i < nbLancers; i++) {
            int lancerCourant = lancer();
            if (lancerCourant > meilleurLancer) {
                meilleurLancer = lancerCourant;
            }
        }
        return meilleurLancer;
    }

    //Redéfinition de méthodes
    public String toString(){
        return "Nom : " + getNom() + " - Nombre de faces : " + getNbFaces();
    }

    public boolean equals(Object obj){
        boolean result = false;
        if (obj != null && obj instanceof De){
            De d = (De) obj;
            result = (this.nbFaces == d.nbFaces)&&(this.nom.equals(d.nom));
        }
        return result;
    }
}

    

