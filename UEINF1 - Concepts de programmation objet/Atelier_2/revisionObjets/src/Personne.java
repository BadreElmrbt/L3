import java.util.*;

public class Personne{
	// Attributs de classes
	private static int nbrPersonnes = 0 ;
	private static final Adresse ADRESSE_INCONNUE = null;

	// Attributs d'instances
    private String nom;
    private String prenom;
    private final GregorianCalendar dateNaissance;
    private Adresse adresse=ADRESSE_INCONNUE;
	
	// Constructeurs
	public Personne(String nom, String prenom, GregorianCalendar dateNaissance, Adresse adresse){
		this.nom = nom.toUpperCase();
		this.prenom = prenom;
		this.dateNaissance = dateNaissance;
		this.adresse = adresse;
		nbrPersonnes++;
	}
	
	public Personne(String nom, String prenom, int annee, int mois, int jour, int numero, String rue, String code_postal, String ville){
		this(nom, prenom, new GregorianCalendar(annee,mois,jour), new Adresse(numero,rue,code_postal,ville));
	}

	// Getters
	public static int getNbrPersonnes() {
		return nbrPersonnes;
	}

	public String getNom(){
		return nom;
	}
	
	public String getPrenom(){
		return prenom;
	}
	
	public GregorianCalendar getDateNaissance() {
		return dateNaissance;
	}
	
	public Adresse getAdresse() {
		return adresse;
	}
	
	// Setters
	public void setNom(String nom) {
		this.nom = nom;
	}

	public void setPrenom(String prenom) {
		this.prenom = prenom;
	}

	public void setAdresse(Adresse adresse) {
		this.adresse = adresse;
	}

	// Méthodes de classes
	public static boolean plusAgee(Personne p1, Personne p2){
		return p1.dateNaissance.before(p2.dateNaissance);
	}

	// Méthodes d'instances
	public boolean plusAgeeQue(Personne autrePersonne) {
        return dateNaissance.before(autrePersonne.dateNaissance);
    }
	
	// Redéfinitions des méthodes toString et equals
	@Override
	public String toString(){
		String result="\nNom : "+nom+"\n"
		+"Prénom : "+prenom+"\n"+
		"Né(e) le : "+dateNaissance.get(Calendar.DAY_OF_MONTH)+
		"-"+dateNaissance.get(Calendar.MONTH)+
		"-"+dateNaissance.get(Calendar.YEAR)+"\n"+
		"Adresse : "+
		adresse.toString();
		return result;
	}

	public boolean equals(Object obj){
		boolean result = false;
		if (obj != null && obj instanceof Personne){
			Personne p = (Personne) obj;
			result = this.nom.equals(p.nom) &&
					 this.prenom.equals(p.prenom) &&
					 this.dateNaissance.equals(p.dateNaissance);
		}
		return result;
	}
}

    
   
   