# Team name: Evil Geniuses
# Authors:
# Vijayasaradhi Muthavarapu (Vijay)
# Nikhil Reddy Pathuri (Nikhil)
# Dilip Molugu (Dilip)
# Date: 9/19/2018


# Please import required libraries first
import sys
import re
import numpy as np
# Now we need required responses for our eliza bot.so we scraped internet for these responses
# Stored them according to their keys or matching words as a List.
Hello_response = ["How do you do? Please state your problem."]
Username_response = [r"Hello \2, How do you do? Please state your problem."]
Computer_response = [
        "Do computers worry you?",
        "What do you think about machines?",
        "Why do you mention computers?",
        "What do you think machines have to do with your problem?",
        ]
Name_response = ["I am not interested in names"]
Sorry_response = [
    "Please don't apologize",
    "Apologies are not necessary",
    "What feelings do you have when you apologize",
    ]
Userremeber_response = [
    r'Do you often think of me\2',
    r"Does thinking of me\2 bring anything else to mind",
    r"What else do you remember",
    r"Why do you recall me\2 right now",
    r"What in the present situation reminds you of me\2",
    r"What is the connection between me and you\2",
    ]
Userremeber_response1 = [
    r"Do you often think of\2",
    r"Does thinking of\2 bring anything else to mind",
    "What else do you remember?",
    r"Why do you recall\2 right now",
    r"What in the present situation reminds you of\2",
    r"What is the connection between me and\2",
    ]
Sysremember_response = [
    r"Did you think I would forget my\2",
    r"Why do you think I should recall my\2 now",
    r"What about my\2?",
    r"You mentioned my\2",
    ]
Sysremember_response1 = [
    r"Did you think I would forget\2",
    r"Why do you think I should recall\2 now",
    r"What about\2",
    r"You mentioned\2",
    ]
Userwants_response = [
    r"What would it mean if you got\2",
    r"Why do you want\2?",
    r"Suppose you got\2 soon."
    ]
If_response = [
    r"Do you really think it's likely that\2?",
    r"Do you wish that\2?",
    r"What do you think about\2?",
    r"Really--if\2?"
    ]
Userdreamt_response = [r"How do you feel about $2 in reality?"]
Dream_response = [
    r"What does this dream suggest to you?",
    r"Do you dream often?",
    r"What persons appear in your dreams?",
    r"Don't you believe that dream has to do with your problem?",
    ]
Usermother_response = [
    r"Who else in your family\2?",
    "Tell me more about your family",
    ]
Userfather_response = [
    "Your father?",
    "Does he influence you strongly?",
    "What else comes to mind when you think of your father?",
    ]
Userglad_response = [
    r"How have I helped you to be\2?",
    "What makes you happy just now?",
    r"Can you explain why you are suddenly\2?",
    ]
Usersad_response = [
    "I am sorry to hear you are depressed",
    "I'm sure it's not pleasant to be sad",
    ]
arelike_response = [
    r"What resemblence do you see between\1 and\2?",
    ]
islike_response = [
    r"In what way is it that\1 is like\2?",
    "What resemblence do you see?",
    "Could there really be some connection?",
    "How?",
    ]
alike_response = [
    "In what way?",
    "What similarities are there?",
    ]
same_response = [
    "What other connections do you see?",
    ]
no_response = [
    "Why not?",
    "You are being a bit negative.",
    "Are you saying 'No' just to be negative?"
    ]
Userwas_response = [
    r"Were you really?",
    r"Perhaps I already knew you were\2.",
    r"Why do you tell me you were\2 now?"
    ]
wasuser_response = [
    r"What if you were\2?",
    r"Do you think you were\2?",
    r"What would it mean if you were\2?",
    ]
Iam_response = [
    r"In what way are you\2?",
    r"Do you want to be\2?",
    ]
ami_response = [
    r"Do you believe you are\2?",
    r"Would you want to be\2?",
    r"You wish I would tell you you are\2?",
    r"What would it mean if you were\2?",
    ]
am_response = [
    "Why do you say 'AM?'",
    "I don't understand that"
    ]
areyou_response = [
    r"Why are you interested in whether I am\2 or not?",
    r"Would you prefer if I weren't\2?",
    r"Perhaps I am\2 in your fantasies",
    ]
youare_response = [r"What makes you think I am\2?"]

because_response = [
    "Is that the real reason?",
    "What other reasons might there be?",
    "Does that reason seem to explain anything else?",
    ]
wereyou_response = [
    r"Perhaps I was\2?",
    "What do you think?",
    r"What if I had been\2?",
    ]
Usercant_response = [
    r"Maybe you could\2 now",
    r"What if you could\2?",
    ]
Userfeel_response = [r"Do you often feel\2?"]

Userfelt_response = ["What other feelings do you have?"]

fantasy_response = [r"Perhaps in your fantasy we\2 each other"]

dontyou_response = [
    r"Should you\2 yourself?",
    r"Do you believe I don't\2?",
    r"Perhaps I will\2 in good time",
    ]
yes_response = [
    "You seem quite positive",
    "You are sure?",
    "I understand",
    ]
someone_response = ["Can you be more specific?"]

everyone_response = [
    "Surely not everyone",
    "Can you think of anyone in particular?",
    "Who, for example?",
    "You are thinking of a special person",
    ]
always_response = [
    "Can you think of a specific example?",
    "When?",
    "What incident are you thinking of?",
    "Really--always?",
    ]
what2_response = [
    "Why do you ask?",
    "Does that question interest you?",
    "What is it you really want to know?",
    "What do you think?",
    "What comes to your mind when you ask that?",
    ]
perhaps_response = ["You do not seem quite certain"]

are_response = [
    r"Did you think they might not be\2?",
    r"Possibly they are\2",
    ]
Story_response = ["Man and God met somewhere; Both exclaimed 'My Creator'",]

Good_response = [r"A very good \1 to you too"]

Creator_response = ["Evil Geniuses created me"]

Flip_coin_response = [
    "It's Heads!",
    "It's Tails!",
    ]
canyou1_response = [
    r"why do you want me to\2you?",
    r"does it help you if I\2you?",
]

canyou_response = [
    r"why do you want me to\2?",
    r"does it help you if I\2?",
]
# Below these responses, i have few default responses to be given to the user to maintain robustness
default_response = [
    "Very interesting",
    "I am not sure I understand you fully",
    "What does that suggest to you?",
    "Please continue",
    "Go on",
    "Do you feel strongly about discussing such things?",
    ]
def response():
    return "Eliza:"
print(response(), "I am Eliza Psycotherapist, What is your name?")
for line in sys.stdin:
    line = line.lower()
    if re.search(r".*hello .*",line,re.I):
        print(response(),np.random.choice(Hello_response))
    elif re.search(r"(.*)?my name is(.*)?",line,re.I):
        print(re.sub(r"(.*)?my name is(.*)?",np.random.choice(Username_response),line))
    elif re.search(r"(.*)? computer(.*)?",line,re.I):
        print(response(),np.random.choice(Computer_response))
    elif re.search(r"(.*)?name(.*)?",line,re.I):
        print(response(),np.random.choice(Name_response))
    elif re.search(r"(.*)?sorry(.*)?",line,re.I):
        print(response(),np.random.choice(Sorry_response))
    elif re.search(r"(.*)?I remember you(.*)?",line,re.I):
        print(response(),re.sub("(.*)?i remember you(.*)?",np.random.choice(Userremeber_response),line))
    elif re.search(r"(.*)?I remember(.*)?",line,re.I):
        print(response(),re.sub("(.*)?i remember(.*)?",np.random.choice(Userremeber_response1),line))
    elif re.search(r"(.*)?do you remember your(.*)?",line,re.I):
        print(response(),re.sub("(.*)?do you remember your(.*)?",np.random.choice(Sysremember_response),line))
    elif re.search(r"(.*)?do you remember(.*)?",line,re.I):
        print(response(),re.sub("(.*)do you remember(.*)?",np.random.choice(Sysremember_response1),line))
    elif re.search(r"(.*)?I want(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?i want(.*)?",np.random.choice(Userwants_response),line))
    elif re.search(r"(.*)?if(.*)?",line,re.I):
        print(response(),re.sub("(.*)?if(.*)?",np.random.choice(If_response),line))
    elif re.search(r"(.*)?I dreamt(.*)?",line,re.I):
        print(response(),re.sub("(.*)?i dreamt(.*)?",np.random.choice(Userdreamt_response),line))
    elif re.search(r"(.*)?dream(.*)?",line,re.I):
        print(response(),np.random.choice(Dream_response))
    elif re.search(r"(.*)?my mother(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?my mother(.*)?",np.random.choice(Usermother_response),line))
    elif re.search("(.*)?my father(.*)?",line,re.I):
        print(response(),np.random.choice(Userfather_response))
    elif re.search(r"(.*)?I am glad(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?i am glad(.*)?",np.random.choice(Userglad_response),line))
    elif re.search("(.*)?I am sad(.*)?",line,re.I):
        print(response(),np.random.choice(Usersad_response))
    elif re.search(r"(.*)?are like(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?are like(.*)?",np.random.choice(arelike_response),line))
    elif re.search(r"(.*)?is like(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?is like(.*)?",np.random.choice(islike_response),line))
    elif re.search("(.*)?alike(.*)?",line,re.I):
        print(response(),np.random.choice(alike_response))
    elif re.search("(.*)?same(.*)?",line,re.I):
        print(response(),np.random.choice(same_response))
    elif re.search("(.*)?no (.*)?",line,re.I):
        print(response(),np.random.choice(no_response))
    elif re.search(r"(.*)?I was(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?i was(.*)?",np.random.choice(Userwas_response),line))
    elif re.search(r"(.*)?was I(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?was i(.*)?",np.random.choice(wasuser_response),line))
    elif re.search(r"(.*)?I am (.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?i am(.*)?",np.random.choice(Iam_response),line))
    elif re.search(r"(.*)?am I(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?am i(.*)?",np.random.choice(ami_response),line))
    elif re.search("(.*)?am(.*)?",line,re.I):
        print(response(),np.random.choice(am_response))
    elif re.search(r"(.*)?are you(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?are you(.*)?",np.random.choice(areyou_response),line))
    elif re.search(r"(.*)?you are(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?you are(.*)?",np.random.choice(youare_response),line))
    elif re.search("(.*)?because(.*)?",line,re.I):
        print(response(),np.random.choice(because_response))
    elif re.search(r"(.*)?were you(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?were you(.*)?",np.random.choice(wereyou_response),line))
    elif re.search(r"(.*)?I can't(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?i can't(.*)?",np.random.choice(Usercant_response),line))
    elif re.search(r"(.*)?I feel(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?i feel(.*)?",np.random.choice(Userfeel_response),line))
    elif re.search(r"(.*)?I felt(.*)?",line,re.I):
        print(response(),np.random.choice(Userfelt_response))
    elif re.search(r"(.*)?I (.*)? you(.*)?z",line,re.I):
        print(response(),re.sub(r"(.*)?i(.*)? you(.*)?z",np.random.choice(fantasy_response),line))
    elif re.search(r"(.*)?why don't you(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?why don't you(.*)?",np.random.choice(dontyou_response),line))
    elif re.search(r"(.*)?yes(.*)?",line,re.I): 
        print(response(),np.random.choice(yes_response))
    elif re.search(r"(.*)?someone(.*)?",line,re.I):
        print(response(),np.random.choice(someone_response))
    elif re.search(r"(.*)?everyone(.*)?",line,re.I):
        print(response(),np.random.choice(everyone_response))
    elif re.search(r"(.*)?always(.*)?",line,re.I):
        print(response(),np.random.choice(always_response))
    elif re.search(r"(.*)?what(.*)?",line,re.I):
        print(response(),np.random.choice(what2_response))
    elif re.search(r"(.*)?perhaps(.*)?",line,re.I):
        print(response(),np.random.choice(perhaps_response))
    elif re.search(r"(.*)?are (.*)?",line,re.I):
        print(response(),re.sub(r"(.*)?are(.*)?",np.random.choice(are_response),line))
    elif re.search(r"good (morning|afternoon|evening|night)(.*)?",line,re.I):
        print(response(),re.sub(r"good (morning|afternoon|evening)(.*)?",np.random.choice(Good_response),line))
    elif re.search(r"who is your creator(\?)*",line,re.I):
        print(response(),np.random.choice(Creator_response))
    elif re.search(r"flip a coin",line,re.I):
        print(response(),np.random.choice(Flip_coin_response))
    elif re.search(r"(.*)can you(.*)?me",line,re.I):
        print(response(),re.sub(r"(.*)can you(.*)?me",np.random.choice(canyou1_response),line))
    elif re.search(r"(.*)can you(.*)?",line,re.I):
        print(response(),re.sub(r"(.*)can you(.*)?",np.random.choice(canyou_response),line))
    elif re.search(r"^(bye|exit|good bye)",line,re.I):
        print("Bye and have a nice day :D")
        break
    elif re.search(r"(.*)?tell(.*)?story(.*)?",line,re.I):
        print(response(),np.random.choice(Story_response))
    else:
        print(response(),np.random.choice(default_response))

# Reference for corpus:
# Website url:http://botartisanz.com/blog/create-your-eliza-chatbot-in-20-minutes-with-regular-expressions-day-6
# Author: Jubin Jose
