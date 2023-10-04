import java.util.ArrayList;

public class DeFacesAutres extends De {
    private ArrayList<String> facesAutres;

    public DeFacesAutres(String nom, ArrayList<String> facesAutres) {
        super(nom, facesAutres.size());
        this.facesAutres = facesAutres;
    }

    public String lancerAutreString(){
        int index = (lancer()) - 1;
        return facesAutres.get(index);
    }

    public void setFacesAutres(ArrayList<String> facesAutres) {
        this.facesAutres = facesAutres;
        this.setNbFaces(facesAutres.size());
    }
}
