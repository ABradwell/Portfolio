import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class GraphicalView extends JFrame implements View {
	private JLabel input;
	private Timer model;
	public GraphicalView (Timer model, Controller controller) {
		setLayout (new GridLayout(2, 3));
		this.model = model; 
		JButton incrementHours = new JButton("IncrementHours");
		incrementHours.addActionListener(controller);
		add(incrementHours);
		JButton incrementMinutes = new JButton("IncrementMinutes");
		incrementMinutes.addActionListener(controller);
		add(incrementMinutes);
		JButton incrementSeconds= new JButton("IncrementSeconds");
		incrementSeconds.addActionListener(controller);
		add(incrementSeconds);
		JButton decreaseHours	= new JButton("DecrementHours");
		decreaseHours.addActionListener(controller);
		add(decreaseHours);
		JButton decreaseMinutes = new JButton("DecrementMinutes");
		decreaseMinutes.addActionListener(controller);
		add(decreaseMinutes);
		JButton decreaseSeconds = new JButton("DecrementSeconds");
		decreaseSeconds.addActionListener(controller);
		add(decreaseSeconds);
		input = new JLabel();
		add(input);


		//setup
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(700, 100);

		//display the window
		setVisible(true);
	}
	public void update () {
	input.setText(model.toString());
}
}
