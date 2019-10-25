//Vital imports, for the games operation
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;
//Unsure if needed, playing it safe
import java.awt.Color;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.BorderFactory;
import javax.swing.border.Border;
    /**
    * A class which creates a button which will be used in the main code logic
    * Button has a series of uses, including indicating slots for the solution, aswell as indicating what is on and off
    * The main building block of the code
    * @author  * @author Aiden Stevenson Bradwell, University of Ottawa, based
    * off the outline of Guy-Vincent Jourdan, University of Ottawa
    */
public class GridButton extends JButton {

	private static final ImageIcon[] icons = new ImageIcon[4]; //
    private int column; //THe x coord of the button
    private int row; // the y coord of the button
    private String icon; // the name of the state
    private boolean isOn; // if the button is lit
    private int id; // the official ID
    /**
     * Constructor used for initializing a GridButton at a specific
     * Board location.
     * 
     * @param column
     *            the column of this Cell
     * @param row
     *            the row of this Cell
     */

    public GridButton(int column, int row) {
        super(); 
        this.column = column;
        this.row = row;
        this.id = 1;
        //following code used to make the button look proper
        setBackground(Color.WHITE);
		setIcon(getImageIcon());
		Border emptyBorder = BorderFactory.createEmptyBorder(0, 0, 0, 0);
		setBorder(emptyBorder);
		setBorderPainted(false);
    }
    /**
    A method which sets the image of the button
    @return the Image which will be used for the button, where it is on or off
    Uses a list of immages provided int he internal files
    */
    private ImageIcon getImageIcon() {
		if (icons[id] == null) {
		    String strId = Integer.toString(id);
		    icons[id] = new ImageIcon(GridButton.class.getResource("/Icons/Light-" + strId + ".png"));
		}
		return icons[id];
    }

   /**
    * sets the icon of the button to reflect the
    * state specified by the parameters
    * @param isOn true if that location is ON
    * @param isClicked true if that location is
    * tapped in the model's current solution
    */ 
    public void setState(boolean isOn, boolean isClicked) {
        if (isOn && isClicked){
            id = 2;
        }else if(isOn){
            id = 0;
        }else if(isClicked){
            id = 3;
        }else{
            id = 1;
        }
        setIcon(getImageIcon());

    }
    /**
    @return the int id of the skin, which determines its look


    */
    public int getType(){
    	return id;
    }
 

    /**
     * Getter method for the attribute row.
     * 
     * @return the value of the attribute row
     */

    public int getRow() {
        return this.row;
    }

    /**
     * Getter method for the attribute column.
     * 
     * @return the value of the attribute column
     */

    public int getColumn() {
        return this.column;
    }

}
