package main;
import ("fmt"; "math"; "sync"; "time")

var waitt sync.WaitGroup

type Neuron struct{
	weight 		float64 //v in the equaltion
	layer 		int32 //v in the equaltion
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
func AddNeuron(n *Neuron, l *Layer){
	l.neurons = append(l.neurons, n)
}
func AddLayer(n *Network, l *Layer){
	n.levels = append(n.levels, l)
}
func addInChannel(neuron *Neuron, ch *chan float64){
	neuron.inChs = append(neuron.inChs, *ch)
}
func wireNetwork(network *Network){
	for i := len(network.levels) - 1; i > 0; i-- {
		curLevel := network.levels[i].neurons
		beneath := network.levels[i-1].neurons
		 // fmt.Println("CurLevel Size: ", len(curLevel))
		 // fmt.Println("Beneath Size: ", len(beneath))
		for _, connecting := range beneath{
			for _, connectTo := range curLevel{
				if(connectTo.weight != 1){
					addInChannel(connectTo, &connecting.outCh)
				}
			}
		}
	}
}
func printNetwork(network *Network){
	for _, a := range network.levels{
		fmt.Println("\n\nLEVEL ", a.level)
		i:= 1
		for _, b := range a.neurons{
			fmt.Println("\nNEURON ", i)
			fmt.Println("Weight: ", b.weight)
			fmt.Println("Output: ", b.outCh)
			fmt.Println("Input: ", b.inChs)
			fmt.Println("Offset:", b.offset)
			i++
		}
	}
}

func refreshNetwork(network *Network) Network{
	fmt.Println("Refreshing network")
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
	// printNetwork(&newNet)
	return newNet
}

func getWeight(group *sync.WaitGroup, neuron *Neuron){
			group.Done()
			// fmt.Println("Neuron on Level: ", neuron.layer)
			// fmt.Println("Neuron weight: ", neuron.weight)
			// fmt.Println("Neuron out Channel: ", neuron.outCh)
			// fmt.Println("Neuron input ch: ", neuron.inChs)
			temp := neuron.weight
			for i:= 0; i < len(neuron.inChs); i++{
				// fmt.Println("Requesting information for Level ", neuron.layer, " ",  neuron.inChs[i])
				inputData := <- neuron.inChs[i]
				// fmt.Println("Received Information for ", neuron.layer, " ",  neuron.inChs[i])
				temp = temp + (neuron.offset[i])*inputData
			}
			fmt.Println("[LAYER ",neuron.layer,"] TEMP:", temp)
			if(neuron.weight == 0 && neuron.layer > 0){
				neuron.weight = (1/float64(1+ math.Pow(math.E, -temp)))
				neuron.outCh <- (1/float64(1 + math.Pow(math.E, -temp)))
			}else{
				neuron.outCh <- neuron.weight
				// fmt.Println("Sending Information from", neuron.outCh)
			}
			time.Sleep(time.Millisecond)
		}

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
	wireNetwork(&network)
	working := refreshNetwork(&network)


	//var n int
	//var e error
	//n,e = fmt.Scanf("%d", &n, &e)


	n := 10
	for i := 0; i<n; i++{
		working.levels[0].neurons[0].weight = 1
		printNetwork(&working)
		working.levels[0].neurons[1].weight = math.Sin(float64(2)*(math.Pi)*float64(i-1)/float64(n))
		working.levels[0].neurons[2].weight = math.Sin(float64(2)*(math.Pi)*float64(i-1)/float64(n))
		fmt.Println("start: ", working.levels[0].neurons[1].weight)
		for w := 1 ; w < len(working.levels); w++ {
			for q := 0 ; q < len(working.levels[w].neurons); q++ {
				waitt.Add(4)
				go getWeight(&waitt, working.levels[w].neurons[q])
				time.Sleep(time.Millisecond*2)
				go getWeight(&waitt, working.levels[0].neurons[0])
				time.Sleep(time.Millisecond * 2)
				go getWeight(&waitt, working.levels[0].neurons[1])
				time.Sleep(time.Millisecond * 2)
				go getWeight(&waitt, working.levels[0].neurons[2])
				time.Sleep(time.Millisecond * 2)
			}
		}
		waitt.Wait()
		output := <- working.levels[2].neurons[0].outCh
		fmt.Println("HERE: ", output)
		// printNetwork(&working)
		working = refreshNetwork(&network)
	}

	
	

}



