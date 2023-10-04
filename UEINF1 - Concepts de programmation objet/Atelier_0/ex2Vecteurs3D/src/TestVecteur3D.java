public class TestVecteur3D {
	public static void main(String[] args) {
		Vecteur3D vect1 = new Vecteur3D(3,2,5);
		Vecteur3D vect2 = new Vecteur3D(1,2,3);

        System.out.println("vect1 = " + vect1);
        System.out.println("Norme de vect1 : " + vect1.norme());

        System.out.println("vect2 = " + vect2);
		System.out.println("Norme de vect2 : " + vect2.norme());
		
        System.out.println("vect 1 + vect 2 = " + vect1.somme(vect2));
		System.out.println("v1.v2 = " + vect1.produitScalaire(vect2));
	}
}
