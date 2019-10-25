/**
 * The class <b>Solution</b> is used
 * to store a (partial) solution to the game
 *
 * @author  Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline of Guy-Vincent Jourdan, University of Ottawa
 */
 
public class Solution {


    /**
     * our board. board[i][j] is true is in this
     * solution, the cell (j,i) is tapped
     */
    private boolean[][] board;

    /**
     *  width of the game
     */
    private int width;

    /**
     * height of the game
     */
    private int height;
    
    /**
     * how far along have we constructed that solution.
     * values range between 0 and height*width-1
     */
    private int currentIndex;



    /**
     * Constructor. Creates an instance of Solution 
     * for a board of size <b>widthxheight</b>. That 
     * solution does not have any board position
     * value explicitly specified yet.
     *
     * @param width
     *  the width of the board
     * @param height
     *  the height of the board
     */
    public Solution(int width, int height) {

        this.width = width;
        this.height = height;

        board = new boolean[height][width];
        currentIndex = 0;

    }

   /**
     * Constructor. Creates an instance of Solution 
     * wich is a deep copy of the instance received
     * as parameter. 
     *
     * @param other
     *  Instance of solution to deep-copy
     */
     public Solution(Solution other) {

        this.width = other.width;
        this.height = other.height;
        this.currentIndex = other.currentIndex;

        board = new boolean[height][width];

        for(int i = 0; i < currentIndex; i++){
            board[i/width][i%width] = other.board[i/width][i%width];
        } 

    }


    /**
     * returns <b>true</b> if and only the parameter 
     * <b>other</b> is referencing an instance of a 
     * Solution which is the ``same'' as  this 
     * instance of Solution (its board as the same
     * values and it is completed to the same degree)
     *
     * @param other
     *  referenced object to compare
     */

    public boolean equals(Object other){

        if(other == null) {
            return false;
        }
        if(this.getClass() != other.getClass()) {
            return false;
        }

        Solution otherSolution = (Solution) other;

        if(width != otherSolution.width ||
            height != otherSolution.height ||
            currentIndex != otherSolution.currentIndex) {
            return false;
        }

        for(int i = 0; i < height ; i++){
            for(int j = 0; j < width; j++) {
                if(board[i][j] != otherSolution.board[i][j]){
                    return false;
                }
            }
        }

        return true;

    }


    /** 
    * returns <b>true</b> if the solution 
    * has been entirely specified
    *
    * @return
    * true if the solution is fully specified
    */
    public boolean isReady(){
        return (currentIndex == width*height);
    }

    /** 
    * specifies the ``next'' value of the 
    * solution. 
    * The first call to setNext specifies 
    * the value of the board location (1,1), 
    * the second call specifies the value
    *  of the board location (1,2) etc. 
    *
    * If <b>setNext</b> is called more times 
    * than there are positions on the board, 
    * an error message is printed out and the 
    * call is ignored.
    *
    * @param nextValue
    *  the boolean value of the next position
    *  of the solution
    */
    public void setNext(boolean nextValue) {

        if(currentIndex >= width*height) {
            System.out.println("Board already full");
            return;
        }
        board[currentIndex/width][currentIndex%width] = nextValue;
        currentIndex++;
    }
    
    /**
    * returns <b>true</b> if the solution is completely 
    * specified and is indeed working, that is, if it 
    * will bring a board of the specified dimensions 
    * from being  entirely ``off'' to being  entirely 
    * ``on''.
    *
    * @return
    *  true if the solution is completely specified
    * and works
    */
    public boolean isSuccessful(){

        if(currentIndex < width*height) {
            System.out.println("Board not finished");
            return false;
        }

        for(int i = 0; i < height ; i++){
            for(int j = 0; j < width; j++) {
                if(!oddNeighborhood(i,j)){
                    return false;
                }
            }
        }
        return true;
    }


   /**
    * this method ensure that add <b>nextValue</b> at the
    * currentIndex does not make the current solution
    * impossible. It assumes that the Solution was
    * built with a series of setNext on which 
    * stillPossible was always true.
    * @param nextValue
    *         The boolean value to add at currentIndex
    * @return true if the board is not known to be
    * impossible (which does not mean that the board
    * is possible!)
    */
    public boolean stillPossible(boolean nextValue) {

        if(currentIndex >= width*height) {
            System.out.println("Board already full");
            return false;
        }

        int i = currentIndex/width;
        int j = currentIndex%width;
        boolean before = board[i][j];
        boolean possible = true;

        board[i][j] = nextValue;
        
        if((i > 0) && (!oddNeighborhood(i-1,j))){
            possible = false;
        }
        if(possible && (i == (height-1))) {
            if((j > 0) && (!oddNeighborhood(i,j-1))){
                possible = false;
            }
            if(possible && (j == (width-1))&& (!oddNeighborhood(i,j))){
                possible = false;            
            }
        }
        board[i][j] = before;
        return possible;
    }


    /**
    * this method attempts to finish the board. 
    * It assumes that the Solution was
    * built with a series of setNext on which 
    * stillPossible was always true. It cannot
    * be called if the board can be extended 
    * with both true and false and still be 
    * possible.
    *
    * @return true if the board can be finished.
    * the board is also completed
    */
    public boolean finish(){
        int i = currentIndex/width;
        int j = currentIndex%width;
        while(currentIndex < height*width) {
            if(i < height - 1 ) {
                setNext(!oddNeighborhood(i-1,j));
                i = currentIndex/width;
                j = currentIndex%width;
            } else { //last raw
                if(j == 0){
                    setNext(!oddNeighborhood(i-1,j));
                } else {
                   if((height > 1) && oddNeighborhood(i-1,j) != oddNeighborhood(i,j-1)){
                     return false;
                   }
                   setNext(!oddNeighborhood(i,j-1));
                } 
                i = currentIndex/width;
                j = currentIndex%width;
            }
        }
        if(!oddNeighborhood(height-1,width-1)){
            return false;
        }
        return true;

    }

    /**
     * checks if board[i][j] and its neighborhood
     * have an odd number of values ``true''
     */

    private boolean oddNeighborhood(int i, int j) {
        
        if(i < 0 || i > height - 1 || j < 0 || j > width - 1) {
            return false;
        }
        int total = 0;
        if(board[i][j]){
            total++;
        }
        if((i > 0) && (board[i-1][j])) {
            total++;
        }
        if((i < height -1 ) && (board[i+1][j])) {
            total++;
        }
        if((j > 0) && (board[i][j-1])) {
            total++;
        }
        if((j < (width - 1)) && (board[i][j+1])) {
            total++;
        }
        return (total%2)== 1 ;                
    }
     /**
     * checks if board[i][j] and its neighborhood
     * have an even number of values ``true''
     */
    private boolean evenNeigbourhood(int i, int j) {
        
        if(i < 0 || i > height - 1 || j < 0 || j > width - 1) {
            return false;
        }
        int total = 0;
        if(board[i][j]){
            total++;
        }
        if((i > 0) && (board[i-1][j])) {
            total++;
        }
        if((i < height -1 ) && (board[i+1][j])) {
            total++;
        }
        if((j > 0) && (board[i][j-1])) {
            total++;
        }
        if((j < (width - 1)) && (board[i][j+1])) {
            total++;
        }
        return (total%2)== 0;    
    }

    /**
     * returns a string representation of the solution
     *
     * @return
     *      the string representation
     */
    public String toString() {
        String output = ""; // Prepares output statement
        if (board == null){ // If proposal is empty
            return(""); 
        }
        else { // Aslong as the proposal isnt null
            for (int i = 0; i < height; i++){ // For each row
                output = output + "[";// start row
                for (int o = 0; o < width; o++){ // start collumn
                    output = output + board[i][o] + ", "; 
                }
                output = output + "] \n"; // Starts following line
            }
        }
        return(output);
    }



    /**
     * returns a string representation of the solution
     *
     *
     *@param nextValue
     * the value which is being checked
     *@param model
     * the preexisting board given from GameModel
     *@return
     *      boolean if the next element is possible
     */

    public boolean stillPossible(boolean nextValue, GameModel model){
        int workingLine; 
        if (this.currentIndex > 0){ // If there has been atleast one slot defined
            workingLine = (this.currentIndex) / this.board[0].length ; // Sets the line which is ready to be checked
        }else{ // Call true until defined
            return(true);
        }

        Solution checkProposal = new Solution(this); // Allows for a solution without editing current
        checkProposal.setNext(nextValue); // If we were to add the next variable
        if (workingLine < 2){ // If there isnt a line ready to be checked, return true
            return(true);
        }else{ // Otherwise, prpare which line si being checked
            workingLine = workingLine -2;
        }
        for (int i = 0; i < checkProposal.board[workingLine].length; i++){ // Goes thorugh each slot and checks
            int counter = 0;
            if (i-1 >= 0){ // Above
                if(checkProposal.board[workingLine][i-1]){ //As long as the above sqaure is checakble
                    counter++; // Check
                }
            }
            if (i+1 < checkProposal.board[workingLine].length){
                if(checkProposal.board[workingLine][i+1]){//As long as the below sqaure is checakble
                    counter++;
                }
            }
            if (workingLine - 1 >=0){ // Left Side
                if(checkProposal.board[workingLine-1][i]){//As long as the left sqaure is checakble
                    counter++;
                }
            }
            if (workingLine + 1 < checkProposal.board.length){ // Right side
                if(checkProposal.board[workingLine+1][i]){//As long as the right sqaure is checakble
                    counter++;
                }
            }
            if(checkProposal.board[workingLine][i]){ //Current slot
                counter++;
            }
            if(model.isON(workingLine,i)){
                if (counter % 2 == 1){ // If even amount counted, return false
                    return(false);
                }
            }else{
                if (counter % 2 == 0){
                    return false;
                }
            }
        }
        return(true); // Otherwise return true
    }
    /**
    *A method which checks if the olution sovles the given model
    *@param model
    *the given board form the application
    *@return
    *a boolean represetnation of it it solves the board
    */
    public boolean isSuccessful(GameModel model){
        for (int i = 0; i < model.getHeight(); i++){
            for(int o = 0; o< model.getWidth(); o++){
                if (model.isON(i,o)){
                    if (!evenNeigbourhood(i,o)){
                        return false;
                    }
                }else{
                    if (!oddNeighborhood(i,o)){
                        return false;
                    }
                }
            }
        }
        return true;
    }
    /**
    *A method which checks if there is an overlapping section
    *@param model
    *the given board form the application
    *@return
    *a boolean represetnation of if it overlaps
    */
    public boolean overLap( GameModel model){
        for ( int i = 0; i < model.getHeight(); i++){
            for (int o = 0; o < model.getWidth(); o++){
                if (model.isON(i, o) && board[i][o]){
                    return false;
                }
            }
        }
        return true;
    }




    /**
    * this method attempts to finish the board. 
    * It assumes that the Solution was
    * built with a series of setNext on which 
    * stillPossible was always true. It cannot
    * be called if the board can be extended 
    * with both true and false and still be 
    * possible.
    *
    * @return true if the board can be finished.
    * the board is also completed
    */
    public boolean finish(GameModel model){
        int i = currentIndex/width;
        int j = currentIndex%width;
        while(currentIndex < height*width) {
            //System.out.println("FUCK IT A LOOP");
            i = currentIndex/width;
            j = currentIndex%width;
                if(stillPossible(false,model)){
                    setNext(false);
                }
                else if(stillPossible(true,model)){
                    setNext(true);
                }else{
                    return false;
                }
            }
        return true;
    }
    
    /**
    *A method which checks how many clicks are needed
    *@return
    *an int value of the amount of clicks required
    */
    public int getSize(){
        int total = 0;
        for (int i = 0; i < height; i++){
            for ( int o= 0; o < width; o++){
                if (board[i][o]){
                    total++;
                }
            }
        }
        return total;    
    }
}
