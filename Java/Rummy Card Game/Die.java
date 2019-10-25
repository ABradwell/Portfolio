// Author: Aiden Stevenson Bradwell, Winston Barrett-Hogg
// Student number: 300064655, 300087985
// Course: ITI 1121-C
// Assignment: 1
// Question: 4
//Class: Die
import java.util.Random;
import java.util.ArrayList;
import java.util.*;
import java.util.Random;
import java.util.Scanner;
public class Die{
	Random rando = new Random();
	private int roll;							//integer representing a roll on a dice
	private int maxvalue = 6;			/*integer representing the maximum value of a
																	roll on a dice, in this case 6 */

	/**
	*	constructor method Die "rolls" the dice when the object is created
	* generating a random number between 0-5 and adding 1 to it
	*/
	public Die(){
		this.roll = rando.nextInt(5) +1;
	}

	/**
	* method getValue returns the value of the private integer "roll"
	*
	* @return				value of "this.roll"
	*/
	public int getValue(){
		return (roll);
	}

	/**
	* method roll generates a random number between 0-5, adds 1 to it, and
	* sets roll to equal this value
	*/
	public void roll(){
		this.roll = rando.nextInt(5) +1;
	}

	/**
	* method toString prints the value of the roll variable
	*/
	public String toString(){
		return("You Rolled a " + this.roll);
	}
}
