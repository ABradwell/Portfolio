import javax.swing.JFrame;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Gui extends JFrame{

	public Gui(){
		super("Move It!");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setLayout (new BorderLayout());
		DisplayArea displayArea = new DisplayArea();
		add(displayArea, BorderLayout.CENTER);
		JPanel jpanel = new JPanel();
		jpanel.setBackground(Color.WHITE);
		JButton left = new JButton("Left");
		left.addActionListener(displayArea);
		jpanel.add(left);
		JButton right= new JButton("Right");
		right.addActionListener(displayArea);
		jpanel.add(right);
		JButton up = new JButton("Up");
		up.addActionListener(displayArea);
		jpanel.add(up);
		JButton down= new JButton("Down");
		down.addActionListener(displayArea);
		jpanel.add(down);

		add(jpanel,BorderLayout.PAGE_END );
		setResizable(false);
		pack();
	}
	public static void main(String[] args){
		Gui gui = new Gui();
		gui.setVisible(true);

	}
}