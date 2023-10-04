import java.util.Random;

public class EntierFou extends Entier {
    private int niveauDeFolie;

    public EntierFou(int borneMin, int borneMax, int valeur, int niveauDeFolie) {
        super(borneMin, borneMax, valeur);
        this.niveauDeFolie = niveauDeFolie;
    }

    public EntierFou(int borneMin, int borneMax, int niveauDeFolie) {
        super(borneMin, borneMax);
        this.niveauDeFolie = niveauDeFolie;
    }

    @Override
    public void incremente() {
        Random random = new Random();
        int increment = random.nextInt(niveauDeFolie + 1);
        super.incremente(increment);
    }

    public int getNiveauDeFolie() {
        return niveauDeFolie;
    }
}
