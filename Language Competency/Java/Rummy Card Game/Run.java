/**
 * The class Run provides a main method for the rummy application.
 *
 * @author Marcel Turcotte@uottawa.ca
 */


public class Run {

    /**
    * method Main contains the main execution for the game
    *
    * @param    args    main arguments
    */
    public static void main(String[] args) {

        Game game;                    //object of type Game, see Game.java
        boolean play, changeSize;     /*main game loop flag, and whether
                                        the player wishes to change the
                                        size of the deck */
        int ranks;                    //number of ranks in the Deck

        StudentInfo.display();

        System.out.println("Welcome to Single Player Rummy with Dice and strange deck.");
        System.out.println();

        System.out.println("The standard deck  has 52 cards: 13 ranks times 4 suits");
        changeSize = Utils.readYesOrNo("Would you like to change the number of cards by changing the number of ranks? ");

        if (changeSize) {
            ranks = Utils.readNumber("Enter a value for the number of ranks: ", 3, 99);
        } else {
            ranks = 13;
        }

        play = true;

        while (play) {
            game = new Game(ranks);
            game.play();
            play = Utils.readYesOrNo("Do you want to again? ");
        }

    }

}
