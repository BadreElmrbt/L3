public class Robot {
	//Declaration des attributs
	private String refRobot;
	private String nomRobot;
	private int x;
	private int y;
	private int orientation;
	
	public static final int NORD = 1;
	public static final int EST = 2;
	public static final int SUD = 3;
	public static final int OUEST = 4;
	
	public static int nombreRobot=0;
    
    //Declaration du constructeur
	public Robot(String nomRobot, int x, int y, int orientation) {
		this.nomRobot=nomRobot;
		this.x=x;
		this.y=y;
		this.orientation = orientation ;
		nombreRobot++;
		this.refRobot = "ROB"+nombreRobot;
	}
	
    public Robot(String nomRobot){
        this(nomRobot,0,0,1);
    }

    public void modifOrientation(int nouvOrientation){
        this.orientation = nouvOrientation;
    }

    public void deplacer(){
		if (orientation == NORD){
			y++;
		}
		else if (orientation == EST){
			x++;
		}
		else if (orientation == SUD & y >= 0){
			y--;
		}
		else if (orientation == OUEST & x >= 0){
			x--;
		}	
	}

    public String chaineOrientation(){
		if (orientation == NORD){
			return "NORD";
		}
		if (orientation == EST){
			return "EST";
		}
		if (orientation == SUD){
			return "SUD";
		}
		if (orientation == OUEST){
			return "OUEST";
		}
		return "";
	}

    public void afficheToi(){
		System.out.println("Nom : " + nomRobot + " ; Référence : " + refRobot + " ; x = " + x + " ; y = " + y + " ; Orientation : " + chaineOrientation());
	}

    public String toString(){
		return ("Nom : " + nomRobot + " ; Référence : " + refRobot + " ; x = " + x + " ; y = " + y + " ; Orientation : " + chaineOrientation());
	}
}