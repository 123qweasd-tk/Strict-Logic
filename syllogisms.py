def input_first_formula():
	global first_formula
	first_formula = input("First logical formula:")
	if first_formula == "MaP":
		first_formula = "auna"
	elif first_formula == "MeP":
		first_formula = "naau"
	elif first_formula == "MiP":
		first_formula = "auuu"
	elif first_formula == "MoP":
		first_formula = "uuau"
	elif first_formula == "PaM":
		first_formula = "anua"
	elif first_formula == "PeM":
		first_formula = "naau"
	elif first_formula == "PiM":
		first_formula = "auuu"
	elif first_formula == "PoM":
		first_formula = "uauu"
	return(first_formula)
	
def input_second_formula():
	global second_formula
	second_formula = input("Second logical formula:")
	if second_formula == "SaM":
		second_formula = "auna"
	elif second_formula == "SeM":
		second_formula = "naau"
	elif second_formula == "SiM":
		second_formula = "auuu"
	elif second_formula == "SoM":
		second_formula = "uuau"
	elif second_formula == "MaS":
		second_formula = "anua"
	elif second_formula == "MeS":
		second_formula = "naau"
	elif second_formula == "MiS":
		second_formula = "auuu"
	elif second_formula == "MoS":
		second_formula = "uauu"
	return(second_formula)
	
def syllogism_deduction_first_value():
	if first_formula[0] == "n" and first_formula[1] == "n":	#caluculates potential "n"-values of first value
		return("n")
	elif second_formula[0] == "n" and first_formula[1] == "n":
		return("n")
	elif first_formula[0] == "n" and second_formula[2] == "n":
		return("n")
	elif second_formula[0] == "n" and second_formula[2] == "n":
		return("n")
	elif first_formula[0] == "a" and second_formula[1] == "n" and second_formula[0] != "n":	#calculates potential "a"-values of first value
		return("a")
	elif second_formula[0] == "a" and first_formula[2] == "n" and first_formula[0] != "n":
		return("a")
	elif first_formula[1] == "a" and second_formula[3] == "n" and second_formula[2] != "n":
		return("a")
	elif second_formula[2] == "a" and first_formula[3] == "n" and first_formula[1] != "n":
		return("a")
	else: #calculates potential "u"-values of first value
		return("u")

def syllogism_deduction_second_value():
	if first_formula[0] == "n" and first_formula[1] == "n":	#caluculates potential "n"-values of second value
		return("n")
	elif second_formula[1] == "n" and first_formula[1] == "n":
		return("n")
	elif first_formula[0] == "n" and second_formula[3] == "n":
		return("n")
	elif second_formula[1] == "n" and second_formula[3] == "n":
		return("n")
	elif first_formula[0] == "a" and second_formula[0] == "n" and second_formula[1] != "n": #calculates potential "a"-values of second value
		return("a")
	elif second_formula[1] == "a" and first_formula[2] == "n" and first_formula[0] != "n":
		return("a")
	elif first_formula[1] == "a" and second_formula[2] == "n" and second_formula[3] != "n":
		return("a")
	elif second_formula[3] == "a" and first_formula[3] == "n" and first_formula[1] != "n":
		return("a")
	else: #calculates potential "u"-values of second value
		return("u") 

def syllogism_deduction_third_value():
	if first_formula[2] == "n" and first_formula[3] == "n":
		return("n")
	elif second_formula[0] == "n" and first_formula[3] == "n":
		return("n")
	elif first_formula[2] == "n" and second_formula[2] == "n":
		return("n")
	elif second_formula[0] == "n" and second_formula[2] == "n":
		return("n")
	elif first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] != "n":
		return("a")
	elif second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
		return("a")
	elif first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] != "n":
		return("a")
	elif second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
		return("a")
	else: 
		return("u")
	
def syllogism_deduction_fourth_value():
	if first_formula[2] == "n" and first_formula[3] == "n":
		return("n")
	elif second_formula[1] == "n" and first_formula[3] == "n":
		return("n")
	elif first_formula[2] == "n" and second_formula[3] == "n":
		return("n")
	elif second_formula[1] == "n" and second_formula[3] == "n":
		return("n")
	elif first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] != "n":
		return("a")
	elif second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
		return("a")
	elif first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] != "n":
		return("a")
	elif second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
		return("a")
	else:
		return("u")
	
def	syllogism_solution():
	first_formula = input_first_formula()
	second_formula = input_second_formula()
	conclusion = [0,0,0,0]
	conclusion[0] = syllogism_deduction_first_value()
	conclusion[1] = syllogism_deduction_second_value()
	conclusion[2] = syllogism_deduction_third_value()
	conclusion[3] = syllogism_deduction_fourth_value()
	if conclusion == ["a","u","n","a"]:
		return "All S are P"
	elif conclusion == ["a","u","u","u"]:
		return "Some S are P"
	elif conclusion == ["n","a","a","u"]:
		return "No S is P"
	elif conclusion == ["u","u","a","u"]:
		return "Some S are no P"

solution = syllogism_solution()
print(solution)
input("Exit with enter!")