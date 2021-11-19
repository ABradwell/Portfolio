/**
 * An objet that reads and stores the content of file. It posses a
 * method that returns an iterator on the content (a String).
 *
 * 
 *@author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline of Marcel Turcotte (marcel.turcotte@uottawa.ca) University of Ottawa
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class WordReader {

    public class NewIterator<J> extends LinkedList<J> implements Iterator<J>{  // Creates a new iterator class for the program
        private int size;  // The size of the iterators stored sections
        private int index;  // The search index
        private int arrSize;  // The size of the array, use for calculations
        public NewIterator(int size){
            super(); // creates iterator
            this.index = 0; // Intiilizes variables
            this.size = size;     
            this.arrSize = content.length() - size; // Used for calculations
        }
        public boolean hasNext(){
            if (index > arrSize){
                return false;
            }
            return true;
        }
        public J next(){
            int temp = index;
            index++;
            return get(temp);

        }
        public Iterator<J> iterator(){
            return this;
        }
    }
    // The content of the file that was read
    
    private String content;

    /**
     * When an object of the class WordReader is created, this
     * constructor reads the content the file specified by the
     * parameter fileName.
     *
     * @param fileName the specified file
     * @throws FileNotFoundException if the file could not be found
     * @throws IOException if there is an error reading the content of the file
     */
    
    public WordReader(String fileName) throws FileNotFoundException, IOException {
        this(fileName, true);
    }
    
    /**
     * When an object of the class WordReader is created, this
     * constructor reads the content the file specified by the
     * parameter fileName.
     *
     * @param fileName the specified file
     * @param caseSensitive if the value is false, the content is transformed to lower case letters
     * @throws FileNotFoundException if the file could not be found
     * @throws IOException if there is an error reading the content of the file
     */
    
    public WordReader(String fileName, boolean caseSensitive) throws FileNotFoundException, IOException {

        BufferedReader reader;
        reader = new BufferedReader(new FileReader(fileName));

        StringBuilder buffer;
        buffer = new StringBuilder();

        String line;

        while ((line = reader.readLine()) != null) {
            if (! caseSensitive) {
                line = line.toLowerCase();
            }
            buffer.append(line);
        }
        
        reader.close();

        content = buffer.toString();
    }

    /**
     * Removes all the blank spaces from the content of the text.
     */
    
    public void removeAllBlankCharacters() {
        content = content.replaceAll("\\p{Blank}","");
    }

    /**
     * Returns an iterator over the content in the text.
     *
     * @param size the size of the n-grams to be returned by the method of the iterator
     * @return an iterator over the content in the text
     */
    

    public Iterator<String> iterator(int size) { 
            NewIterator listy = new NewIterator<String>(size); // Creates a new Iterator using my class defined in te beginning
            int arrSize = content.length() - size; // Creates the size of the array needed for calculations
            for(int i = 0; i <= arrSize; i++){ // Goes through the text
                String currentSegment = ""; // Cretes blank string
                for (int o = i; o < i + size; o++){//Creates a segment of length size
                    currentSegment = (currentSegment + content.charAt(o)); // Adds a letter for each (size) slot
                }
                listy.add(i,currentSegment); // Add segment to iterator
            }
            Iterator<String> returnThis = listy.iterator(); // Creates actual iterator value|| works as type casting
            return returnThis; // Return to called program
    }

}
