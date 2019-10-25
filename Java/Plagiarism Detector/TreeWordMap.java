/**
 * A Binary Search Tree implementation of the interface WordMap.
 *
 * @author Marcel Turcotte (marcel.turcotte@uottawa.ca)
 */

public class TreeWordMap implements WordMap {

    private static class Elem {

        private String key;
        private int count;
        private Elem left, right;

        private Elem(String key) {
            this.key = key;
            count = 1;
        }

    }

    private Elem root;
    private int size;

    /**
     * Returns true if and only if this WordMap contains the specified
     * word.
     *
     * @param key the specified word
     * @return true if and only if this WordMap contains the specified key
     * @throws NullPointerException if the value of the parameter is null
     */
    
    public boolean contains(String key) {

        if (key == null) {
            throw new NullPointerException();
        }
        boolean found = false;
        Elem current = root;
        while (! found && current != null) {
            int test = key.compareTo(current.key);
            if (test == 0) {
                found = true;
            } else if (test < 0) {
                current = current.left;
            } else {
                current = current.right;
            }
        }
        return found;
    }
    
    /**
     * Increments by 1 the counter associated with the specified
     * word. If the specified word is absent from the data structure,
     * a new association is created.
     *
     * @param key the specified word
     * @throws NullPointerException if the value of the parameter is null
     */
    
    public void update(String key) {
        Elem current = root; // initialize the scanner
        if (key == null) { // Null check
            throw new NullPointerException();
        }
        if(current == null){ // if the current list has no value, then the list is empty
            root = new Elem(key); // adds first node to the tree
            size++; 
            return; //break from method
        }
        if(!contains(key)){  // Checsk if there is a node exisiting of this key value
            boolean finished = false; // If not, it begins to find the placement of this new node
            while(!finished){ // Until the node is placed
                int test = key.compareTo(current.key); // finds if the new key is > or < than the current node
                if (test < 0){ // found to be less than
                    if(current.left == null){ // if there is not already a ndoe less than the current
                        current.left = new Elem(key); //add this to that left position
                        finished = true; // break from the loop
                        size++;
                    }else{
                        current = current.left;  //Otherwise the new node to check becomes the now below to the left
                    }
                }else{  // If the new key is greater than te current node being checked
                    if(current.right == null){  // If there is not already a node reater than this one being checked
                        current.right = new Elem(key);   // Create new Node
                        finished = true; // break;
                        size++;
                    }else{
                        current = current.right; // the new node to be checked is below to the right
                    }
                }
            }
        }else{ // There is already a node with the new key in the tree
            boolean finished = false; 
            while(!finished){ // until that node is found
                int test = key.compareTo(current.key); // same as above test
                if ( test == 0){ // Same key value found
                    current.count++;
                    finished = true; // Break
                } else if (test < 0){ // Value less than current
                    if(current.left == null){ // just in contains runs wrong
                        current.left = new Elem(key);
                        size++;
                        finished = true;
                    }else{ // check next left below node
                        current = current.left;
                    }
                }else{ // Going t the right branch of ndoe
                    if(current.right == null){ // In case contains ran wrong
                        current.right = new Elem(key);
                        size++;
                        finished = true;
                    }else{ // check next right
                        current = current.right;
                    }
                }
            }
        }
    }
    
    /**
     * Returns the count associated with the specified word or 0 if
     * the word is absent.
     *
     * @param key the specified word
     * @return the count associated with the specified word or 0 if absent
     * @throws NullPointerException if the value of the parameter is null
     */
    
    public int get(String key) {

        if (key == null) { // Null check for key value
            throw new NullPointerException();
        }
        
        boolean found = false;
        Elem current = root;  // initializes checker
        while (current != null) {  // While the tree has more nodes to continue down
            int test = key.compareTo(current.key);  // Checks parameter vs current Node
            if (test == 0) {  //Same node found
                return current.count;  //return value of this node
            } else if (test < 0) {  // check left
                current = current.left;  
            } else {  // check right
                current = current.right;  
            }
        }

        return 0;  // No node found, returning 0
    }
    
    /**
     * Returns the logical size of this WordMap. That is the number of
     * associations currently stored in it.
     *
     * @return the logical size of this WordMap
     */
    
    public int size() {
        return size;
    }
    
    /**
     * Returns all the keys (words) of this WordMap using their
     * natural order.
     *
     * @return all the keys (words)
     */
    public String[] keys() {
        String[] list = new String[size()]; // Initiailizes the String array of keys for the tree
        Elem current = root;
        list = orderedStr(current, list);  // Send into recursive loop
        return list;  // Return list
        } 
    /**
     * Returns all the counts associated with keys in this
     * WordMap. The counts are in the same order as that of the keys
     * returned by the method keys().
     *
     * @return all the counts
     */
    
    public Integer[] counts() {
        Integer[] list = new Integer[size()];  // Initiailizes the Int array of keys for the tree
        Elem current = root;
        list = orderedInt(current, list);  // Sends list into recursive loop
        return list; // Return list
    }


    public String[] orderedStr(Elem current, String[] list){
        if(current != null){  // As long as there isnt a null value passed, so we dont overextend past the bottom of the tree
            list = orderedStr( current.left, list);  // Go left as long as there is left to go
            list = addToStringList(list, current.key);  // Found farthest left Node
            list = orderedStr( current.right, list);  // Goes right and continue the loop
        }
        return list;  // Sends the list back a level, or to the Key method
    }

    public Integer[] orderedInt(Elem current, Integer[] list){

        if(current != null){  // As long as there isnt a null value passed, so we dont overextend past the bottom of the tree
            list = orderedInt( current.left,list);  // Go left as long as there is a node to the left
            list = addToIntegerList(list, current.count);  // Farthest left found, now adding to array
            list = orderedInt( current.right,list);  // Going right, and repeat the loop
        }
        return list;  // return the List back a evel, or the the counts method
    }

    public String[] addToStringList(String[] stringList, String key){
        for(int i = 0; i< stringList.length; i++){ //Begin going through array
            if(stringList[i] == null){ // finds frst empty slot
                stringList[i] = key; // adds key to this slot
                break;
            }
        }
        return stringList;
    }
    public Integer[] addToIntegerList(Integer[] integerList, Integer value){
        for(int i = 0; i< integerList.length; i++){  // Begins going through the array
            if(integerList[i] == null){  // Finds first null value
                integerList[i] = value;  // adds the value to this slot
                break;
            }
        }
        return integerList;
    }

}
