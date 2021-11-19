/**
 *
 * @author  * @author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline of Guy-Vincent Jourdan, University of Ottawa
 */

import java.util.ArrayList;
public interface Queue<E> {
 	
 	public abstract void enqueue(E element);
 	public abstract E dequeue();
 	public abstract boolean isEmpty();

}
