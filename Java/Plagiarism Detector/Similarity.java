 /**
 *
 * A nn interface for the Plagerism detector
 * 
 * @author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline of Guy-Vincent Jourdan, University of Ottawa
 */

public interface Similarity{
	double score(WordMap a, WordMap b); // A model to check the sililartities between the two WordMaps
}