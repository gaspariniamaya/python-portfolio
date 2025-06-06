 #Amaya Gasparini - Period 4 - 2/24/2025
#Vacation Recommender
#Init
from PIL import Image
import requests
from io import BytesIO
import random

vacaList = ["https://tinyurl.com/f6x4j8r3", #Rio
            "https://tinyurl.com/4nways2p", #Rome
            "https://tinyurl.com/5brkakns", #Maui
            "https://tinyurl.com/2tt4ynx5", #New York
            "https://tinyurl.com/23thkeze" #Bali
            ]
def open_image(url): #code that makes it possible to print out images
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def vaca_recommender():
    print("Welcome to the Vacation Recommender")
    while True:
        ans = input("Would you like a recommendation? Enter: ") #intro to the program
        if ans == "yes" or ans == "y":
            randomPlace = random.randint(0,4) #chooses a random location
            if randomPlace == 0: #prints an image of each place and gives a brief description
                open_image(vacaList[0])
                print("Description: Rio de Janiero is a huge coastal city in the southeast side of Brazil. It is known for its beautiful Christ the Redeemer statue and Sugarloaf Mountain, with a trolly cart attached on top that gives you an amazing view of the city. It is social, tropical, and full of life with beautiful beaches.")
            elif randomPlace == 1:
                open_image(vacaList[1])
                print("Description: Rome is the capital city of Italy. It is a metropolitan city known for its ancient history, art, architecture, and culture. Some of its most famous attractions include the Colosseum Arena, the Vatican City chapel, and the Trevi Fountain.")
            elif randomPlace == 2:
                open_image(vacaList[2])
                print("Description: Maui is a Hawaiian island belonging to the Central Pacific. This is the spot if you enjoy stunning beaches. Maui is known for its white sand stretches like Ka'anapali Beach and its dramatic volcanic landscape at Haleakalā National Park. The park also provides opportunities such as whale watching, snorkeling, and hiking if you are interested in a bit of an adventure.")
            elif randomPlace == 3:
                open_image(vacaList[3])
                print("Description: New York is the place for you if you would like to explore a big and busy city in the USA with many fun things to do. They are most known for the beautiful Statue of Liberty and Central Park, which extends about 2.5 miles.")
            elif randomPlace == 4:
                open_image(vacaList[4])
                print("Description: Bali is a province of Indonesia and the westernmost of the Lesser Sunda Islands. It is famous for its beautiful beaches, green rice paddies, and unique culture. This is the place for you if you want a calm and relaxing vacation by the ocean and nature.")
        else:
                print("Visit again some other time!")
                break


#intro
#ask for input

#Generate a random number between 0 , 4 or 2. use random.choice()

#Main
vaca_recommender()



#SOURCES
#RIO: Accessed at https://whc.unesco.org/uploads/thumbs/site_1100_0004-750-750-20120625114004.jpg - Article:Rio de Janeiro: Carioca Landscapes between the Mountain and the Sea - Website: Unesco.org - Author:Ruy Salaverry - License: All rights reserved - Date: 01/08/2009
#ROME: Accessed at https://cdn.britannica.com/16/99616-050-72CD201A/Colosseum-Rome.jpg - Article: Rome - Website: britannica.com - Author: Encyclopædia Britannica
#MAUI: Accessed at https://hips.hearstapps.com/hmg-prod/images/road-to-hana-maui-hawaii-royalty-free-image-1716563729.jpg?crop=0.668xw:1.00xh;0.167xw,0&resize=1200:* - Article: How to Spend a Perfect Long Weekend on Maui - Website: veranda.com - Author: wingmar // getty images
#NEW YORK: Accessed at https://idsb.tmgrup.com.tr/ly/uploads/images/2024/04/09/thumbs/800x531/323101.jpg - Article: Times Square at 120: Historic milestone for New York City - Website: dailysabah.com - Author: Shutterstock
#BALI: Accessed at https://image.urlaubspiraten.de/4x3/image/upload/v1603282722/mediavault_images/ihjatwhtozn7ljfgtad7.jpg - Article: Explore Bali: A Comprehensive Guide to the Island of the Gods - Website: travelpirates.com - no info found on picture sources
