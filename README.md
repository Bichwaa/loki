## About

### LOKI🧙🏾

A CLI text file encryption tool.

Turn any text file into an intelligible mess of characters and then back to its original form with a simple password. And now your txt file is a vault.

Trivia: In Swahili, loki is a bastardization of the English word "lock" and it it means...lock 😑. And since you're very likely to find mischief where you find encryption...

<h3 style="color:red">Important!</h3>  

- This tool is not battle tested. It uses python standard library's module "Cryptography" to encrypt and decrypt. It is Fernet encryption to be precise.  
- It is meant to be used on text based files although it might work on many other file types.
- don't forget your password/key. 

## Dependencies

- [Python fire](https://github.com/google/python-fire/tree/master)



#### Prerequisites
 - Be mad enouh to consider having python 3
 - Have python 3

#### Installation instructions

- Clone/download repo... 🙄 obviously.
- Open the location of the repo in your favourite terminal (Shame on you if thats CMD prompt)

##### **Linux / macOS**
 `python3 -m venv . `  #If venv is not installed, install it or use your favourite virtual environment initializer.  

 `source bin/activate`  

 `pip install -r requirements`

 ` pip install .`

 ##### **Windows (with shame if you use CMD)**
 `python -m venv . `  #If venv is not installed, install it or use your favourite virtual environment initializer. 

 `Scripts/activate`  
 
 `pip install -r requirements`  

 ` pip install .`

 if everything goes okay, you should be able to use loki, if not, I suggest you don't do anything drastic like reinstalling python or 


## How to use loki:

