public class Adresse {
	public static final int AUCUN_NUMERO=-1;
	public static final int INUTILE_NUMERO=-2;
	public static final String INCONNU_CHAINE="Inconnu";
	public static final String INUTILE_CHAINE="Inutile";
	private int numero=AUCUN_NUMERO;
	private String rue=INCONNU_CHAINE;
	private String code_postal=INCONNU_CHAINE;
	private final String ville;

	public Adresse(int numero, String rue,String code_postal, String ville){
		setCode_postal(code_postal);
		setNumero(numero);
		this.rue = rue;
		this.ville = ville;
	}
	
	public Adresse(String code_postal, String ville) {
		this(INUTILE_NUMERO,INUTILE_CHAINE,code_postal,ville);
	}

	public Adresse(String code_postal, String rue, String ville) {
		this(INUTILE_NUMERO,rue,code_postal,ville);
	}

	public String getCode_postal() {
		return code_postal;
	}
	
	public final void  setCode_postal(String c_p){
		if (code_postal.equals(INCONNU_CHAINE)&&(c_p.matches("[0-9]{5}")))
			code_postal=c_p;
		else{
			if (!code_postal.equals(INCONNU_CHAINE))
				System.err.println("Le code postal a déjà été attribué, vous ne pouvez plus le modifier...");
			else {
				System.err.println("Code postal mal écrit, il doit être de la forme NNNNN avec N un chiffre différent de 0");
				System.err.println("Vous pouvez réessayer une nouvelle affectation...");
			}
		}
	}

	public int getNumero() {
		return numero;
	}
	
	public final void  setNumero(int n) {
		if (((numero==AUCUN_NUMERO)||(numero==INUTILE_NUMERO))&&(n>0)) numero = n;
		else System.err.println("Numero incorrect, il doit être positif...");
	}
	
	public String getRue() {
		return rue;
	}
	
	public void setRue(String r) {
		rue = r;
	}
	
	public String getVille() {
		return ville;
	}

	public String toString() {
		StringBuilder result=new StringBuilder();
		if ((numero!=AUCUN_NUMERO)&&(numero!=INUTILE_NUMERO)) result.append("n°").append(numero).append(",");
		if ((!rue.equals(INCONNU_CHAINE))&&(!(rue.equals(INUTILE_CHAINE)))) result.append(" Rue ").append(rue);
		if (!code_postal.equals(INCONNU_CHAINE)) result.append(" ").append(code_postal).append(" ");
		else result.append(" Code postal inconnu ");
		result.append(ville);
		return result.toString();
	}
}
