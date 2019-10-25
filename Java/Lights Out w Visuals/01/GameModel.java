/**
 * The class <b>Solution</b> is used
 * to store a (partial) solution to the game
 *
 * @author  * @author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline of Guy-Vincent Jourdan, University of Ottawa
 */

public class GameModel {

	private int width;
	private int height;
	private boolean[][] activated;
	/**
	* Constructor which initializes the instance variables. Creates a blank overaly for the game
	*@param width
	* The width of the grid
	*@param height
	* the height of the grid
	*
	*
	*/
	public GameModel(int width, int height){
		this.width = width;
		this.height = height;
		activated = new boolean[height][width];
		for (int i = 0; i < height; i++){
			for ( int o = 0; o < width; o++){
				activated[i][o] = false; 
			}
		}
	}
	/**
	*A method which returns the height of the board
	*@return the height of board
	*/
	public int getHeight(){
		return this.height;
	}
	/**
	* A method which retursn the width of the board
	* @return the width of the board
	**/
	public int getWidth(){
		return this.width;
	}
	/**
	* @param i
	* THe row of the light
	* @param j
	* the collumn of the light
	* A method which determines if the light on that slot is lit
	* @return true is the light is lit, and false if it is off
	**/
	public boolean isON(int i, int j){
		return this.activated[i][j]; // Sets the next varible to be the one given by the run program
	}
	/**
	* A method which sets the entire board to an off state
	*
	**/
	public void reset(){
		for (int o = 0; o < this.height; o++){
			for (int i = 0; i < this.width; i++){
				this.activated[o][i] = false;
			}
		}
	}
	/**
	* A method which makes the light at the i,j position to 
	* an onn or off state
	*@param i
	*the int collumn of the light
	*@param j
	*the int row of the light
	*@param value
	* the boolean future value of the light
	**/
	public void set(int i, int j, boolean value){
		this.activated[j][i] = value;
	}
	/**
	*The standard printing method of the class
	*Outputs a nice format for the display of the board
	**/
	public String toString(){
		String output = ""; // Prepares output statement
        if (activated == null){ // If proposal is empty
            return(""); 
        }
        else { // Aslong as the proposal isnt null
            for (int i = 0; i < this.height; i++){ // For each row
                output = output + "[";// start row
                for (int o = 0; o < this.width; o++){ // start collumn
                    output = output + this.activated[i][o] + ", "; 
                }
                output = output + "] \n"; // Starts following line
            }
        }
        return(output);
	}
}

