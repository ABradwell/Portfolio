/**
 * Rummy Game
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
public class Game{
	private Deck maindeck;
	private Deck playerhand;
	private Die die;
	private int rank;
	public Game(int ranks){
		this.rank= ranks;
		this.maindeck = new Deck(ranks);
		this.playerhand  = new Deck();
		this.die = new Die();
	}
	/*
	* method "play" contains all code for the base game loop, see below comments
	*/
	public void play(){
		// Initialize the variables including:
		// 			Scanners, ints, Strings, ArrayLists, ect
		Scanner input = new Scanner(System.in); // new scanner
		Deck newdeal = new Deck();  // new deck
		int i = 0;//temp variable
		int suit; //temp variable
		int rank;//temp variable
		int numberofmoves = 0;// overall counter
		Card removecard = new Card(0,0); // new temp card
		boolean run = true; // used for circut system
		int dealamount; // temp variable
		String playerchoice = ""; // temp variable
		boolean finalmoves = false; // temp variable
		ArrayList<String> continuechoices = new ArrayList<String>(Arrays.asList("y","n","yes","no","Y","N")); // Possible answers
		ArrayList<String> yes = new ArrayList<String>(Arrays.asList("y","Y","yes")); // Possible positive answers
		ArrayList<String> no = new ArrayList<String>(Arrays.asList("n","N","no")); // Possible neg answers

		// Begin The Actual Game
		this.maindeck.shuffle(); // Suffles original deck
		this.playerhand = this.maindeck.deal(7); // deals a set of 7 numbers from the main deck
		while (this.playerhand.size() > 0){
			numberofmoves = numberofmoves + 1; // keeps track of how amny turns have been taken
			System.out.println("Enter any value to roll die: "); // ask for user to type
			String voids = input.next(); // receives input
			if (no.contains(playerchoice) && this.maindeck.size() == 0){ // Checks for an emptty deck and no more melds
				finalmoves =true; // will always roll 1
			}else{
				this.die.roll(); // Otherwise, random roll
			}
			if (this.die.getValue() == 1  || finalmoves){ // Checks if the dice rolled a one
				if (this.playerhand.size() == 0){ // checks the player's hand is not empty
					break;
				}
				System.out.println("\n\n\n######### ROUND: "+ numberofmoves +" #########"); // Standard title print
				System.out.println("You rolled a 1");// Standard title print
				run = true;
				while(run){
					this.playerhand.print();// Standard title print
					System.out.println("You may remove any one card that you would like: ");
					System.out.println("Please enter the card suit: "); // Gets intended card's suit
					suit = input.nextInt();// receives input
					System.out.println("Please enter the card rank: "); // Gets the intended card's rank
					rank = input.nextInt();// receives input
					removecard = new Card(suit, rank);
					if (this.playerhand.contains(removecard)){
						this.playerhand.remove(removecard);
						break;
					}else {
						System.out.println("You do not have that card in your hand.");
					}
				}
				}else{
					if (this.maindeck.size()< this.die.getValue()){
						dealamount = this.maindeck.size();
					} else{
						dealamount = this.die.getValue();
					}

					newdeal = this.maindeck.deal(dealamount);
					this.playerhand.addAll(newdeal);
					run = true;
					if (this.playerhand.size() == 0){
						break;
					}
					while (run){
						if (this.playerhand.size() == 0){
							break;
						}
						System.out.println("\n\n\n######### ROUND: "+ numberofmoves +" #########");// Standard title print
						System.out.println("You rolled a " + this.die.getValue());// Standard title print
						this.playerhand.print();// Standard title print
						System.out.println("Do you have any molds you would like to discard?  (Y/N)"); // Check if player has any melds
						playerchoice = input.next(); // receives input
						if (continuechoices.contains(playerchoice)){
							if (yes.contains(playerchoice)){  //checks the player wants to continue
								System.out.println("Please choose a meld to remove."); // Standard title print
								System.out.println("How many cards are in this meld?"); // Standard request print
								int cardnumber = input.nextInt(); // receives input
								Deck meldremove = new Deck(); // initializes a deck which will be filled with the cards the user chooses
								for (int w = 0; w < cardnumber; w++){ // receive each card expected
									System.out.println("Please enter the suit (1-4):  ");// Standard request print
									int suits = input.nextInt();// receives input
									System.out.println("Please enter the rank(1-"+ this.rank + "):  ");// Standard request print
									int ranky = input.nextInt();// receives input
									Card newcard = new Card(suits,ranky); //Creates a new card with inputed data
									meldremove.add(newcard); // Adds new card to proposed meld
								}
								boolean inclusive = this.playerhand.containsAll(meldremove); // Checks that the player has each card
								boolean iskind = meldremove.isKind(); // checks either the meld is a kind
								boolean isseq = meldremove.isSeq(); // or the meld is a sequence
								if (inclusive && iskind || inclusive && isseq){ // As long as it is one of these, and the player has the cards
									this.playerhand.removeAll(meldremove); // remove the cards from the player's hand
								} else{
									System.out.println("This is not a Valid Meld"); // If they enter either a meld that isnt a meld, or that the player doesnt have.
								}
							} else{ //checks the player doesnt want to continue
								break;
							}
						}
					}
				}
			}
			System.out.println("######### Congraulations! #########"); // Standard Exit print
			System.out.println("You have completed the game in  " + numberofmoves + " turns!"); // Standard Exit print
		}
}
