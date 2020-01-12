// Author: Aiden Stevenson Bradwell, Winston Barrett-Hogg
// Student number: 300064655, 300087985
// Course: ITI 1121-C
// Assignment: 1
// Question: 2
public class A1Q2{

	/**
	*	method hasLengthTwoRun takes a reference of an array of double and returns
	* a boolean true if the referenced array has at least one run of at minimum
	* length two of repeated and consecutive values, and returns boolean false
	* otherwise.
	*
	* @param		arr		reference of an array of type double
	*	@return					boolean True if conditions above are met, false otherwise
	*/

	static Boolean hasLengthTwoRun(double[] arr){
		int currentrun;								//the current run of repeated and consecutive values
		int overallmax;								//the maximum length run found so far
		if (arr.length == 0){
			currentrun = 0;
			overallmax = 0;
		} else {
			currentrun = 1;
			overallmax = 1;
		}
		for (int i =0; i < arr.length - 1; i++){
			if (arr[i] == arr[i + 1]){
				currentrun = currentrun + 1;
				if (currentrun > overallmax){overallmax = currentrun;}
			} else {
				currentrun = 1;
			}
			if (overallmax >= 2){
				return (true);
			}
		}
		return (false);
	}
	}
