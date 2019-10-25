import java.util.ArrayList;


/**
 * The class <b>LightsOut</b> launches the game
 *
 * @author  * @author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline of Guy-Vincent Jourdan, University of Ottawa
 */
public class LightsOut {


     /**
     * default width of the game.
     */
    public static final int DEFAULT_WIDTH = 8;
     /**
     * default height of the game.
     */
    public static final int DEFAULT_HEIGTH = 5;

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
     * This version does not continue exploring a 
     * partial solution that is known to be
     * impossible. It will also attempt to complete
     * a solution as soon as possible
     *
     * During the computation of the solution, the 
     * method prints out a message each time a new 
     * solution  is found, along with the total time 
     * it took (in milliseconds) to find that solution.
     *
     * @param model
     * A game model sent over from the application
     * @return
     *  an instance of <b>ArrayList&lt;Solution&gt;</b>
     * containing all the solutions
     */
    public static ArrayList<Solution> solve (GameModel model){
        //Initialize the array and the queue
        Queue<Solution> partialSolutions = new QueueImplementation<Solution>();
        ArrayList<Solution> solutions  = new ArrayList<Solution>();
        //Initialize over parts of code
        Solution blank = new Solution(model.getWidth(), model.getHeight()); // new blank solution
        partialSolutions.enqueue(blank); // queues balnk solution
        long start = System.currentTimeMillis(); // for timing purposes
        //Begin algortihm
        while(!(partialSolutions.isEmpty())){ //As long as all soltuions have not yet been checked
            Solution current = partialSolutions.dequeue(); // Take the current soltuion work is to be done to
            if (current.isReady()){ // If the array is fully defined
                if(current.isSuccessful(model)){ // If the array is sucessful
                    solutions.add(current); // Add to the solutions list
                    long end = System.currentTimeMillis(); // Finds time taken
                    long runtime = (end-start); // Calculates runtime
                    System.out.println("New Solution Found. Time Spent: " + (runtime)  + "ms"); // Prints time found
                }
            }else{
                Solution addable1 = new Solution(current); // Creates version 1
                Solution addable2 = new Solution(current); // Creates version 2
                if(addable1.stillPossible(true, model)){ // If true add is an option
                    addable1.setNext(true); // Add true to solution
                    partialSolutions.enqueue(addable1); //requeue
                }
                if(addable2.stillPossible(false, model)){ // If false add is an option
                    addable2.setNext(false); // Add false to solution
                    partialSolutions.enqueue(addable2);  //requeue
                }
            }
        }
        return(solutions); // returns valid solutions
    }

    /**
     * The method <b>solve</b> finds  the shortest 
     * solution to the <b>Lights Out</b> game 
     * for an given model board 
     * of size <b>widthxheight</b>, using a  
     * Breadth-First Search algorithm. 
     *
     * During the computation of the solution, the 
     * method prints out a message each time a new 
     * solution  is found, along with the total time 
     * it took (in milliseconds) to find that solution.
     *
     * @param model
     * The model of a game sent from the application
     * @return
     *  an instance of <b>ArrayList&lt;Solution&gt;</b>
     * containing the shortest solution
     */
    public static Solution solveShortest(GameModel model){
        ArrayList<Solution> possible = solve(model);
        int smallestSize = 0;
        Solution smallest = new Solution(model.getWidth(), model.getHeight());
        if (possible.size() > 0){
            smallest = possible.get(0);
            if (possible.size() > 1){
                for (Solution current: possible){
                    if (current.getSize() < smallest.getSize()){
                        smallest = new Solution(current);
                    }
                }
            }
        }
        return smallest;
    }


    
   /**
     * <b>main</b> of the application. Creates the instance of  GameController 
     * and starts the game. If two parameters width and height
     * are passed, they are used. 
     * Otherwise, a default value is used. Defaults values are also
     * used if the paramters are too small (less than 1).
     * 
     * @param args
     *            command line parameters
     */
     public static void main(String[] args) {
        int width   = DEFAULT_WIDTH;
        int height  = DEFAULT_HEIGTH;
 
        StudentInfo.display();

        if (args.length == 2) {
            try{
                width = Integer.parseInt(args[0]);
                if(width<1){
                    System.out.println("Invalid argument, using default...");
                    width = DEFAULT_WIDTH;
                }
                height = Integer.parseInt(args[1]);
                if(height<1){
                    System.out.println("Invalid argument, using default...");
                    height = DEFAULT_HEIGTH;
                }
            } catch(NumberFormatException e){
                System.out.println("Invalid argument, using default...");
                width   = DEFAULT_WIDTH;
                height  = DEFAULT_HEIGTH;
            }
        }
        GameController game = new GameController(width, height);
    }


}
