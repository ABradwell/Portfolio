/**
 * An implementation of the interface WordMap using linked elements.
 *@author Aiden Stevenson Bradwell, University of Ottawa, based
 * off the outline of Marcel Turcotte (marcel.turcotte@uottawa.ca) University of Ottawa
 */

// Imports needed for the program
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;
import java.util.Arrays;
import java.util.Iterator;
import java.util.NoSuchElementException;


public class LinkedWordMap implements WordMap {
    private LinkedList<Set> elems;
    private int count;
    //Sets up a Pair calss between values and Keys
    public class Set {
        //Initializes pair values
        private final String key;
        private Integer value;
        //Creates new pairing
        public Set(String key, Integer value) {
            this.key = key;
            this.value = value;
        }
        //Returns Key from the pair
        public String getKey() {
            return key;
        }
        //Returns the value of the pair
        public Integer getValue() {
            return value;
        }
        //updates the value of the pair
        public void setValue(Integer value) {
            this.value = value;
        }

        //Prints the set in a readable format
        @Override
        public String toString() {
            return "(key=" + key + ",value=" + value + ")";
        }
    }
    // Creates new Linked Map
    public LinkedWordMap(){
        count = 0;
        elems = new LinkedList<Set>(); // Creates a linked list fo the set class above
    }

    /**
     * Returns the logical size of this WordMap. That is the number of
     * associations currently stored in it.
     *
     * @return the logical size of this WordMap
     */
    
    public int size() { 
        return elems.size();
    }

    /**
     * Returns true if and only if this WordMap contains the specified
     * word.
     *
     * @param key the specified word
     * @return true if and only if this WordMap contains the specified word
     * @throws NullPointerException if the value of the parameter is null
     */

    public boolean contains(String key) {
        if (key == null){ // checks if key being checked is null
            throw new NullPointerException("Invalid Number");
        }
        if (size() == 0){ // if there are no objects in the list, it cannot contian the key
              return(false);
            }
        else{// Otherwise go through list
           for (int i = 0; i < size(); i++){ // Checks through each object in the linked list
              String currentKey = elems.get(i).getKey();
              if(currentKey.equals(key)){ // Checks if the key is part of the list
                return true; // Key found
              }
            }
        }
        return false; // Key not found
    }
    
    /**
     * Returns the count associated with the specified word or 0 if
     * the word is absent.
     *
     * @param key the specified word
     * @return the count associated with the specified word or 0 if absent
     * @throws NullPointerException if the value of the parameter is null
     */
    
    public int get(String word) {
        if (word == null){ // Assures word is not null
            throw new NullPointerException("Invalid Number");
        }if(!contains(word)){ // if the word is not in the list, then the value is 0
            return 0;
        }else{// if teh word is in the list then
            for (int i = 0; i< elems.size(); i++){ // check through list
                if(elems.get(i).getKey().equals(word)){
                    return elems.get(i).getValue(); // returns value of this specific key
                }
            }
        }
        return 0; // in case contains fails
    }
    
    /**
     * Increments by 1 the counter associated with the specified
     * word. If the specified word is absent from the data structure,
     * a new association is created.
     *
     * @param key the specified word
     * @throws NullPointerException if the value of the parameter is null
     */

    public void update(String word) {        
         if (word == null){  // Null check for the key
            throw new NullPointerException("Invalid Number");
        }if(get(word) == 0){ // If there are no existing values of the word
            Set newSet = new Set(word, 1); // Create a new set for the word
            if(elems.size() == 0){ // If this is the first item
                elems.addFirst(newSet); // add to start
            }else{ // if there are already items in the list
                elems.addLast(new Set(word, 1)); // add to end
            }
        }else{  // There is already this key in the list
            for (int i = 0; i< elems.size(); i++){  // Checks each item
                if(elems.get(i).getKey().equals(word)){  // Found word
                    elems.get(i).setValue(get(word) + 1); // Increase its value of occurances
                }
            }
        }
    }
    
    /**
     * Returns all the keys (words) of this WordMap using their
     * natural order.
     *
     * @return all the keys (words)
     */
    
    public String[] keys() {
        Set[] sets = elems.toArray(new Set[elems.size()]);  // Creates a filled array of Set objects
        String[] keyValues = new String[sets.length];  // Creates an empty array of String values
        int i = 0;
        for(Set current: sets){  // Goes through every set
            keyValues[i] = current.getKey();  // Adds just the key of the set objects
            i++;
        }
        Arrays.sort(keyValues);  // Organizes the array
        return keyValues;  // returns the array/list
    }

    /**
     * Returns all the counts associated with keys in this
     * WordMap. The counts are in the same order as that of the keys
     * returned by the method keys().
     *
     * @return all the counts
     */
    
    public Integer[] counts() {
        Set[] sets = elems.toArray(new Set[elems.size()]);  // Creates a filled array of Set objects
        Integer[] countValues = new Integer[sets.length];  // Creates an empty array of Integer values
        int i = 0;
        for(Set current: sets){  // Goes through every set
            countValues[i] = current.getValue();  // Adds just the key of the set objects
            i++;
        }
        Arrays.sort(countValues);  // Organizes the array
        return countValues;  // returns the array/list
    }
}
