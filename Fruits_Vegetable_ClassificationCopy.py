import streamlit as st
from PIL import Image
from keras.preprocessing.image import load_img,img_to_array
import numpy as np
from keras.models import load_model
import requests
from bs4 import BeautifulSoup
import cv2
import os

model = load_model('FV.h5')
labels = {0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot', 7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger', 14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
          19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple', 26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn', 32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'}



fruits = ['Apple','Banana','Bello Pepper','Chilli Pepper','Grapes','Jalepeno','Kiwi','Lemon','Mango','Orange','Paprika','Pear','Pineapple','Pomegranate','Watermelon']
vegetables = ['Beetroot','Cabbage','Capsicum','Carrot','Cauliflower','Corn','Cucumber','Eggplant','Ginger','Lettuce','Onion','Peas','Potato','Raddish','Soy Beans','Spinach','Sweetcorn','Sweetpotato','Tomato','Turnip']


def fetch_calories(prediction): 
    try:
        url = 'https://www.google.com/search?&q=calories in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        details.append(int(calories[0:2]))
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)

def fetch_carbs(prediction) :
    try:
        url = 'https://www.google.com/search?&q=carbohydrates in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        details.append(float(calories[0:2]))
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)
    
def fetch_protien(prediction) :
    try:
        url = 'https://www.google.com/search?&q=protein in ' + prediction +" in 100 gm"
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        details.append(float(calories[0:2]))
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)
    

def fetch_fat(prediction) :
    try:
        url = 'https://www.google.com/search?&q=fat in ' + prediction +" in 100 gm"
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        details.append(float(calories[0:2]))
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)

        

def cutphotos() :
    path_to_image="./Photos/togather.jpg"
    image= cv2.imread(path_to_image)
    print(image)
    (h,w) = image.shape[:2]
    centerX, centerY = (w//2), (h//2)
    topLeft = image[0:centerY, 0:centerX]
    topRight = image[0:centerY, centerX:w]
    bottomLeft=image[centerY:h,0:centerX]
    bottomRight = image[centerY:h , centerX:w]
    path =r"./upload_images"
    isWritten= cv2.imwrite(os.path.join(path , 'p1.jpg'), topLeft)
    isWritten= cv2.imwrite(os.path.join(path , 'p2.jpg'), topRight)
    isWritten= cv2.imwrite(os.path.join(path , 'p3.jpg'), bottomLeft)
    isWritten= cv2.imwrite(os.path.join(path , 'p4.jpg'), bottomRight)
    if isWritten:
        print('Image is successfully saved as file.')
    cv2.waitKey(0)



def processed_img(img_path):
    img=load_img(img_path,target_size=(224,224,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    return res.capitalize()



def run():
    # st.title("Fruits🍍-Vegetable🍅 Classification")
    # img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    # print(img_file)
    # if img_file is not None:
    #     img = Image.open(img_file).resize((450,450))
    #     st.image(img,use_column_width=False)
    #     save_image_path = './upload_images/'+img_file.name
    #     with open(save_image_path, "wb") as f:
    #         f.write(img_file.getbuffer())

    #     # if st.button("Predict"):
    #     if img_file is not None:
    #         result= processed_img(save_image_path)
    #         print(result)
    #         if result in vegetables:
    #             st.info('**Category : Vegetables**')
    #         else:
    #             st.info('**Category : Fruit**')
    #         st.success("**Predicted : "+result+'**')
    #         cal = fetch_calories(result)
    #         if cal:
    #             st.warning('**'+cal+'(100 grams)**')
    cutphotos()
    fruitNames = []
    weight = []
    calories = []
    fat = []
    protien = []
    carbs = []
    topLeft = processed_img("./upload_images/p1.jpg")
    topRight = processed_img("./upload_images/p2.jpg")
    bottomLeft = processed_img("./upload_images/p3.jpg")
    bottomRight = processed_img("./upload_images/p4.jpg")
    fruitNames = [topLeft, topRight, bottomLeft, bottomRight]
    print(fruitNames)

run()
