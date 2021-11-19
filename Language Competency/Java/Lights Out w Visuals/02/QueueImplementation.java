/**
 *
 * @author  * @author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline of Guy-Vincent Jourdan, University of Ottawa
 */
import java.util.ArrayList;
public class QueueImplementation<E> implements Queue<E> {

	public ArrayList<E> queue;
	public QueueImplementation(){
		queue = new ArrayList<E>();
	}
	public void enqueue(E element){
		this.queue.add(element);
	}
	public E dequeue(){
		E copy = this.queue.remove(0);
		return(copy);
	}
	public boolean isEmpty(){
		return(this.queue.size() == 0);
	}
}
