/*
Simple Neural network Structure. 
Author: Aiden Stevenson Bradwell  ||  abrad060@uottawa.ca  ||  300064655
Janurary 30th, 2020
Created for: CSI2120 (Programming Paradigms)

USED Structs:
	Neuron 		
	Layer 		
	Network 	

USED NETWORK CONSTRCUTOR FUNCTIONS:
	AddNeuron(*Neuron, *Layer)				nil
	AddLayer(*Network, *Layer) 				nil
	addInChannel(*Neuron, *chan float64)	nil

USED FACTORY FUNCTIONS:
	NewNeuron(float64, int32, *[]float64)	Neuron
	NewLayer(int32)							Layer
	NewNetwork()							Network

USED MISC FUNCTIONS:
	wireNetwork(*Network)			nil
	printNetwork(*Network)			nil
	refreshNetwork(*Network)		nil
	getWeight(*WaitGroup, *Neuron)	nil


Sample Neuron Structure:


				|
********** [OUT CHANNEL] **********
*[weight]		|	   [dampeners]*
*	  {	[Signma Formula] }	      *
*		 /	    |	   \	      *
*		/		|	    \	      *
*** IN-CH *** IN-CH *** IN-CH *****
	  |			|		  |

*/

package main;
import ("fmt"; "math"; "sync"; "time";)

var waitt sync.WaitGroup

type Neuron struct{
	weight 		float64 
	layer 		int32 
	outCh		chan float64
	inChs		[]chan float64
	offset		[]float64
}
type Layer struct{
	level 		int32
	neurons 	[]*Neuron
}
type Network struct{
	levels	[]*Layer
}

// FACTORY METHODS

func NewNeuron(w float64, l int32, off *[]float64) Neuron{
	chann:= make(chan float64)
	return Neuron{w,l,chann, []chan float64{}, *off}
}
func NewLayer(l int32) Layer{
	return Layer{l, []*Neuron{}}
}
func NewNetwork() Network{
	return Network{[]*Layer{}}
}


// CONSTRUCTION METHODS

func AddNeuron(n *Neuron, l *Layer){
	l.neurons = append(l.neurons, n)
}
func AddLayer(n *Network, l *Layer){
	n.levels = append(n.levels, l)
}
func addInChannel(neuron *Neuron, ch *chan float64){
	neuron.inChs = append(neuron.inChs, *ch)
}


//Given a disconnected network w/ layers, this creates the channels which connect their neurons
//Wires the network fully, and directly edits the neuron's input ports
//Each neuron on the lwer level connects to every neuron on the layer above it

func wireNetwork(network *Network){
	for i := len(network.levels) - 1; i > 0; i-- {
		curLevel := network.levels[i].neurons
		beneath := network.levels[i-1].neurons
		for _, connecting := range beneath{
			for _, connectTo := range curLevel{
				if(connectTo.weight != 1){
					addInChannel(connectTo, &connecting.outCh)
				}
			}
		}
	}
}

//Used to display the structure of the network. 

func printNetwork(network *Network){
	for _, a := range network.levels{
		fmt.Println("\n\nLEVEL ", a.level)
		i:= 1
		for _, b := range a.neurons{
			fmt.Println("\n      NEURON ", i)
			fmt.Println("      Weight: ", b.weight)
			fmt.Println("      Output: ", b.outCh)
			fmt.Println("      Input: ", b.inChs)
			fmt.Println("      Offset:", b.offset)
			i++
		}
	}
}

//  Takes an existing network, and recreates the layout
//  It then rewires this new network
//  Values are reset and network is ready to be fired again

func refreshNetwork(network *Network) Network{
	newNet := NewNetwork()
	for _, a := range network.levels{
		newLayerClone := NewLayer(a.level)
		for _, b := range a.neurons{
			newoffset := []float64{}
			for _,c := range b.offset{
				newoffset = append(newoffset, c)
			}
			var fillerNeuron Neuron
			if(len(b.inChs) == 0 && b.layer > 0){
					fillerNeuron =  NewNeuron(1, b.layer, &newoffset)

			}else{
					fillerNeuron =  NewNeuron(0, b.layer, &newoffset)
			}
			AddNeuron(&fillerNeuron, &newLayerClone)
		}
		AddLayer(&newNet, &newLayerClone)
	}
	wireNetwork(&newNet)
	return newNet
}

//  Calculates the weight of the neuron
//  if input is available already, it fires the neuron directly by interpretaing the input channels' inforomation and sening it onwards
//  Otherwise, it halts and waits for all inputs to be provided

func getWeight(group *sync.WaitGroup, neuron *Neuron){
			group.Done()
			
			temp := neuron.weight
			for i:= 0; i < len(neuron.inChs); i++{
				inputData := <- neuron.inChs[i]
				temp = temp + (neuron.offset[i])*inputData
			}
			if(neuron.weight == 0 && neuron.layer > 0){
				neuron.weight = (1/float64(1+ math.Pow(math.E, -temp)))
				neuron.outCh <- (1/float64(1 + math.Pow(math.E, -temp)))
			}else{
				neuron.outCh <- neuron.weight
			}
			time.Sleep(time.Millisecond)
		}

//Main script, creating a network consisting of 3 layers made out of 3 neurons, 4 neurons and one final neuron.

func main(){
	network := NewNetwork()
	//Bottom Layer
	bottomLayer := NewLayer(0)
	a1 := NewNeuron(1,0, &[]float64{})
	x1 := NewNeuron(0,0, &[]float64{})
	x2 := NewNeuron(0,0, &[]float64{})
	AddNeuron(&a1, &bottomLayer )
	AddNeuron(&x1, &bottomLayer )
	AddNeuron(&x2, &bottomLayer )
	AddLayer( &network,&bottomLayer)

	//Middle Layer
	hiddenLayer := NewLayer(1)
	b1 := NewNeuron(1,1,&[]float64{})
	z1 := NewNeuron(0,1,&[]float64{0.1,0.3,0.4})
	z2 := NewNeuron(0,1,&[]float64{0.5,0.8,0.3})
	z3 := NewNeuron(0,1,&[]float64{0.7,0.6,0.6})
	AddNeuron(&b1, &hiddenLayer)
	AddNeuron(&z1, &hiddenLayer)
	AddNeuron(&z2, &hiddenLayer)
	AddNeuron(&z3, &hiddenLayer)
	AddLayer( &network,&hiddenLayer)

	//Output Layer
	lastLayer := NewLayer(2)
	out := NewNeuron(0,2,&[]float64{0.5,0.3,0.7,0.1});
	AddNeuron(&out, &lastLayer)
	AddLayer( &network, &lastLayer)

	//wire the network and clone it
	wireNetwork(&network)
	working := refreshNetwork(&network)

	//users main input
	var n int
	fmt.Println("Enter how many networks you would like to produce...")
	_,err := fmt.Scanf("%d", &n)
	fmt.Println(n, err)
	//run a new network as many times as requested
	//Works for request netowrk size, but needs to be tweaked for a relative sized network
	for i := 0; i<n; i++{
		working.levels[0].neurons[0].weight = 1
		working.levels[0].neurons[1].weight = math.Sin(float64(2)*(math.Pi)*float64(i-1)/float64(n))
		working.levels[0].neurons[2].weight = math.Cos(float64(2)*(math.Pi)*float64(i-1)/float64(n))
		for w := 1 ; w < len(working.levels); w++ { // for each level of the network
			for q := 0 ; q < len(working.levels[w].neurons); q++ { // and for each neuron on that level
				waitt.Add(1)
				go getWeight(&waitt, working.levels[w].neurons[q]) //read input and fire neuron
				time.Sleep(time.Millisecond)
				for t := 0; t<len(working.levels[w-1].neurons);  t++{ //for each neuron beneath this now-waiting-to-fire neuron
					waitt.Add(1)
					go getWeight(&waitt, working.levels[w-1].neurons[t]) //Fire neurons upward
				}
			}
		}
		waitt.Wait() //allow all neurons to finish firing
		output := <- working.levels[2].neurons[0].outCh // pull final neuron's data
		fmt.Println(output)
		working = refreshNetwork(&network) //reset netowrk to fire again
	}
}



