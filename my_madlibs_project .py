# This program is a game that tells you a story if you enter the prompts 

# the welcome message.

welcome_message = """Hi there, I am Ghoxtman.\nI'm your assistant.\nReply the following prompts to hear a story about\
The Greatest Data Scientist yet."""
print(welcome_message, '\n')

#Defining useful variables for the story 

name =  input("Enter your name: ")
name = name.upper()
age = int(input("Enter your age: "))

hobby_1 = input("Enter a game you like to play: ")
hobby_2 = input("Enter an other game you like to play: ")
hobby_1.upper()                                  # capitalising the input
hobby_2.upper()

state = input("Enter any state of your chioce: ")
state = state.upper()                          #capitalising the input 

nickname = input("Give yourself a nickname that relates to what you are studying: ")
year = int(input("Enter your Favourite year: "))
school = input("Enter your favourite university: ")
school = school.upper()                         # capitalising the input

disease = input("Enter one disease that is not curable: ")
country = input("Enter a country you\'ll like to travell to: ")
country = country.upper()                         # capitalising the input

doctor = input("Enter the name of your favourite Doctor: ")
doctor = doctor.upper()                             # capitalising the input



print("\n\n")

message = f'Hello my name is {name} and this is how I became the worlds greatest. I like to {hobby_1} despite being {age} old.\n\
I also like {hobby_2} .\n\
I have decided to choose my own path to become one of the Greatest Data Scientist to walk the earth.\
In the {year},I decided to travell to {state} to pursue my dreams of becoming\
The Greatest Data Scientist.\n\n\
I enrolled in the prestigous {school} and graduated at the top of my class.\
I started practicing the skills I acquired and solving real life problems.\n\
I was fondly called the {nickname} especially by data folks on twitter. Then I fell very i\'ll. The doctors diagnosed me of {disease}.\n\
My whole world came crashing, all my life I have lived as strong and invincible fellow only to be shatter by this {disease}.\
But I did not let that hold me back. I used my skills as a Data Scientist to collect data and find the cause of this disease.\
Despite my health challenge i travelled to {country} in search for answers and to gather data to fight {disease}.\n\n\
While in {country}, I met a Man named Pablo, he was a data scientist too, he has extra ordinary skills in data visualisation.\
With his help and the data I collected I was able to see patterns that leads to one having {disease}. I submited my finding to Dr. {doctor}.\
With his expertise and the aid of the data submitted to him, he and his team developed a permanent solution that will cure {disease} forever.\
I, {name} built a model that could predict this disease early enough and this solution made me rich with over $500 Billion.'


print(message)




