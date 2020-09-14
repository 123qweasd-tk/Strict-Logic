def input_first_formula():
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

def syllogism_deduction_first_value_n(first_formula,second_formula):
	if first_formula[0] == "n" and first_formula[1] == "n":	#caluculates potential "n"-values of first value
		return("n")
	elif second_formula[0] == "n" and first_formula[1] == "n":
		return("n")
	elif first_formula[0] == "n" and second_formula[2] == "n":
		return("n")
	elif second_formula[0] == "n" and second_formula[2] == "n":
		return("n")
	else: #calculates potential "u"-values of first value
		return("u")

def syllogism_deduction_first_value_a(first_formula,second_formula):
	if first_formula[0] == "a" and second_formula[1] == "n" and second_formula[0] == "n":	#calculates potential "a"-values of first value
		return("a")
	elif second_formula[0] == "a" and first_formula[2] == "n" and first_formula[0] == "n":
		return("a")
	elif first_formula[1] == "a" and second_formula[3] == "n" and second_formula[2] == "n":
		return("a")
	elif second_formula[2] == "a" and first_formula[3] == "n" and first_formula[1] == "n":
		return("a")
	else: #calculates potential "u"-values of first value
		return("u")

def syllogism_deduction_second_value_n(first_formula,second_formula):
	if first_formula[0] == "n" and first_formula[1] == "n":	#caluculates potential "n"-values of second value
		return("n")
	elif second_formula[1] == "n" and first_formula[1] == "n":
		return("n")
	elif first_formula[0] == "n" and second_formula[3] == "n":
		return("n")
	elif second_formula[1] == "n" and second_formula[3] == "n":
		return("n")
	else: #calculates potential "u"-values of second value
		return("u") 

def syllogism_deduction_second_value_a(first_formula,second_formula):
	if first_formula[0] == "a" and second_formula[0] == "n" and second_formula[1] == "n": #calculates potential "a"-values of second value
		return("a")
	elif second_formula[1] == "a" and first_formula[2] == "n" and first_formula[0] == "n":
		return("a")
	elif first_formula[1] == "a" and second_formula[2] == "n" and second_formula[3] == "n":
		return("a")
	elif second_formula[3] == "a" and first_formula[3] == "n" and first_formula[1] == "n":
		return("a")
	else: #calculates potential "u"-values of second value
		return("u") 

def syllogism_deduction_third_value_n(first_formula,second_formula):
	if first_formula[2] == "n" and first_formula[3] == "n":
		return("n")
	elif second_formula[0] == "n" and first_formula[3] == "n":
		return("n")
	elif first_formula[2] == "n" and second_formula[2] == "n":
		return("n")
	elif second_formula[0] == "n" and second_formula[2] == "n":
		return("n")
	else: 
		return("u")
		
def syllogism_deduction_third_value_a(first_formula,second_formula):
	if first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] == "n":
		return("a")
	elif second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] == "n":
		return("a")
	elif first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] == "n":
		return("a")
	elif second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] == "n":
		return("a")
	else: 
		return("u")
	
def syllogism_deduction_fourth_value_n(first_formula,second_formula):
	if first_formula[2] == "n" and first_formula[3] == "n":
		return("n")
	elif second_formula[1] == "n" and first_formula[3] == "n":
		return("n")
	elif first_formula[2] == "n" and second_formula[3] == "n":
		return("n")
	elif second_formula[1] == "n" and second_formula[3] == "n":
		return("n")
	else:
		return("u")

def syllogism_deduction_fourth_value_a(first_formula,second_formula):
	if first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] == "n":
		return("a")
	elif second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] == "n":
		return("a")
	elif first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] == "n":
		return("a")
	elif second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] == "n":
		return("a")
	else:
		return("u")

def	syllogism_contradiction_test(first_formula,second_formula):
	conclusion = [0,0,0,0,0,0,0,0]
	conclusion[0] = syllogism_deduction_first_value_n(first_formula,second_formula)
	conclusion[1] = syllogism_deduction_first_value_a(first_formula,second_formula)
	if conclusion[0] == 'n' and conclusion[1] == 'a':
		print('first error at 0')
		return(1)
	conclusion[2] = syllogism_deduction_second_value_n(first_formula,second_formula)
	conclusion[3] = syllogism_deduction_second_value_a(first_formula,second_formula)
	if conclusion[2] == 'n' and conclusion[3] == 'a':
		print('first error at 1')
		return(1)
	conclusion[4] = syllogism_deduction_third_value_n(first_formula,second_formula)
	conclusion[5] = syllogism_deduction_third_value_a(first_formula,second_formula)
	if conclusion[4] == 'n' and conclusion[5] == 'a':
		print('first error at 2')
		return(1)
	conclusion[6] = syllogism_deduction_fourth_value_n(first_formula,second_formula)
	conclusion[7] = syllogism_deduction_fourth_value_a(first_formula,second_formula)
	if conclusion[6] == 'n' and conclusion[7] == 'a':
		print('first error at 3')
		return(1)
	else:
		return(0)

def syllogism_deduction_first_value(first_formula,second_formula):
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

def syllogism_deduction_second_value(first_formula,second_formula):
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

def syllogism_deduction_third_value(first_formula,second_formula):
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
	
def syllogism_deduction_fourth_value(first_formula,second_formula):
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
	
def	syllogism_solution(first_formula,second_formula):
	conclusion = [0,0,0,0]
	conclusion[0] = syllogism_deduction_first_value(first_formula,second_formula)
	conclusion[1] = syllogism_deduction_second_value(first_formula,second_formula)
	conclusion[2] = syllogism_deduction_third_value(first_formula,second_formula)
	conclusion[3] = syllogism_deduction_fourth_value(first_formula,second_formula)
	return(conclusion)

def output(solution):
	if solution == ["a","u","n","a"]:
		return "All S are P, also known as"
	elif solution == ["a","u","u","u"]:
		return "Some S are P, also known as"
	elif solution == ["n","a","a","u"]:
		return "No S is P, also known as"
	elif solution == ["u","u","a","u"]:
		return "Some S are no P, also known as"
	else:
		return('No traditional categorical judge:')

#import pdb; pdb.set_trace()
first_formula = input_first_formula()
second_formula = input_second_formula()
result_contradiction_test = syllogism_contradiction_test(first_formula,second_formula)
if result_contradiction_test == 1:
	print('CONTRADICTION! FOLLOWING -CONCLUSION- IS NOT VALID!')
else:
	print('No contradiction.')
solution = syllogism_solution(first_formula,second_formula)
output = output(solution)
print(output)
print("S ",solution," P")
input("Exit with enter!")