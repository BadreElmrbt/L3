public class DeEffetMemoire extends De {
    private static int derniereValeur = -1;

    public DeEffetMemoire(String nom, int nbFaces) {
        super(nom, nbFaces);
    }

    public int lancer() {
        int resultat;
        do {
            resultat = super.lancer();
        } while (resultat == derniereValeur); // Continue à lancer jusqu'à obtenir une nouvelle valeur
        derniereValeur = resultat;
        return resultat;
    }
}