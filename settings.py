# -*- coding: utf-8 -*-
"""
Created on Tuesday March 29 03:00:00 2022

@author: Adamu Ayanfeoluwa Samuel. @ayanfe2345 on github.
Comments and explanations done by Adamu Ayanfeoluwa.
@Teacher: Olufemi Victor Tolulope

This settings page helps to dynamically adjust the app content based on the model selected to be used.

This includes, the demo served by the app, the thresh hold, and other descriptive content.
"""


class model_influencer:
    def __init__(self, name) -> None:
        self.name = name

# Reset everything to conform based on the model selected.

    def set_params(self):

        # if crop disease model is selected
        if self.name == "crop_disease":
            self.detectables = "This contains the list of what the A.I can detect in order of best accuracy.<p> </p>Blueberry leaf <p> </p> Tomato leaf yellow virus <p> </p> Peach leaf <p> </p> Raspberry leaf <p> </p> Strawberry leaf <p> </p> Tomato Septoria leaf spot <p> </p> Tomato leaf <p> </p> Corn leaf blight <p> </p> Bell_pepper leaf <p> </p> Potato leaf early blight <p> </p> Tomato mold leaf <p> </p> Tomato leaf bacterial spot <p> </p> Soyabean leaf <p> </p> Bell_pepper leaf spot <p> </p> Tomato leaf mosaic virus <p> </p> Squash Powdery mildew leaf <p> </p> Apple leaf <p> </p> Potato leaf late blight <p> </p> Cherry leaf <p> </p> grape leaf <p> </p> Tomato leaf late blight <p> </p> Tomato Early blight leaf <p> </p> Apple rust leaf <p> </p> Apple Scab Leaf <p> </p> grape leaf black rot <p> </p> Corn rust leaf <p> </p> Corn Gray leaf spot <p> </p> Soybean leaf <p> </p> Potato leaf <p> </p> Tomato two spotted spider mites leaf <p> </p>"
            self.type = "search"
            self.initial_threshold = 0.5
            self.demo1 = "tempDir/crop_disease_test_01.jpg"
            self.demo2 = "tempDir/crop_disease_test_02.jpg"
            self.demo3 = "tempDir/crop_disease_test_03.jpg"
            self.string1 = "what is "
            self.string2 = "Latest on curing "
            self.string3 = "how to cure "

            #If the fruits harvest model is selected
        elif self.name == "fruits_harvest":
            self.type = "search"
            self.detectables = "This contains the list of what the A.I can detect in order of best accuracy. <p> </p> Beetroot <p> </p> Avocado<p> </p> Kiwi <p> </p> Peach<p> </p> Mandarine <p> </p> Orange <p> </p> Ginger <p> </p> Banana <p> </p> Kumquats <p> </p> Onion <p> </p> Cactus <p> </p> Plum <p> </p> Kaki <p> </p> Tomato <p> </p> Pineapple <p> </p> Cauliflower <p> </p> Pepper <p> </p> Melon <p> </p> Nectarine <p> </p> Papaya <p> </p> Pear <p> </p> Redcurrant <p> </p> Apple <p> </p> Huckleberry <p> </p> Guava <p> </p> Limes <p> </p> Granadilla <p> </p> Lemon <p> </p> Mango <p> </p> Strawberry <p> </p> Physalis <p> </p> Quince <p> </p> Kohlrabi <p> </p> Pepino <p> </p> Rambutan <p> </p> Salak <p> </p> Eggplant <p> </p> Maracuja <p> </p> Nut <p> </p> Walnut <p> </p> Grapefruit <p> </p> Mangostan <p> </p> Pomegranate <p> </p> Hazelnut <p> </p> Mulberry <p> </p> Tamarillo <p> </p> Tangelo <p> </p> Cantaloupe <p> </p> Potato <p> </p> Chestnut <p> </p> Cherry <p> </p> Clementine <p> </p> Lychee <p> </p> Apricot <p> </p> Dates <p> </p> Cocos <p> </p> Pomelo <p> </p> Grape <p> </p> Passion <p> </p> Carambula <p> </p> Blueberry <p> </p> Pitahaya <p> </p> Raspberry <p> </p>"
            self.initial_threshold = 0.3
            self.demo1 = "tempDir/syn_fruit01.PNG"
            self.demo2 = "tempDir/syn_fruit02.PNG"
            self.demo3 = "tempDir/syn_fruit03.PNG"
            self.string1 = ""
            self.string2 = "Top health benefits"
            self.string3 = "Health benefits of "

            #if the weeds model is selected.
        elif self.name == "weeds":
            self.type = "search"
            self.detectables = "This contains the list of what the A.I can detect in order of best accuracy. <p> </p> Weeds <p> </p>"
            self.initial_threshold =0.6
            self.demo1 = "tempDir/weed_test_01.jpg"
            self.demo2 = "tempDir/weed_test_02.jpg"
            self.demo3 = "tempDir/weed_test_03.jpg"
            self.string1 = "what are "
            self.string2 = "Some advice on removing weeds"
            self.string3 = "how to remove "

            #if the Chicken model is selected.
        elif self.name == "chicken":
            self.type = "count"
            self.detectables = "This contains the list of what the A.I can detect in order of best accuracy. <p> </p> Chicken <p> </p>"
            self.initial_threshold = 0.5
            self.demo1 = "tempDir/chick001.jpg"
            self.demo2 = "tempDir/chick002.jpg"
            self.demo3 = "tempDir/chick003.jpg"
