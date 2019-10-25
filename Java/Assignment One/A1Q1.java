// Author: Aiden Stevenson Bradwell, Winston Barrett-Hogg
// Student number: 300064655, 300087985
// Course: ITI 1121-C
// Assignment: 1
// Question: 1
public class A1Q1{

	/**
	*	method countPositive takes a reference of an array of doubles and returns
	* the count of elements in the referenced array that are positive (>0)
	*
	*	@param		arr		reference of an array of type double
	* @return		i  		the count of elements in arr that are positive (>0)
	*/

	static int countPositive(double[] arr){
			int i =0;																	//i = count of positive elemnents in arr
			for (double current:arr){
				if (current > 0){
					i++;
				}
		}
		return (i);
		}
}
