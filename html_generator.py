	# Code for Title:
def title (title_of_concepts):

# Output of procedure:
	concept_title_HTML = '''
	<div class = "conceptTitle">
		''' + "<h1> " + title_of_concepts + " </h1>"

	return concept_title_HTML


###########

	# Code for definition of Title:
def definition (definition_of_concepts):

# Output of procedure:
	notes_for_title_HTML = '''
			''' "<h2>" + "".join(definition_of_concepts) + "</h2>"

	return notes_for_title_HTML


###########

	# Code for Notes of the Title:
def notes (notes_of_concepts):

# Output of procedure:
	notes_of_concept = '''
		<div class = "notesOfConcept"> 
		''' + "".join(notes_of_concepts)

	return notes_of_concept


###########

	# Code to close the concept:
def closing ():
	closing_divs = '''
		</div>
	</div> '''

	return closing_divs


###########

	# Concatenation of all concepts introduced in the procedures:
def concatenation (number_of_concepts):
	counter = 0
	complete_HTML = ""
	while counter < number_of_concepts:
		title_HTML = title(title_of_concepts[counter])
		definition_HTML = definition(definition_of_concepts[counter])
		notes_HTML = notes(notes_of_concepts[counter])
		complete_HTML = complete_HTML + title_HTML + definition_HTML + notes_HTML + closing()
		counter = counter + 1
	return complete_HTML


	#Titles, definition, notes:
title_of_concepts = ["HTML",
										"CSS",
										"Computer Programming",
										"Python",
										"DOM"]
definition_of_concepts = ["HTML makes the structure of a website.",
													"configures the style of the website by changing the color, fonts, etc. of the different objects that are presented in the HTML.",
													"computers by itself cannot do much, unless a program is introduced and tells the computer what to do. A program uses the different components that a computer has available to perform the different commands that a program gives.",
													"a programming language that enables computers to do specific commands in few lines of code. The main reason computer languages are created is because they serve a specific purpose and have specific commands; whereas normal languages (English, Spanish, Danish, etc.) can contain certain ambiguity that might confuse the computer or send a command that was not desired.",
													"a cross-platform and language that interacts with objects from a HTML, XHTML, XML documents."]
notes_of_concepts = ['Every HTML file should start with <!DOCTYPE html> and wrap all the code within <html>',
										 'Adding style to HTML, there are 3 ways:']






