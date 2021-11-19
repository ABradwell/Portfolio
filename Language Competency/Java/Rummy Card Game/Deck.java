/**
 * Deck for Rummy Game
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
public class Deck{
	private ArrayList<Card> deck; //an ArrayList of type Card (a Deck)

	/**
	* constructor method Deck takes an input ranks, representing the number
	* of ranks to include in the deck. Then it fills the deck with cards
	*
	* @param		ranks		int representing the number of ranks in the deck
	*/
	public Deck(){
		this.deck = new ArrayList<Card>();
	}
	public Deck(int ranks){
		 Card newcard = new Card(0,0);
		 this.deck = new ArrayList<Card>();

		 for (int o = 0; o<4;o++){
			for (int j =0; j < ranks; j++){
				newcard = new Card(o,j);
				this.deck.add(newcard);
			}
		}
	}

	/**
	* method size returns as int the current size of the deck
	*
	* @return					current size of deck as type integer
	*/
	public int size(){
		return(this.deck.size());
	}

	/**
	* method hasCards returns boolean true if the size of the deck is greater
	* than zero
	*
	* @return				true if deck size is >0, false otherwise
	*/
	public boolean hasCards(){
		return (this.deck.size() > 0);
	}

	/**
	* method get takes an integer representing a position in the Deck
	* and returns the value of the card at this position
	*
	* @param		pos		integer represnting the position in the Deck
	* @return					value of the card (suit,rank) at position pos
	*/
	public Card get(int pos){
		Card returncard;
		returncard = this.deck.get(pos);
		return (returncard);
	}

	/**
	* method add adds an object of type card to the Deck
	*
	* @param		card		object of type card to be added to the Deck
	*/
	public void add(Card card){
		this.deck.add(card);
	}

	/**
	* method addAll takes all the card objects out of another deck and adds
	* them to the calling deck object
	*
	* @param		other		represents a different deck object
	*/
	public void addAll(Deck other){
		for (int i = 0; i < other.deck.size(); i++){
			this.deck.add(other.deck.get(i));
			other.deck.remove(i);
		}
	}

	/**
	* method removeLast removes from the deck the card at the "bottom" or at the
	* highest position, and returns it as a card object
	*
	* @return				card object at highest position in calling deck
	*/
	public Card removeLast(){
		Card returncard = this.deck.get(this.deck.size() -1);
		this.deck.remove(this.deck.size() -1);
		return (returncard);
	}

	/**
	* method removeFirst removes from the deck the card at the "top or at the
	* lowest position, and returns it as a card object
	*
	* @return				card object at lowest position in calling deck
	*/
	public Card removeFirst(){
		Card returncard = this.deck.get(0);
		this.deck.remove(0);
		return(returncard);
	}

	/**
	* method takes as input a card object, looks for it in the deck, removes
	* it if present, and returns true if successful or false otherwise
	*
	* @param		card		object of type card to be removed from calling deck
	* @return						boolean True if removal was successful or false otherwise
	*/
	public boolean remove(Card card){
		int i = 0;
			for (Card search:this.deck){
				if (search.equals(card)){
					this.deck.remove(i);
					return(true);
				}
				i++;
			}
			return(false);
		}

	/**
	* method removeAll takse as input a deck object and removes all cards from
	* the calling deck that match the rank and suit of any card in the other Deck
	*
	* @param		other		object of type Deck to match against cards in calling Deck
	*/
	public void removeAll(Deck other){
		int i;
		for (Card card:other.deck){
			i =0;
			for (Card searchy:this.deck){
				if (searchy.getRank() == card.getRank() && searchy.getSuit() == card.getSuit()){
					this.deck.remove(i);
					break;
					}
					i = i+1;
			}
		}
	}

	/**
	* method shuffle Shuffles the calling deck object
	*/
	public void shuffle(){
		Collections.shuffle(this.deck);
	}

	/**
	* method deal creates or 'deals' a new deck object of length n and returns it
	*
	* @param		n		integer representing number of cards to deal
	* @return				object of type deck, dealt following above rules
	*/
	public Deck deal(int n){
		Deck newdeck = new Deck();
		for (int i = 0; i < n; i++){
			newdeck.add(this.deck.get(this.deck.size() - 1));
			this.deck.remove(this.deck.size()-1);
		}
		return (newdeck);
	}
	/**
	* method contains takes an object of type card and returns true if the given
	* card object is contained in the calling deck, and false otherwise
	*
	* @param		card		object of type card
	* @return 					boolean true if card is found in calling deck,
	*										false otherwise
	*/
	public boolean contains(Card card){
		return(this.deck.contains(card));
	}

	/**
	* method contains all takes another object of type deck and returns true
	* if the calling deck contains all card objects of the given deck
	*
	* @param		other		other deck object to check containing cards
	* @return						boolean true if all cards in other are found in calling
	*									  deck, false otherwise
	*/
	public boolean containsAll(Deck other){
		boolean allin;
		for (Card card:other.deck){
			allin = this.deck.contains(card);
			if (allin == false){
				return (false);
			}
		}
		return (true);
	}

	/**
	* method isKind returns true if cards are in a sequence of the same suit
	*
	* @return				Boolean true if cards are in suit sequence
	*/
	public boolean isKind(){
		boolean good = true;
		if (this.deck.size() > 1){
			for (int i = 0; i< this.deck.size() -1; i++){
			if (this.deck.get(i).getSuit() == this.deck.get(i+1).getSuit()){
					return(false);
				}else{
					good = true;
				}
			}
			for(int o = 0;o < this.deck.size()-1; o++){
				int int1 = this.deck.get(o).getRank();
				int int2 = this.deck.get(o+1).getRank();
				if (int1 == int2){
					return(true);
				}else{
					return(false);
				}
			}
		}else{
			return(false);
		}
		return(good);
	}

	/**
	* method isSeq returns true if cards are in a sequence of the same rank
	*
	* @return				Boolean true if cards are in rank sequence
	*/
	public boolean isSeq(){
		if (this.deck.size() > 2){
			for (int o = 0; o < this.deck.size()-1 ; o++){
				if (this.deck.get(o).getSuit() != this.deck.get(o+1).getSuit()){
					return(false);
				}
			}
			for (int i = 0; i< this.deck.size() -1; i++){
				if(this.deck.get(i+1).getRank() != this.deck.get(i).getRank() + 1){
					return(false);
				}
			}
		return(true);
		}
		return(false);
	}

	/**
	* method sortBySuit sorts the calling deck in order of suit, in the order of
	* Spade>Heart>Club>Diamond
	*/
	public void sortBySuit(){
		ArrayList<Integer> combine = new ArrayList<Integer>();
		for (Card card:this.deck){
			combine.add(card.getSuit() * 100 + card.getRank());
		}
		Card tempcard = new Card(0,0);
		int tempcombine = 0;
		for (int o = 0; o < this.deck.size() - 1; o++){
			for (int i = 0; i < this.deck.size() - 1; i++){
				if (combine.get(i) > combine.get(i + 1)){
					tempcard = this.deck.get(i);
					this.deck.set(i,this.deck.get(i+1));
					this.deck.set(i+1,tempcard);
					tempcombine = combine.get(i);
					combine.set(i, combine.get(i+1));
					combine.set(i+1, tempcombine);
				}
			}
		}
	}

	/**
	* method sortByRank sorts the calling deck in order of suit, in the order of
	* 0-12
	*/
	public void sortByRank(){
		Card tempy = new Card(0,0);
		for (int o = 0; o < this.deck.size() - 1; o++){
			for (int i = 0; i < this.deck.size() - 1; i++){
				if (this.deck.get(i).getRank() > this.deck.get(i+1).getRank()){
					tempy = this.deck.get(i);
					this.deck.set(i, this.deck.get(i+1));
					this.deck.set(i+1,tempy);
				}
			}
		}
	}

	/**
	* method print displays to the user their "hand", or the calling deck object,
	* in two ways; one sorted by suit, and the other by rank
	*
	* @see sortByRank()
	* @see sortBySuit()
	*/
	public void print(){
		System.out.println("Here is your hand printed in two ways:");
		System.out.println("Organized by Suit:  ");
		sortBySuit();
		System.out.println(this.deck);
		System.out.println("Organized by Rank:  ");
		sortByRank();
		System.out.println(this.deck);
		}

	/**
	* method toString returns a string representation of every
	* card contained in the calling Deck Object
	*/
	public String toString(){
		String result = "";
		for (Card card:this.deck){
			result = result + "(" + card.getSuit() + ", " + card.getRank() + "), ";

	}
	return(result);
	}
}
