# How to connect chatGPT with a mySQL database
# Roni Bandini, December 2024
# https://bandini.medium.com
# MIT License
# pip3 install mysql-connector
# pip3 install openai

import mysql.connector
from mysql.connector import Error
from openai import OpenAI
import json
import requests
import sys
import os


# settings
chatGPTKey      = ""
model		='gpt-4o'

os.system('cls')
print("ChatGPT accesing a mySQL database - Roni Bandini - Dec 2024")
print("")

def get_cream(purpose):
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',
            database='creams',
            user='root',
            password=''
        )

        if connection.is_connected():

            # Create a cursor to execute SQL queries
            cursor = connection.cursor(dictionary=True)

            # Define the query to fetch a row
            query = "SELECT description, price FROM products, categories_products, categories WHERE products.idProduct=categories_products.idProduct AND LCASE(categories.categoryDesc)= LCASE('"+purpose+"') ORDER by RAND();"
            print("..."+query)

            # Execute the query
            cursor.execute(query)

            # Fetch one row
            row = cursor.fetchone()

            if row:
                print("...Fetched row from db:", row)
                description=row['description']
                price=row['price']
            else:
                print("...No row matches the condition.")
                description="There are no products for that"
                price=0

            #print(row['description'])
            #print(row['price'])
            return {
                "description": description,
                "price": price
            }


    except Error as e:
        print("...Error while connecting to MySQL", e)

    finally:
        # Ensure the connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()

# --------------------------------------------------------------
# Initiate OpenAI API
# --------------------------------------------------------------

client = OpenAI(api_key=chatGPTKey,)

# --------------------------------------------------------------
# Prompt
# --------------------------------------------------------------

prompt = input('Enter your question: ')


function_descriptions = [
    {
        "name": "get_cream",
        "description": "Get cream description and price from an external mysql database",
        "parameters": {
            "type": "object",
            "properties": {
                "purpose": {
                    "type": "string",
                    "description": "The cream purpose. Example: beauty",
                }
            },
	    "additionalProperties": False,
            "required": ["purpose"],
        },
    }
]

# --------------------------------------------------------------
# Make the API Call
# --------------------------------------------------------------

print("")
print("...Making the first chatGPT API call")

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user", "content": prompt}
  ],
  functions=function_descriptions,
  function_call="auto"
)

# --------------------------------------------------------------
# Extract the results
# --------------------------------------------------------------

output = completion.choices[0].message

if output.function_call==None:
    print(output.content)
    sys.exit()

purpose = json.loads(output.function_call.arguments).get("purpose")

print("...Extracted cream purpose: "+purpose)

# Call the mysql database query function
answer=get_cream(purpose)
price=float(answer['price'])
description=answer['description']

print('...mySQL returned '+description+" at $"+str(price))

# --------------------------------------------------------------
# Make chatGPT second call to write the answer with the data
# --------------------------------------------------------------

print("...Making a second chatGPT call to rephrase")

if price>0:
    prompt2="Can you write a 30 word paragraph about the benefits of the herbal cream named "+description+" priced $ "+str(price)
else:
    prompt2="You are a shop representative informing a customer you dont have in stock a cream for "+purpose+" and suggest a natural. Please return only the message to the customer."

completion = client.chat.completions.create(
        model=model,
        messages=[
    {"role": "user", "content": prompt2}
        ],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.2,
    )

# --------------------------------------------------------------
# Extract the results
# --------------------------------------------------------------

finalAnswer=completion.choices[0]
print("")
print(finalAnswer.message.content.strip())

