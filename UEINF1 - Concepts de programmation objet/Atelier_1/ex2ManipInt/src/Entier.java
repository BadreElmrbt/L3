public class Entier {
    private final int borneMin;
    private final int borneMax;
    private int valeur;

    public Entier(int borneMin, int borneMax) {
        this.borneMin = borneMin;
        this.borneMax = borneMax;
        this.valeur = 0;
    }

    public Entier(int borneMin, int borneMax, int valeur) {
        this.borneMin = borneMin;
        this.borneMax = borneMax;
        this.valeur = Math.max(Math.min(valeur, borneMax), borneMin);
    }

    public void set(int valeur) {
        if (valeur >= borneMin && valeur <= borneMax) {
            this.valeur = valeur;
        }
    }

    public void incremente() {
        if (valeur < borneMax) {
            valeur++;
        }
    }

    public void incremente(int pas) {
        if (valeur + pas <= borneMax) {
            valeur += pas;
        }
    }

    public int getValeur() {
        return valeur;
    }

    public String toString(){
        return "Entier(borneMin = " + borneMin + ", borneMax = " + borneMax + ", valeur = " + valeur + ")";
    }

    public boolean equals(Object obj){
        boolean result = false;
        if (obj != null && obj instanceof De){
            Entier ent = (Entier) obj;
            result = (valeur == ent.valeur) && (borneMin == ent.borneMin) && (borneMax == ent.borneMax);
        }
        return result;
    }
}
