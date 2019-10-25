import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class DisplayArea extends JPanel implements ActionListener{

	private static final int DISPLAY_SIZE = 600;
	private Point point;
	public DisplayArea(){
		super();
		setBackground(Color.WHITE);
		Dimension display = getPreferredSize();
		setSize(display);
		 this.point = new Point(getSize().width/2, getSize().height/2);

	}
	public Dimension getPreferredSize(){
		Dimension returned = new Dimension(DISPLAY_SIZE, DISPLAY_SIZE);
		return returned;
	}
	
	//@SuppressWarnings ("unchecked")
	@Override
	public void actionPerformed ( ActionEvent e ) {
		if ( e.getActionCommand().equals("Left")){
			point.setLocation(point.getX() - 10, point.getY());
			repaint();
		}
		if ( e.getActionCommand().equals("Right")){
			point.setLocation(point.getX() + 10, point.getY());
			repaint();

		}
		if ( e.getActionCommand().equals("Up")){
			point.setLocation(point.getX(), point.getY() - 10);
			repaint();
		}
		if ( e.getActionCommand().equals("Down")){
			point.setLocation(point.getX(), point.getY() + 10);
			repaint();
		}
	}
	@Override
	public void paint(Graphics g){
		super.paint(g);
		g.drawOval((int)point.getX(),(int)point.getY(), 10,10);
		g.setColor(Color.BLACK);


	}
}