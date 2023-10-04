import java.util.ArrayList;

public class TestDe {
    public static void main(String[] args) {
        De de0 = new De("Mon Dé", 8);
        System.out.println(de0);

        De de1 = new De(10);
        System.out.println(de1);

        De de2 = new De("Autre Dé");
        System.out.println(de2);

        De de3 = new De();
        System.out.println(de3);

        de3.setNbFaces(12);
        System.out.println("Nouveau nombre de faces : " + de3.getNbFaces());

        int resultat = de3.lancer();
        System.out.println("Résultat du lancer : " + resultat);

        int meilleurLancer = de3.lancer(5);
        System.out.println("Meilleur lancé sur 5 lancés : " + meilleurLancer);

        boolean resultat2 = de3.equals(de2);
        System.out.println("Est ce que de3 est égal à de2 : " + resultat2);
        //De de5 = new De(2);
        //System.out.println(de5);

        DePipe de4 = new DePipe("Nouveau dé", 10, 5);
        int resultat3 = de4.lancer();
        System.out.println(de4);
        System.out.println("Résultat du lancé du dé pipé : " + resultat3);

        DeEffetMemoire de5 = new DeEffetMemoire("Dé mémoire", 6);
        System.out.println("Résultat du lancer du dé à effet mémoire : " + de5.lancer());
        System.out.println("Résultat du lancer du dé à effet mémoire : " + de5.lancer());

        ArrayList<String> faces = new ArrayList<>();
        faces.add("Kelawin");
        faces.add("Kelaloose");
        faces.add("Relancez");
        faces.add("Passez votre tour");

        DeFacesAutres de6 = new DeFacesAutres("Dé avec faces autres", faces);
        System.out.println(de6 + " --- Résulat : " + de6.lancerAutreString());
    }
}
