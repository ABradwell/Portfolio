import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;
import java.util.ArrayList;
import javax.swing.*; 
import java.util.Random;

/**
 * The class <b>GameController</b> is the controller of the game. It is a listener
 * of the view, and has a method <b>play</b> which computes the next
 * step of the game, and  updates model and view.
 *
 * @author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline of Guy-Vincent Jourdan, University of Ottawa
 */




public class GameController implements ActionListener, ItemListener {
	public boolean displaySolution;
    private int width;
    private int height;
    private GameView view;
    private GameModel model;
 


    /**
     * Constructor used for initializing the controller. It creates the game's view 
     * and the game's model instances
     * 
     * @param width
     *            the width of the board on which the game will be played
     * @param height
     *            the height of the board on which the game will be played
     */
    public GameController(int width, int height) {
    	displaySolution = false;
        this.width = width;
        this.height = height;
        this.model = new GameModel(width, height);
        this.view = new GameView(model, this);
    }


    /**
     * Callback used when the user clicks a button (reset, 
     * random or quit)
     *
     * @param e
     *            the ActionEvent
     */

    public void actionPerformed(ActionEvent e) {
        if(e.getActionCommand().equals("RESET")) {
            model.reset();
            view.update();
        }

        if(e.getActionCommand().equals("RANDOMIZE")) {
            model.randomize();
            view.update();
        }

        if(e.getActionCommand().equals("QUIT")) {
            view.setVisible(false);
            view.dispose();
            System.exit(0);
        }
        if(e.getSource() instanceof GridButton){
            GridButton clicked = (GridButton) e.getSource();
            model.click(clicked.getColumn(),clicked.getRow());
            if(displaySolution){
        	   model.setSolution();
            }
            view.update();
        }
        if (model.isFinished()){
            String[] options = { "Play Again", "Quit"};
            int choice = JOptionPane.showOptionDialog(null, "You have finsihed the game in " + model.getNumberOfSteps() +" clicks. Would you like to play again? ","Congragulations", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, options, options[0]);
            if (choice == 0){
                String[] resetOptions = {Integer.toString(model.getWidth()), Integer.toString(model.getHeight())};
                LightsOut.main(resetOptions);
            }else{
                System.exit(0);
            }
        }
    }

    /**
     * Callback used when the user select/unselects
     * a checkbox
     *
     * @param e
     *            the ItemEvent
     */

    public void  itemStateChanged(ItemEvent e){
    	if (e.getStateChange() == ItemEvent.SELECTED){
    		displaySolution = true;
            model.setSolution();
    	}else{
    		displaySolution = false;
    	}
    	view.update();
    }

}
