# Recommendation engine
This project takes natural language inputs from the user and provides restaurant recommendations based on a semantic undertanding of the reviews of the restaurant 

## How this works
## Setup
clone this project to your local and run
```
pip install -r requirements.txt
```
to install the requirements

Then run the following command:
```
flask --app run run
```
to start the flask server

## Send requests to the endpoints

There are 2 main endpoints i this project:
1. "/corpus_encoding": this adds an new review to the existing corpus of reviews

   Request type: POST
   Body: json
   sample format:
    {
    "cafe_name":"Jalsa",
    "review":"A gorgeous place for dining"
   }
2. "/top_5" : this returns the top 5 recommended restaurants given a user input

   Request type: POST
   Body: json
   sample format:
   {
    "prompt": "Best places to eat with friends"

  }
   Return format: list
   [
    "Energy Addaa",
    "C Corner",
    "Chutney Chang",
    "Chill Out",
    "Thamboola"
]
   
   
