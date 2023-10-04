public class Vecteur3D {
	private double x;
	private double y;
	private double z;
	
	public Vecteur3D(double x, double y, double z){
		this.x=x;
		this.y=y;
		this.z=z;
	}
	
	public Vecteur3D(){
		this(0,0,0);
	}
	
	public void affiche(){
		System.out.println("<" + x + ", " + y + ", " + z + ">");
	}

    public String toString(){
		return "<" + x + ", " + y + ", " + z + ">";
	}

    public double norme(){
		return Math.sqrt(x*x+y*y+z*z);
	}

    public double getX(){
		return x;
	}

	public double getY(){
		return y;
	}

	public double getZ(){
		return z;
	}
	
	public double produitScalaire(Vecteur3D v1){
		return (x*v1.getX() + y*v1.getY() + z*v1.getZ());
	}
	
	public Vecteur3D somme(Vecteur3D v1){
		double x2 = x + v1.getX();
		double y2 = y + v1.getY();
		double z2 = z + v1.getZ();
		
		Vecteur3D v2 = new Vecteur3D(x2,y2,z2);
		
		return v2;
	}
}