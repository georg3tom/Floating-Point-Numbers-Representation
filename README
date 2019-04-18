#Floating-Point Numbers Representation
.
└── app
    ├── errors		//contains routes related to errors
    ├── static		//contains all static files
    │   ├── css		//css files
    │   ├── img		//img files
    │   └── js		//js files
    ├── templates	//all templates(~error)
    │   └── errors	//error templates
    └── user		//all other routes and functions


	/templates/layout.html		contains the default layout for the html pages
	/templates/*.html 			loads layout from layout.html


	/errors/handlers.py			contains routes for error 404 and 500


###	/static/js/exp.js :
		funtion ieee()
			reads value from the input box(id='infloat')
			sends a GET request to the server
			var ret is a JSON data containing the sign,exponent,exponent bits of the input
			if ret['status'] is fail the input validation has failed
			else a new table is inserted

###	/static/js/quiz.js :
		function check() :
			gets user marked options from the form
			send a GET requst to evaluate the users response
			var ret is a string of 0s and 1s
			if ret=1011 -> only the second qustion is incorrect
			if k[i] is 5 -> i+1th question is unansweres
			this is done so that that question not marked incorrect

		function reset() :
			Resets the users input and
			clears 'Correct' or 'Incorrect' tags

###	/quizadd.py :
		adds question to the database
		the database file is located at app/quiz.db


###	/user/controllers.py :
		Contains routed to all pages in the navbar-
			Introduction,Objective,Theory,Experiment,Manual,Quizzes,Procedure,Reference,
			Feedback and for other get request for quiz and experiment


			/experiment/<arg>:
				return a JSON file with the IEEE fomat variable (Exp,Mantissa,Sign)
				If the validation of arg fails (If args is not a floating-point number)
				then JSON data with ['status']="fail" is returned
			/quizzes? :
				creates a list containing 4 random numbers between 1 and 8
				args is an array of JSON objects containing questions with id in the list
				args is passed to the render_template function

				if qi is not None
				qi is the users response
				qii is the question id
				quizcheck is called to evaluate the users response


###	/user/model.py :
		Contains Quiz class which is a model for the database

		function quizcheck() :
			Checks if the user input matches with the answers saved in the database

###	/user/exp.py :
		Functions to convert a number to its iEEE 754 representation
