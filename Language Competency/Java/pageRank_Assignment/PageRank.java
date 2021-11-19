/*
 * Framework @author Md Atiqur Rahman (mrahm021@uottawa.ca)
 * @author Aiden Stevenson Bradwell,300064655, abrad060@uottawa.ca
 */
 

import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

public class PageRank{
	public static final double DAMPING_FACTOR = 0.85;	// damping factor
	private double tolerance;							// tolerance to stop
	private long maxIter;								// max iterations to stop
	private Map<Integer, Double> nextRank;              // the next round of PRs for calculations 
	private Map<Integer, Double> lastRank;              // The Prs from alst round, used in the calculations of nextRank
	private List<Integer> nodes;                        // all nodes in a given graph
	private Map<Integer, List<Integer>> edges;          // all edges between said nodes


	PageRank(){
		// default tolerance=0.000001, default maxIter=100
		this(0.000001, 100);			
	}
	
	PageRank(double tolerance, long maxIter){
		this.tolerance = tolerance;
		this.maxIter = maxIter;
	}
	
	
	
	/**
	 * Computes the PageRank (PR) of each node in a graph in an iterative way.
	 * Iteration stops as soon as this.maxIter or this.tolerance whichever is reached first.
	 * 
	 * @param graph the Graph to compute PR for
     * @return returns a Map<Integer, Double> mapping each node to its PR
     * 
     */

	public Map<Integer, Double> computePageRank(Graph graph){
             //
		this.lastRank = new HashMap<Integer, Double>();
		this.nextRank = new HashMap<Integer, Double>();
		this.nodes = graph.getGraphNodes();
		this.edges = graph.getGraphEdges();

		int i = 1; //#of iterations
		double tol = 10000; //default high tolerance to assure it runs at least once
		double newTol;
		for(Integer curNode: nodes){ //Initialize rank arrays to each node being equal
			lastRank.put(curNode, 1.00);
			nextRank.put(curNode, 1.00);
		}

		while(i < this.maxIter && tol > this.tolerance){ //calculations have begun
			newTol = 0;
			for(Integer curNode: nodes){ //goes through each node in the list, and updates their PR
				List<Integer> pointingTo = new ArrayList<>(); //new array of nodes pointing to this node
				for(Integer otherNode: nodes){ //checks every other node to assure that it 
					if(edges.containsKey(otherNode)){
						if(edges.get(otherNode).contains(curNode) && otherNode != curNode){ 
							pointingTo.add(otherNode); //if it points to the current node, track it
						}
					}
				}
				adjustPR(curNode, pointingTo);
			}
			for(Integer aNode: nodes){ // calucluates the new tolerance based on the average of differences
				newTol = newTol + (lastRank.get(aNode) - nextRank.get(aNode));
			}
			tol = newTol/edges.size(); 
			for(Map.Entry<Integer, Double> cur: nextRank.entrySet()){
				lastRank.put(cur.getKey(), cur.getValue());  //moves the lastRank array forward a step
			}
			
			i++;
		}
		return lastRank;
	}

	/**
	 * Updates the PR of a specific node in an iterative way
	 * Iterates through all nodes poiting to the current node, and updates the PR for the next wave of PRs
	 * @param curNode the current node which is being updated
	 * @param pointingTo a list of all nodes pointing to the current node
     * 
     */
	private void adjustPR(Integer curNode, List<Integer> pointingTo){
		double newPR = (1- DAMPING_FACTOR); //initialize the new PR
		for(Integer pointedBy: pointingTo){
			newPR = newPR + DAMPING_FACTOR*(lastRank.get(pointedBy)/edges.get(pointedBy).size());
		}
		Double newPRDouble = new Double(newPR);
		nextRank.replace(curNode, newPRDouble);
	}
}
