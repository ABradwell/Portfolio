/*  CSI2114 Lab 3 - lab3.java
 *  
 *  Class to check balanced brackets in math expressions  
 *
 *  Usage: java bracketsBalance <exp>
 *  
 *  by Jeff Souza
 *
 */

class bracketsBalance {

    private boolean bBalance (String exp){ 

        ArrayStack open = new ArrayStack();
        ArrayStack nonBracks = new ArrayStack();
        String opening = "({[";
        String closing = ")}]";
        for(int i = 0; i < exp.length(); i++){
            if(opening.indexOf(exp.charAt(i)) != -1){
                open.push(exp.charAt(i));
            }else if(closing.indexOf(exp.charAt(i)) != -1){
                if(open.size() == 0){
                    return false;
                }
                if (closing.indexOf(exp.charAt(i)) != opening.indexOf((char) open.pop())){
                    return false;
                }
            }
        }
        return open.isEmpty();
    }

    public static void main(String[] args) {

        bracketsBalance b = new bracketsBalance();
        boolean result = b.bBalance(args[0]);
   
        if (result) System.out.println("The expression is balanced."); 
        else        System.out.println("The expression is NOT balanced."); 
    }
}