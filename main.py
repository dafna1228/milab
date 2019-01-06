import boto3
import os
import pygame
from playsound import playsound
from time import sleep

pygame.mixer.init()
#playsound('song.mp3')

if __name__ == "__main__":
    Car = 'Sound_Car.mp3'
    Nature = 'Sound_Nature.mp3'
    Sign = 'Sound_Sign.mp3'
    imageFile = 'footage.jpg'
    client = boto3.client('rekognition', 'eu-west-1', aws_access_key_id='ASIA4QPZ4Y5UK5EWKOOH', aws_secret_access_key='n/pyrQlDOCdpIUYI+YyeQkzXfZWJCLMzsqNIQa9A', aws_session_token="FQoGZXIvYXdzEOv//////////wEaDMmM4ZNTwbB7MPv2gyLrAguyXZggqT6YOQaHa4m1/GMI+sl0ua+uo/pRG/mYYg0Ye7D3DHOYpAldPKQzq5appNG67EjM3FZuYhYTo/9Sphy/UWuXua4qc8Eazgwz3nHUEPgPqrOf8nraRy/AidOu2dnjiIq7yEPklxzuagki8CIX4vdCfGvsj1JThNsh0NAp7TrFJSsr+YySt9gXN1oLklknpyzganm2gLHomZLpIEOJ0ZQ1O83spcGKR4wbGIMbm08Xwq7cLxoBN8M6FHX81udJO3zH3eVmZvDy5BoPsA9Q6in0mf0TRazPmSzn3wHJz8ltfbh35vok+As6fRUtEZeANGV2gdixh2/e1LZO9iWsdz1lp65JiCgjZjI+M/QR4SBSczJm/RwUIyX8i1su38JAg6a3VYzfy6dP2k+XgAmt8kstjX1uYtH3NjVLQZgoKStoqF1QvZSDvJaZMr8c1qC1o55Ugs7R1DSbvfhmWfev+KgzaF74niR4eyiLncfhBQ==")
    while True:
            for filename in os.listdir(os.getcwd() + '/images'):
                with open(imageFile, 'rb') as image:
                    response = client.detect_labels(Image={'Bytes': image.read()})
                print(response)
                lst = response['Labels']
                results = {}
                for i in lst:
                    results[i['Name']] = i['Confidence']
                if results.get('Car') > 50:
                    pygame.mixer.music.load(Car)
                    pygame.mixer.music.play()
                elif results.get('Nature') > 50:
                    pygame.mixer.music.load(Nature)
                    pygame.mixer.music.play()
                elif results.get('Words') > 50:
                    pygame.mixer.music.load(Sign)
                    pygame.mixer.music.play()
                os.remove(os.getcwd() + '/images/' + filename)
                results = {}
            for label in response['Labels']:
                print(label['Name'] + ' : ' + str(label['Confidence']))
    print('Done...')