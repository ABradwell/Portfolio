import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.Color;

/**
 * The class <b>GameView</b> provides the current view of the entire Game. It extends
 * <b>JFrame</b> and lays out a matrix of <b>GridButton</b> (the actual game) and 
 * two instances of JButton. The action listener for the buttons is the controller.
 *
 * @author  * @author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline of Guy-Vincent Jourdan, University of Ottawa
 */

public class GameView extends JFrame {

    private JLabel input;
    private GameModel gameModel;
    private GameController gameController;
    private JPanel buttons;
    private JPanel buttonHolder;
    private GridButton[][] buttonGrid;
    /**
     * Constructor used for initializing the Frame
     * 
     * @param gameModel
     *            the model of the game (already initialized)
     * @param gameController
     *            the controller
     */

    public GameView(GameModel gameModel, GameController gameController) {
        
    	setTitle("Lights Out Game by Aiden Bradwell");
    	setSize(1000,1000);
    	setLocationRelativeTo(null);
    	buttonGrid = new GridButton[gameModel.getHeight()][gameModel.getWidth()];

        
        this.gameModel = gameModel;
        this.gameController = gameController;
        buttonHolder = new JPanel();
        buttons = new JPanel();

        setLayout (new BorderLayout());
        buttons.setLayout (new GridLayout(gameModel.getHeight(),gameModel.getWidth()));
        buttonHolder.setLayout(new GridLayout(4,1));
        
        JButton reset = new JButton("RESET");
        JButton quit = new JButton("QUIT");
        JCheckBox showSolution = new JCheckBox("SOLUTION");
        JButton randomize = new JButton("RANDOMIZE");
        
        showSolution.setSelected(false);

        reset.addActionListener(gameController);
        quit.addActionListener(gameController);
        showSolution.addItemListener(gameController);
        randomize.addActionListener(gameController);

        
        for (int i = 0; i < gameModel.getHeight(); i++){
            for (int o = 0; o < gameModel.getWidth(); o++){
            	GridButton newbutton = new GridButton(o,i);
            	newbutton.addActionListener(gameController);
                buttons.add(newbutton);
                buttonGrid[i][o] = newbutton;
            }
        }

        buttonHolder.add(reset);
        buttonHolder.add(randomize);
        buttonHolder.add(showSolution);
        buttonHolder.add(quit);

        reset.setBackground(Color.WHITE);
        quit.setBackground(Color.WHITE);
        randomize.setBackground(Color.WHITE);
        add(buttons, BorderLayout.CENTER);
        add(buttonHolder, BorderLayout.EAST);
        pack();


        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        setVisible(true);
        
        

    }

    /**
     * updates the status of the board's GridButton instances based 
     * on the current game model, then redraws the view
     */

    public void update(){
        for (int i = 0; i < gameModel.getHeight(); i++){
            for (int o = 0; o < gameModel.getWidth(); o++){
            		GridButton currentButton = buttonGrid[i][o];
            		if (gameController.displaySolution){
            			currentButton.setState(gameModel.isON(i,o), gameModel.solutionSelects(i,o));
            		}
            		else{
            			currentButton.setState(gameModel.isON(i,o), false);
            		}
            	}
            }
        } 

    /**
     * returns true if the ``solution'' checkbox
     * is checked
     *
     * @return the status of the ``solution'' checkbox
     */

    public boolean solutionShown(){

        return false;

    }

}
