import java.util.ArrayList;
import java.util.Scanner;

/**
 * The class <b>LightsOut</b> is the
 * class that implements the method to
 * computs solutions of the Lights Out game.
 * It contains the main of our application.
 *
 * @author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline and instruction of Guy-Vincent Jourdan, University of Ottawa
  */

public class LightsOut {

    private ArrayList<Solution> solutions;

    /**
     * The method <b>solve</b> finds all the 
     * solutions to the <b>Lights Out</b> game 
     * for an initially completely ``off'' board 
     * of size <b>widthxheight</b>, using a  
     * Breadth-First Search algorithm. 
     *
     * It returns an <b>ArrayList&lt;Solution&gt;</b> 
     * containing all the valid solutions to the 
     * problem.
     *
     * During the computation of the solution, the 
     * method prints out a message each time a new 
     * solution  is found, along with the total time 
     * it took (in milliseconds) to find that solution.
     *
     * @param width
     *  the width of the board
     * @param height
     *  the height of the board
     * @return
     *  an instance of <b>ArrayList&lt;Solution&gt;</b>
     * containing all the solutions
     */
    public static ArrayList<Solution> solve(int width, int height){
        //Initialize the array and the queue
        ArrayList<Solution> solutions = new ArrayList<Solution>();
        ArrayListSolutionQueue partialSolutions = new ArrayListSolutionQueue();
        //Initialize over parts of code
        Solution blank = new Solution(width, height); // new blank solution
        partialSolutions.enqueue(blank); // queues balnk solution
        long start = System.currentTimeMillis(); // for timing purposes
        boolean valid = false; // for valididity check


        while(!(partialSolutions.isEmpty())){ //As long as all soltuions have not yet been checked
            Solution current = partialSolutions.dequeue(); // Take the current soltuion work is to be done to
            if (current.isReady()){ // If the array is fully defined
                if(current.isSuccessful()){ // If the array is sucessful
                    solutions.add(current); // Add to the solutions list
                    long end = System.currentTimeMillis(); // Finds time taken
                    long runtime = (end-start); // Calculates runtime
                System.out.println("New Solution Found. Time Spent: " + (runtime)  + "ms"); // Prints time found
                }
            }else{
                Solution addable1 = new Solution(current); // Creates version 1
                Solution addable2 = new Solution(current); // Creates version 2
              if(addable1.stillPossible(true) && addable2.stillPossible(false)){ // If there are two ways for it to be expanded
                    addable1.setNext(true); // hanges to the next step
                    partialSolutions.enqueue(addable1); //Queues up new solution
                    addable2.setNext(false); // Changes to the next step
                    partialSolutions.enqueue(addable2); //Queues up new solution
                }else if (addable1.stillPossible(true)){ //If only one way, true
                    addable1.setNext(true); // make next true
                    valid = addable1.finish(); //send new one to be finished
                    if (valid){ // if finsihed is a valid solution
                        solutions.add(addable1); //move to solutons
                    }
                }else if(addable2.stillPossible(false)){// if only one way, false
                    addable2.setNext(false); //make next false
                    valid = addable2.finish(); // finishes the falsified solution
                    if (valid){ // If returned soltuion is valid
                        solutions.add(addable2); // add to solutions
                    }
                }
            }
        }
        return(solutions);
    }

    /**
     * <b>main</b> method  calls the method <b>solve</b> 
     * and then prints out the number of solutions found,
     * as well as the details of each solution.
     *
     * The <b>width</b> and <b>height</b> used by the 
     * main are passed as runtime parameters to
     * the program. If no runtime parameters are passed 
     * to the program, or if the parameters are incorrect,
     * then the default values are used.
     *
     * @param args
     *  Strings array of runtime parameters
     */
    public static void main(String[] args) {

        StudentInfo.display(); // Prints Students Information
        ArrayList<Solution> finalSolutions = new ArrayList<Solution>(); // Initialize the array for solutions
        int width; // Inputted width
        int height; // inputted width
        boolean validInput;


        if (args.length > 0){ // f arguments are inputted
            if (args.length < 2 || args.length > 2 ){ // and more or less than two have been inputted
                width = 3; //default
                height = 3; //default
            }else{ // Only two inputted
                try{//Check if they're integers
                    Integer.parseInt(args[0]);
                    width = Integer.parseInt(args[0]);
                    validInput = true;
                }catch(Exception NumberFormatException){ //default the wdith if not
                    height = 3; //defauly height to 3
                    width = 3; // deafuly width to 3
                    validInput = false;
                }
                try{
                    Integer.parseInt(args[1]); //checks height
                    if(validInput){
                        height = Integer.parseInt(args[1]); 
                    }else{
                        height = 3; //defauly height to 3
                        width = 3; // deafuly width to 3
                    }
                }catch(Exception NumberFormatException){
                    height = 3; //defauly height to 3
                    width = 3; // deafuly width to 3
                }
            }
        } else{
            width = 3; // Default
            height = 3; // Default
        }

        finalSolutions = solve(width,height); // Calls bred-schmidgt algorithm
        for (Solution current: finalSolutions){ // Goes thorugh soltuions found
            System.out.println("********");
            System.out.println(current); // prints solutions
        }
        System.out.println("Number of Solutions Found: " + finalSolutions.size()); // prints # of solutions found
    }
}