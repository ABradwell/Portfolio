// Aiden Stevenson Brawell
// September 21st, 2020
// abrad060@uottawa.ca

// Task given: Implement the Gales-Shapely algorithm for the stable marriage problem.

package main

import( "fmt"; "encoding/csv"; "os";"time" )

var matches = []*Match{}

type Student struct{
	name 			string
	happiness		int
	assigned		*Company
	prefNames		[]string
	prefCompanies	[]*Company
	offeredBy		[]string
}
type Company struct{
	name 			string
	happiness	 	int
	assigned 		*Student
	prefNames		[]string
	prefStudents	[]*Student
}
type Match struct{
	student 	*Student
	company 	*Company
}
func newStudent(name string) Student{
	if name == ""{
		fmt.Println("NAME ERROR")
	}
	newst:= Student{name, int(^uint(0) >> 1), nil, []string{}, []*Company{}, []string{}}
	return newst;
}
func newCompany(name string) Company{
	if name == ""{
		fmt.Println("NAME ERROR")
	}
	return Company{name, int(^uint(0) >> 1), nil, []string{}, []*Student{}}
}
func newMatch(st *Student, co *Company) Match{
	return Match{st, co}
}

func AddStudent(s *Student, c *Company){
	c.prefStudents = append(c.prefStudents, s)
}
func AddCompany(s *Student, c *Company){
	s.prefCompanies = append(s.prefCompanies, c)
}

func addOffer(student *Student, str string){
	student.offeredBy = append(student.offeredBy, str)
}

func updateHappiness(st *Student, co *Company) {
	for i := 0; i< len(st.prefCompanies); i++{
		if st.prefCompanies[i].name == co.name{
			st.happiness = i
		}
	}
	for o := 0; o< len(co.prefStudents); o++{
		if co.prefStudents[o].name == st.name{
			co.happiness = o
		}
	}
}

func potentialStHappiness(st *Student, co *Company)int{
	var a int
	for i := 0; i< len(st.prefCompanies); i++{
		if st.prefCompanies[i].name == co.name{
			a = i
		}
	}
	return a
}

func offer(co *Company, ch chan bool){
	if(co.assigned == nil){
		for i:= 0; i<len(co.prefStudents); i++{
			a:= co.prefStudents[i];
			offered := false
			for _,b := range a.offeredBy{
				if co.name == b {
					offered = true
				}
			}
			if !offered{
				thisMatch := newMatch(co.prefStudents[i], co)
				ch <-evaluate(&thisMatch, ch)
				break
			}
		}
	}
}

func evaluate(match *Match, ch chan bool) bool{
	if match.student.assigned == nil{
		//Update the two structs information
		match.student.offeredBy = append(match.student.offeredBy, match.company.name)
		match.student.assigned = match.company
		match.company.assigned = match.student
		updateHappiness(match.student, match.company)
		addOffer(match.student, match.company.name)
		matches = append(matches, match)
	} else if (match.student.happiness > potentialStHappiness(match.student, match.company)){
		tempCo := match.student.assigned;
		for i := 0 ; i< len(matches) ; i++ {
			if matches[i].student.name == match.student.name {
				//Update the two structs information
				match.student.assigned.assigned = nil
				matches[i] = match
				addOffer(match.student, match.company.name)
				match.student.assigned = match.company
				match.company.assigned = match.student
				updateHappiness(match.student, match.company)
				break
			}
		}
		//send newly freed comapny into the algorithm
		offer(tempCo, ch)
		return true
	} else {
		addOffer(match.student, match.company.name)
		offer(match.company, ch)
		return false
	}
	return true
}

func main() {
	var size int
	companies := []*Company{} //Will store companies
	students := []*Student{} // Will store students
	//Begin file reading proccess
	openArgs := os.Args[1:]
	// Load in student information file
	studentFile, err := os.Open(openArgs[1])
	if err != nil {
		fmt.Println("FIle 1 Loading Error")
	}
	defer studentFile.Close()
	// initial student file reading
	studentReader, err := csv.NewReader(studentFile).ReadAll()
	if err != nil{
		fmt.Println("FIle 1 Reading Error")
	}
	for _, stud := range studentReader{
		newStud := newStudent(stud[0])
		newStud.prefNames = stud[1:]
		students = append(students, &newStud)
	}
	// initial company information file read
	companyFile, err := os.Open(openArgs[0])
	if err != nil {
		fmt.Println("File 2 Loading Error")
	}
	defer companyFile.Close()
	//  Initial company file reading
	companyReader, err := csv.NewReader(companyFile).ReadAll()
	if err != nil{
		fmt.Println("FIle 1 Reading Error")
	}
	for _, co := range companyReader{
		newCo := newCompany(co[0])
		newCo.prefNames = co[1:]
		size = len(newCo.prefNames) //For file naming purposes
		companies = append(companies, &newCo)
	}
	//Connect students' preferred comapny names with their company structs
	for _, a:= range companies{
		for _, b := range a.prefNames{
			for _,c := range students{
				if b == c.name{
					AddStudent(c, a)
					break
				}
			}
		}
	}
	//Do the inverse for the companies
	for _, a:= range students{
		for _, b := range a.prefNames{
			for _,c := range companies{
				if b == c.name{
					AddCompany(a, c)
					break
				}
			}
		}
	}

	//Run concurrent channels
	newCh := make(chan bool,10)
	for _, a := range companies{
		go offer(a, newCh)
		time.Sleep(time.Millisecond * 50)
	}
	counter := 0
	Forever:
		for{ // While some companies have not closed their channel
			select{
			case good := <-newCh:
				if(good){
					counter++ //Another company returned
				}
			default:
				if counter >= len(companies){
					break Forever //all comapies set, break free
				}
			}
		}
	//FIle to be created
	path := fmt.Sprintf("matches_go_%d_%d.csv", size, size)
	var _, existsErr = os.Stat(path)
	if existsErr == nil{
		os.Remove(path)
	}
	//Creating a new file
	outFile, er := os.Create(path)
	if er != nil{
		fmt.Println( er)
	}
	//Information being written by
	outWriter := csv.NewWriter(outFile)
	for _, match := range matches{
		outline := []string{match.student.name, match.company.name}
		_ = outWriter.Write(outline)
	}
	outWriter.Flush()
	outFile.Close()
}
