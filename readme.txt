1-The main objective of this program is to make ELIZA Psycotherapist chat bot
by making use of the regular expressions and some basic python concepts.

2- For example: if we run the program, as a intro statement our ELIZA bot will give
this phrase as a output ELIZA:"I am Eliza Psycotherapist, What is your name?"
for which if the user responds My name is Vijay then our program will spot the words
"My name is" and gives response by using regx methods as " Hello  vijay, How do you do? Please state your problem."
We used this to provide some personalization. If the users wants to take advantage of this command they should
type their command in this format "Anytext/my name is/Name" Name can be anything.

3- About our code and algorithm:
Corpus:
We decided that our program should match many different inputs from the user to do that we need wide variety of 
stories (userresponse, Eliza response). So for our stories we found a website with many different stories, we will
site the website in the references. The structured text from the website and the regular expressions are fuzzy.
We formatted them according to our program logic. We created lists for Eliza response.
Lists contain One or more than one responses. For some responses we used groups notations to convert the user input into
a question. example: User input "Do you remember ravi" 
                          Eliza: Did you think I would forget ravi (using re.sub() and groups)         

Program logic:
Step1: Eliza Intro response. We just used a print statement for this. To differentiate Eliza and User input
we created a function which will return "Eliza:".
Step2: Getting input from the user for this we used a for loop with standard input.
Step3: To make the word spotting effortless we decided to convert the input from the user into lower case
and store it into a variable.
Step4: Now we need to include our conditions for word spotting and the corresponding responses should 
be printed out as Eliza response. Throught out our program the conditions are consistent in two ways
First way: Condition to spot the word we used re.search() if we find a match then we print the eliza response
To print the Eliza response we call the response() function and pass the lists we created above with Eliza responses.
If the lists contains multiple responses we used np.random.choice(list) to select one random response from the list.
Second way: To spot the words we use re.search() in the second way also but the difference comes when we are printing
the response, for this we are calling the response() function and using re.sub() method. We are doing this in order
to use word substitutions to construct some responses by Eliza from users input.
Example:
response() function to customize Eliza response
def response():
    return "Eliza:"
print(response(), "I am Eliza Psycotherapist, What is your name?")
Program logic
firt way
for line in sys.stdin:                                                                         To read the user input and ignores text case (re.I)
    line = line.lower()                                                                        To convert the user input to lower
    if re.search(r".*hello .*",line,re.I):                                                     To Spot the words
        print(response(),np.random.choice(Hello_response))                                     To print the Eliza response from the stored responses in lists
Second way: Although it's second way we will include first way to find the match and for printing the response we use re.sub() method.
    elif re.search(r"(.*)?my name is(.*)?",line,re.I):
        print(re.sub(r"(.*)?my name is(.*)?",np.random.choice(Username_response),line))        Here we are substituting the user response using groups(regx) inside regx.
Finally if we don't find any words or if the user gives gibberish input our program will give output using default responses
    else:
          print(response(),np.random.choice(default_response))
Special commands:
If you want quit or exit the program please use "bye" or "exit" or "good bye"

Reference for corpus:
Website url:http://botartisanz.com/blog/create-your-eliza-chatbot-in-20-minutes-with-regular-expressions-day-6
Author: Jubin Jose

Copyright (c) 2018 Vijayasaradhi Muthavarapu, Nikhil Reddy Pathuri, Dilip Molugu
