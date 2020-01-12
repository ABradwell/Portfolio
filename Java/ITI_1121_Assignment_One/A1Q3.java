// Author: Aiden Stevenson Bradwell, Winston Barrett-Hogg
// Student number: 300064655, 300087985
// Course: ITI 1121-C
// Assignment: 1
// Question: 3
public class A1Q3{

	/**
	*	method getLongestRun takes a reference of an array of double and returns
	* an integer representing the longest run of repetated consecutive values
	* in the referenced array
	*
	* @param		arr							reference of an array of type double
	*	@return		overallmax			length of maximum run in the referenced array
	*/

	static int getLongestRun(double[] arr){
		int currentmax;								//the current run of repeated and consecutive values
		int overallmax;								//the maximum length run found so far
		if (arr.length == 0){
			currentmax = 0;
			overallmax = 0;
		} else {
			currentmax = 1;
			overallmax = 1;
		}
		for (int i =0; i < arr.length - 1; i++){
			if (arr[i] == arr[i + 1]){
				currentmax = currentmax + 1;
				if (currentmax > overallmax){overallmax = currentmax;}
			} else {
				currentmax = 1;
			}
		}
		return (overallmax);
	}

	/**
	*	method getLongestRun takes a reference of an array of type string and
	* returns an integer representing the longest run of repetated consecutive
	* values in the referenced array
	*
	* @param		arr							reference of an array of type double
	*	@return		overallmax			length of maximum run in the referenced array
	*/

	static int getLongestRun(String[] arr){
		int currentmax;								//the current run of repeated and consecutive values
		int overallmax;								//the maximum length run found so far
		System.out.println(arr.length);
		if (arr.length == 0){
			currentmax = 0;
			overallmax = 0;
		} else {
			currentmax = 1;
			overallmax = 1;
		}
		for (int i =0; i < arr.length - 1; i++){
			if (arr[i].equals(arr[i + 1])){
				currentmax = currentmax + 1;
				if (currentmax > overallmax){overallmax = currentmax;}
			} else {
				currentmax = 1;
			}
		}
		return (overallmax);
}
}
