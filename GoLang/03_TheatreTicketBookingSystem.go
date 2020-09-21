/*
This program creates a theatre structure, with 25 seats, and then proceeds to enter an infinate loop to sell tickets to customers.
Author: Aiden Stevenson Bradwell  ||  abrad060@uottawa.ca  ||  300064655
Janurary 30th, 2020
Created for: CSI2120 (Programming Paradigms)

USED Structs:
	Play
	Seat
	Category
	Comedy
	Tragedy
	Theatre
	Ticket

USED INTERFACE FUNCTIONS:
	getName() 				String
	getShowStart() 			time.Time
	getShowEnd() 			time.Time
	addPurchase(Ticket) 	bool
	isNotPurchased(Ticket) 	bool
	
USED FACTORY FUNCTIONS
	NewSeat(int32, int32, *Category)	Seat
	NewTicket(string, *Seat, *Show)		Ticket
	NewTheatre(*[]Seat, *[]Show)		Theatre
	NewTragedy(float32, int32, *Play)	Tragedy
	NewComedy(float32, int32, *Play)	Comedy
	NewCategory(string, float32) 		Category

USED MISC FUNCTIONS
	butTicket(*Theatre, int)			bool
*/

package main

import( "time" ; "fmt" )


type Show interface {
	 getName()	(string)
	 getShowStart() (time.Time)
	 getShowEnd()	(time.Time)
	 addPurchase(tick *Ticket) (bool)
	 isNotPurchased(tick *Ticket) (bool)
}

type Play struct {
	name string 
	purchased []Ticket
	showStart time.Time 
	showEnd time.Time
}
type Comedy struct{
	laughs float32
	deaths int32
	play  Play
}
type Tragedy struct {
	laughs float32
	deaths int32
	play  Play
}
type Seat struct {
	number 	int32
	row 	int32
	cat 	*Category
}
type Category struct {
	name 	string
	base 	float32
}
type Ticket struct {
	customer 	string
	s 			*Seat
	show 		*Show
}
type Theatre struct{
	seats	[]Seat
	shows 	[]Show
}

/*
In:
Out: Name of stored play
*/
func (p *Comedy) getName() (string){
 	return p.play.name
}
/*
In:
Out: Name of stored play
*/
 func (p *Comedy) getShowStart() (time.Time){
 	return p.play.showStart
} 
/*
In:
Out: Time the comedy starts
*/
func (p *Comedy) getShowEnd() (time.Time){
	return p.play.showEnd
} 
/*
In:
Out: Time the comedy ends
*/
func (p *Comedy) addPurchase(tick *Ticket) (bool){
	p.play.purchased = append(p.play.purchased, *tick )
	return true
}
/*
In: A ticket requested to be purchased
Out: Checks to see if the ticket is already sold for this comedy
*/
func (p *Comedy) isNotPurchased(tick *Ticket) (bool){
	if (tick == nil){ return false}
	for _, a := range p.play.purchased{
		if(a.s.number == tick.s.number && a.s.row == tick.s.row){ return false} 
	}
	return true
}

/*
In:
Out: Name of stored play
*/
func (p *Tragedy) getName() (string){
 	return p.play.name
}
/*
In:
Out: Name of stored play
*/
 func (p *Tragedy) getShowStart() (time.Time){
 	return p.play.showStart
} 
/*
In:
Out: Time the tragedy starts
*/
func (p *Tragedy) getShowEnd() (time.Time){
	return p.play.showEnd
} 
/*
In:
Out: Time the tragedy ends
*/
func (p *Tragedy) addPurchase(tick *Ticket) (bool){
	p.play.purchased = append(p.play.purchased, *tick )
	return true
}
/*
In: A ticket requested to be purchased
Out: Checks to see if the ticket is already sold for this tragedy
*/
func (p *Tragedy) isNotPurchased(tick *Ticket) (bool){
	if (tick == nil){ return false}
	for _, a := range p.play.purchased{
		if(a.s.number == tick.s.number && a.s.row == tick.s.row){ return false} 
	}
	return true
}


/*
In: The row and number of a new seat, aswell as teh type of seat this is
Out: The new seat which has been created
*/
func NewSeat(seatNum, rowNum int32, cate *Category) Seat{
	if(seatNum <= 0){ seatNum = 1; }
	if(rowNum <= 0){ rowNum = 1; }
	var cat Category
	if(rowNum == 1){
		cat = NewCategory("Prime",35)
	}else if(rowNum >= 2 && rowNum <=4){
		cat = NewCategory("Standard",25)
	}else{
		cat = NewCategory("Special",15)
	}
	return Seat{seatNum, rowNum, &cat}
}
/*
   TICKET FACTORY
*/
func NewTicket(cusName string, seat *Seat, show *Show) Ticket{
	if(seat == nil){ *seat = Seat{1,1,&Category{"Standard", 25.0}} }

	return Ticket{cusName, seat, show}
}
/*
   Theatre FACTORY
*/
func NewTheatre( numSeats *[]Seat, shows *[]Show ) Theatre{
	return Theatre{*numSeats, *shows}
}
/*
   Tragedy FACTORY
*/
func NewTragedy( lafs float32, deaths int32, play *Play) (Tragedy) {
	if (play.name == "") {
		play.name = "Macbeth"
	} 
	if (play.showStart.IsZero()){
		play.showStart = time.Date(2020, 04, 16, 9, 30, 0, 0,time.UTC)
	}
	if(play.showEnd.IsZero()){
		play.showEnd = time.Date(2020, 04, 16, 12, 30, 0, 0,time.UTC)
	}
	if (lafs < 0){
		lafs = 0.2
	}
	return Tragedy{lafs, deaths, *play}
}
/*
   Comedy FACTORY
*/
func NewComedy( lafs float32, deaths int32, play *Play) (Comedy){
	if(play.name == ""){
		play.name = "Tartufe"
	}
	if (play.showStart.IsZero() || play.showEnd.IsZero()){
		play.showStart = time.Date(2020, 03, 03, 16, 0, 0, 0,time.UTC)
		play.showEnd = time.Date(2020, 03, 03, 17, 20, 0, 0,time.UTC)

	}
	if (deaths < 0){
		deaths = 12
	}
	return Comedy{lafs, deaths, *play}
}
/*
   Category FACTORY
*/
func NewCategory(typ string, base float32) Category{
	if(base == 0){
		base = 25
	}
	if(typ == "" ||( typ != "Standard" && typ != "Prime" && typ != "Special")){
		typ = "Standard"
	}
	return Category{typ, base}
}
/*
   MAIN SCRIPT
*/
func main() {
	
	shows := []Show{}

	sadply := Play{"", []Ticket{},time.Date(2020, 03, 03, 19, 30, 0, 0,time.UTC), time.Date(2020, 03, 03, 22, 00, 0, 0,time.UTC)} //new tragedy play
	ply := Play{"", []Ticket{},time.Date(2020, 04, 10, 20, 00, 0, 0,time.UTC), time.Date(2020, 04, 10, 23, 00, 0, 0,time.UTC)} // new comedy play

	cmdy := NewComedy(-1, -1, &ply); // new comedy event
	trdgy := NewTragedy(-1, -1, &sadply); // new tragedy event

	shows = append(shows, &cmdy) 
	shows = append(shows, &trdgy)  // ALL SHOWS ADDED
	
	seats := []Seat{}
	for i:= 0; i<25; i++{
		seat := i % 5 + 1
		row := i/5 + 1
		temp := NewSeat(int32(seat), int32(row), nil) 
		seats = append(seats, temp)
	}
	theatre := NewTheatre(&seats,&shows) // ALL SEATS ADDED
	
	for{
		fmt.Println("************************") //Menu System for User
		fmt.Println("* TICKET MASTER*")
		fmt.Println("* [0] Purchase Comedy Ticket *")
		fmt.Println("* [1] Purchase Tragedy Ticket *")
		fmt.Println("* [2] Exit Program *")
		fmt.Println("************************")
		var n int
		m,err := fmt.Scanf("%d\n", &n)
		if(err != nil || m !=1){ fmt.Println(n, err)}
		if(n == 0){ 
			purchased := false
			for !purchased{
				purchased = buyTicket(&theatre, n)
			}
		}else if( n == 1){
			purchased := false
			for !purchased{
				purchased = buyTicket(&theatre, n)
			}
		}else if n == 2{
			fmt.Println("\n\n\n\n\n")
			break 
		}else{
			fmt.Println(n ," IS NOT AN OPTION*")
		}
	}
}

func buyTicket(theatre *Theatre,n int) bool{
	show := theatre.shows[n]
	fmt.Println("ENTER ROW [1-5] || ")
	var row int
	n, err :=fmt.Scanf("%d\n", &row)
	if err!= nil || n != 1{
		fmt.Println(n, err)
	}

	fmt.Println("ENTER SEAT [1-5] || ")
	var seat int
	n, err = fmt.Scanf("%d\n", &seat)
	if err!= nil || n != 1{
		fmt.Println(n, err)
	}

	if(row>5 || row <1 || seat>5 || seat <1){
		fmt.Println("INVALID COMBINATION.")
		return false
	}else{
		fmt.Println("CUSTOMERS NAME:")
		var name string
		n, err =  fmt.Scanf("%s\n", &name)
		if err!= nil || n != 1{
			fmt.Println(n, err)
		}
		tickseat := NewSeat(int32(seat),int32(row), nil) // Create requested seat
		tick := NewTicket(name, &tickseat, &show) // Create requested ticket

		if(show.isNotPurchased(&tick)){ // Attempt to sell ticket
			show.addPurchase(&tick)
			fmt.Println("*****TICKET PURCHASED by ", name ,"*****\n\n")
			return true
		}else{
			fmt.Println("TICKET ALREADY PURCHASED")
			checkingCat := NewCategory(tick.s.cat.name, tick.s.cat.base) //Mark which section was requested
			var seatsInSection, startSeat int 
			for w := 0; w < 3; w++{ // For each section of seating, scan each seat for one which is able to be sold
				if checkingCat.name == "Prime" { // Search requested section first
					seatsInSection = 5
					startSeat = 0
				} else if checkingCat.name == "Special" {
					seatsInSection = 5
					startSeat = 20
				} else if checkingCat.name == "Standard" {
					seatsInSection = 15
					startSeat = 5
				}
				for o:= startSeat; o<startSeat+seatsInSection; o++ { // for each seat in this section
					curSeat := theatre.seats[o]
					tryTick := NewTicket(name, &curSeat, &show) //Create a possible alternative ticket

					if curSeat.cat.name == checkingCat.name && show.isNotPurchased(&tryTick){ //If it is vald, suggest it to the user
						fmt.Println("\nALTERNATE OFFER: ",show.getName(), " ",curSeat.cat.name, " seat, ROW: " ,curSeat.row, "SEAT: " ,curSeat.number)
						fmt.Println("\nACCEPT ALTERNATE OFFER? [Y/N]")
						validEntry := false
						var accept string
						for !validEntry{ // See if the user accepts the alternative
							n, err = fmt.Scanf("%s\n", &accept)
							if err!= nil || n != 1{
								fmt.Println(n, err)
							}	
							if(accept == "Y" || accept == "y" || accept == "n" || accept == "N"){
								validEntry = true 
							}else{
								fmt.Println("\n\nINVALID ENTRY")
							}
						}
						if(accept == "Y" || accept == "y"){ // If so sell it
							show.addPurchase(&tryTick)
							fmt.Println("*****TICKET PURCHASED*****\n\n")
							return true
						}else{ // Otherwise have then enter another seat
							return false
						}
					}
				}
				if checkingCat.name == "Special" { checkingCat.name = "Standard" // If section is sold out, try more expensive ticket
				} else if checkingCat.name == "Prime" { checkingCat.name = "Special" // if this is a valid section
				} else if checkingCat.name == "Standard" { checkingCat.name = "Prime" // it will be suggested
				}
			}
			fmt.Println("NO MORE ALTERNATE OPTIONS") //All options checked. No mroe tickets are available. 
			return false
		}
	}
	return false // Error catch return statement
}