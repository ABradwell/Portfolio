/**
 * Dice for Rummy Game
 * @author Aiden Stevenson Bradwell
 * Feburary 1st, 2019
 * Course: ITI 1121-C
 * 300064655
 * abrad060@uottawa.ca
 * 
 */ 
import java.util.Random;
import java.util.ArrayList;
import java.util.*;
import java.util.Random;
import java.util.Scanner;
public class Card{
	private int rank;									//represents rank (0-12) of given card
	private int suit;								  //represents suit (0-4)
	public static int DIAMOND = 0;		//number -> suit representation
	public static int CLUB = 1;
	public static int HEART = 2;
	public static int SPADE = 3;
	public Card(int suit, int rank){
		this.rank = rank;
		this.suit = suit;
	}
	public int getRank(){
		return(this.rank);
	}

	/**
	*	method getSuit returns the suit of a given card Object
	*
	* @return				the suit of the referenced card object
	*/
	public int getSuit(){
		return(this.suit);
	}

	/**
	* method equals takes an object of any type and, if it is type card, returns
	* boolean true if it is of equivelent suit and rank to the calling card Object
	*
	* @param	object	object of any type
	* @return					boolean true if object is of type card and is
	*									equivelent to calling card object
	*/
	public boolean equals(Object object){
		if(!(object instanceof Card)){
			return(false);
		}
		Card other;
		other = (Card) object;
		if (this.suit == other.getSuit() && this.rank == other.getRank()){
			return(true);
		}else{
			return(false);
		}
	}
	
	/**
	* method toString returns a string representation of the calling card Object
	*/
	public String toString(){
		return("(" + this.suit + ", " + this.rank + ")");
	}
}
