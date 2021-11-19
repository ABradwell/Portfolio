import java.lang.Math;
import java.util.ArrayList;
import java.util.Random;

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
	private int clicked = 0;
	private Solution solution;
	private ArrayList<Solution> solutions;
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
		solutions = new ArrayList<Solution>();
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
	/**
	*A method which activates the click feature, it inverst the light cliked
	*aswell as the neightbors of said light
	*@param column
	*the location in the x direction of the light
	*@param row
	*the location in the y direction of the light 
	**/
	public void click(int column, int row){
		activated[row][column] = !activated[row][column];
		if (column-1>=0){
			activated[row][column-1] = !activated[row][column-1];
		}
		if (column+1<width){
			activated[row][column+1] = !activated[row][column+1];
		}
		if (row-1>=0){
			activated[row-1][column] = !activated[row-1][column];
		}
		if (row+1<height){
			activated[row+1][column] = !activated[row+1][column];
		}
		clicked++;
	}
	/**
	* A method which finds the number of times clicked
	*@return an int value of the amount of times the player has clicked
	**/
	public int getNumberOfSteps(){
		return clicked;
	}
	/**
	*A method which determins if the current model is finished
	*@return a boolean value of if the board is complete
	**/
	public boolean isFinished(){
		for (boolean[] height : activated){
			for(boolean current: height){
				if (!current){
					return false;
				}
			}
		}
		return true;
	}
	/**
	*A method which creates a new, and completely random board for the player to go off of
	*
	**/
	public void randomize(){
		boolean solvable = false;
		while (solvable == false){
			reset();
			for (int i =0; i< height; i++){
				for(int o = 0; o< width; o++){
					Random random = new Random();
					int determination = random.nextInt(21);
					if (determination < 10){
						activated[i][o] = true;
					}else{
						activated[i][o] = false;
					}
				}
			}
			setSolution();
			if (solution.isSuccessful(this)){
				break;
			}			
		}
	}
	/**
	* A method which creates the solution of the given board
	*
	**/
	public void setSolution(){
		solution = LightsOut.solveShortest(this);
	}
	/**
	*
	*
	*@param row
	* the y coordinate for the solution check
	*@param column
	*the x coordinate for the solution check
	*@return a boolean of if the solution requries a click
	*
	**/
	public boolean solutionSelects(int row, int column){
		if (solution != null){
			return solution.get(row,column);
		}else{
			return false;
		}
	}
}

