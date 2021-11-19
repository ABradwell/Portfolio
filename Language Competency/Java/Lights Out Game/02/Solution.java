
/**
 * The class <b>Solution</b> is used
 * to store a (partial) solution to the game
 *
 * @author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline and instruction of Guy-Vincent Jourdan, University of Ottawa
  */
public class Solution {


    // Soluiton Class parameters
    private int nextInt = 0; // Start at (1,1) 
    public boolean[][] proposal; // prepares solution
    private int currentCol = 0; // (1,_)
    private int currentRow = 0;// (_1)
    public int width; // []
    public int height;// [][]

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
        this.proposal = new boolean[height][width]; // Preapres a determined proposal
        this.width = width; 
        this.height = height; 
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
       if (other.proposal != null){
            if (other.proposal[0] != null){ // As long as the other proposal has values
                this.width = other.proposal[0].length; // sets width
                this.height = other.proposal.length; // sets height
                this.proposal = new boolean[other.proposal.length][other.proposal[0].length]; // copies array size
                for (int i = 0; i < other.proposal.length; i++){ // 
                    for (int o = 0; o < other.proposal[0].length; o++){ //
                        this.proposal[i][o] = other.proposal[i][o]; // duplicates array
                    }
                }
                this.nextInt = other.nextInt; // sets net interval
            } 
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
         if (this == null && other == null){ // Assures neither are null
            return (true); // if they are theyre the same
        }
        if(other.getClass() == this.getClass()){ // assures they are the same class
            Class classy = other.getClass(); // Prepares class
            Solution copy = (Solution) other; // Sets other to be solution
            if(this.width == copy.width){  // makes sure theyre the same width
                if(this.height == copy.height){ // makes sure theyre the same height
                    for(int i = 0; i < this.height; i++){
                        for(int o = 0; o < this.width; o++){
                            if (this.proposal[i][o] != copy.proposal[i][o]){
                                return (false); // Checks all variables for equivalence
                            }
                        }
                    }
                    
                }else{
                    return(false);
                }
            }else{
                return(false);
            }
        }else{
            return(false);
        }
        return(true);
    }


    /** 
    * returns <b>true</b> if the solution 
    * has been entirely specified
    *
    * @return
    * true if the solution is fully specified
    */
    public boolean isReady(){
        return(this.nextInt == this.width*this.height); // As long as the nextInt is outside of the size of array
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
        if (this.nextInt < this.width*this.height){ // As long as it is not larger than te size of the array
            this.proposal[(this.nextInt/this.proposal[0].length)][(this.nextInt%this.proposal[0].length)] = nextValue; // Sets the next varible to be the one given by the run program
            this.nextInt++; 
        }else{ //Otherwise tlet them know the array is full
            System.out.println("ERROR: ARRAY IS FULLY DEFINED...");
        }
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
        int counter;
        boolean good;
        // Null checks on the matrix
        if (this.proposal == null){
            return(false);
        } else if (this.proposal[0] == null){
            return(false);
        }
        // Checks for a 1 by 1 matrix
        if (this.proposal.length == 1 && this.proposal[0].length == 1){
            if (this.proposal[0][0] == true){
                return (true);
            }
        }
        //Goes through each slot of the array, and checsk their validity
        for (int i = 0; i < this.proposal.length; i++){
            for(int o = 0; o < this.proposal[0].length; o++){
                counter = 0;
                // Above
                if ((i - 1) >= 0){
                    if (this.proposal[i-1][o]){ //If the placemnent is true then add 1 to the counter
                        counter++;
                    }
                }
                // Below
                if ((i + 1) < this.proposal.length){ //If the placemnent is true then add 1 to the counter
                    if(this.proposal[i + 1][o]){
                        counter++;
                    }
                }
                // Right side
                if ((o + 1) < this.proposal[0].length){ //If the placemnent is true then add 1 to the counter
                    if(this.proposal[i][o + 1]){
                        counter++;
                    }
                }
                // Left Side
                if((o - 1) >= 0){
                    if(this.proposal[i][o - 1]){ //If the placemnent is true then add 1 to the counter
                        counter++;
                    }
                }
                // Piece Itself
                if(this.proposal[i][o]){ //If the placemnent is true then add 1 to the counter
                        counter++;
                    }
                if (counter % 2 == 0){ // If there is an even amount counted
                    return(false);
                }
            }
        }

    return(true);
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
        int workingLine; 
        if (this.nextInt > 0){ // If there has been atleast one slot defined
            workingLine = (this.nextInt) / this.proposal[0].length ; // Sets the line which is ready to be checked
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

        for (int i = 0; i < checkProposal.proposal[workingLine].length; i++){ // Goes thorugh each slot and checks
            int counter = 0;
            if (i-1 >= 0){ // Above
                if(checkProposal.proposal[workingLine][i-1]){ //As long as the above sqaure is checakble
                    counter++; // Check
                }
            }
            if (i+1 < checkProposal.proposal[workingLine].length){
                if(checkProposal.proposal[workingLine][i+1]){//As long as the below sqaure is checakble
                    counter++;
                }
            }
            if (workingLine - 1 >=0){ // Left Side
                if(checkProposal.proposal[workingLine-1][i]){//As long as the left sqaure is checakble
                    counter++;
                }
            }
            if (workingLine + 1 < checkProposal.proposal.length){ // Right side
                if(checkProposal.proposal[workingLine+1][i]){//As long as the right sqaure is checakble
                    counter++;
                }
            }
            if(checkProposal.proposal[workingLine][i]){ //Current slot
                counter++;
            }
            if (counter % 2 == 0){ // If even amount counted, return false
                return(false);
            }
        }
        return(true); // Otherwise return true
    }




    /**
     * returns a string representation of the solution
     *
     * @return
     *      the string representation
     */
    public String toString() {
        String output = ""; // Prepares output statement
        if (this.proposal == null){ // If proposal is empty
            return(""); 
        }
        else { // Aslong as the proposal isnt null
            for (int i = 0; i < this.proposal.length; i++){ // For each row
                output = output + "[";// start row
                for (int o = 0; o < this.proposal[0].length; o++){ // start collumn
                    output = output + this.proposal[i][o] + ", "; 
                }
                output = output + "] \n"; // Starts following line
            }
        }
        return(output);
    }
}
