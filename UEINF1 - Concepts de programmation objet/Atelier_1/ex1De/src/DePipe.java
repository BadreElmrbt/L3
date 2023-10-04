public class DePipe extends De{
    private int borneMinimale;

    public DePipe(String nom, int nbFaces, int borneMinimale) {
        super(nom, nbFaces); // Appel au constructeur de la classe mère
        if (borneMinimale >= 1 && borneMinimale <= nbFaces) {
            this.borneMinimale = borneMinimale;
        } else {
            System.err.println("Erreur : La borne minimale doit être comprise entre 1 et le nombre de faces.");
            System.exit(1);
        }
    }

    public int lancer() {
        int resultat = super.lancer();
        return Math.max(resultat, borneMinimale + 1); // Retourne la valeur maximale entre le lancer et la borne minimale + 1
    }

    public int getBorneMinimale() {
        return borneMinimale;
    }

    public String toString(){
        return super.toString() + " - Borne minimale : " + borneMinimale;
    }
}
