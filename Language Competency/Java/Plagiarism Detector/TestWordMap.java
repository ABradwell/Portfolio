/** 
 * A test program illustrating how the implementations of WordMap are
 * expected to be work.
 * 
 * @author Marcel Turcotte (marcel.turcotte@uottawa.ca)
 */

import java.util.Arrays;

public class TestWordMap {

    private static void testAddOneTwo(WordMap w) {
        // System.out.println(w.size());
        // System.out.println("X");
        w.update("one");
        // System.out.println(w.size());
        // System.out.println("XX");
        Utils.assertEquals(1, w.size());
        // System.out.println("XXX");
        Utils.assertTrue(w.contains("one"));
        // System.out.println("XXXX");
        Utils.assertEquals(1, w.get("one"));
        // System.out.println("O");
        w.update("two");
        // System.out.println(w.size());
        // System.out.println("OO");
        Utils.assertTrue(w.contains("two"));
        // System.out.println("OOO");
        Utils.assertEquals(1, w.get("two"));
        // System.out.println("OOOO");
        Utils.assertEquals(1, w.get("one"));
        // System.out.println("OOOOO");
        w.update("two");
        // System.out.println(w.size());
        // System.out.println("K");
        Utils.assertEquals(2, w.get("two"));
        // System.out.println("KK");
        Utils.assertEquals(1, w.get("one"));
        // System.out.println("KKK");
        w.update("one");
        // System.out.println(w.size());
        // System.out.println("J");
        Utils.assertEquals(2, w.get("one"));
        // System.out.println("JJ");
        Utils.assertFalse(w.contains("a"));
        // System.out.println("JJJ");
        Utils.assertFalse(w.contains("q"));
        // System.out.println("JJJJ");
        Utils.assertFalse(w.contains("z"));
        // System.out.println("JJJJJ");
        Utils.assertEquals(0, w.get("a"));
        // System.out.println("JJJJJJ");
        Utils.assertEquals(0, w.get("q"));
        // System.out.println("JJJJJJJ");
        Utils.assertEquals(0, w.get("z"));
        
    }

    private static void testAddFive(WordMap w) {

        String[] keys = new String[]{"charlie", "alpha", "bravo", "epoch", "delta"};

        for (String key : keys) {
            Utils.assertFalse(w.contains(key));
                       
            w.update(key);
            
            Utils.assertTrue(w.contains(key));

            Utils.assertEquals(1, w.get(key));

        }

        Arrays.sort(keys);
        Utils.assertTrue(Arrays.equals(keys, w.keys()));

    }

    private static void testABC(WordMap w) {
        w.update("B");
        w.update("B");

        Utils.assertEquals(1, w.size());
        w.update("A");

        Utils.assertEquals(2, w.size());
        w.update("C");        
        w.update("C");        
        w.update("C");        
        Utils.assertEquals(3, w.size());
        Utils.assertTrue(w.contains("A"));
        Utils.assertTrue(w.contains("B"));
        Utils.assertTrue(w.contains("C"));
        Utils.assertEquals(1, w.get("A"));
        Utils.assertEquals(2, w.get("B"));
        Utils.assertEquals(3, w.get("C"));

        String[] keys = new String[]{"A", "B", "C"};
        Utils.assertTrue(Arrays.equals(keys, w.keys()));

        Integer[] counts = new Integer[]{1, 2, 3};
        Utils.assertTrue(Arrays.equals(counts, w.counts()));

    }

    /**
     * Runs the tests.
     *
     * @param args reference to the array of values passed on the command line
     */

    public static void main(String[] args) {

        StudentInfo.display();

        if (args.length != 0) {
            System.out.println("Usage: java TestWordMap");
            return;
        }

        System.out.println("testAddOneTwo(new LinkedWordMap())");
        testAddOneTwo(new LinkedWordMap());

        System.out.println("testAddFive(new LinkedWordMap())");
        testAddFive(new LinkedWordMap());

        System.out.println("testABC(new LinkedWordMap())");
        testABC(new LinkedWordMap());

        System.out.println("testAddOneTwo(new TreeWordMap())");
        testAddOneTwo(new TreeWordMap());

        System.out.println("testAddFive(new TreeWordMap())");
        testAddFive(new TreeWordMap());
        
        System.out.println("testABC(new TreeWordMap())");
        testABC(new TreeWordMap());
    }

}
