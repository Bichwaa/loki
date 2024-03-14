## About

### LOKI 🧙🏾

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

 if everything goes okay, you should be able to use loki, if not, I suggest you don't do anything drastic like reinstalling python or turning to drugs. Just steal the code from this repo and run it on your file.  Don't open an issue expecting the rest of us to find a solution. Skill issues are a global crisis.


## How to use loki:

Say you have a text file called `file.txt` and you want to hide its content from nosy eyes or whatever. Because its a top secret letter for your babe's eyes only.  

Also say your want the password that locks and unlocks this file to be `top secret, keep out!`,

- to encrypt:  
  You can do it like this  
  `loki enc 'top secret, keep out!' file.txt`  

  Or one of these  
  `loki enc -k 'top secret, keep out!' -f file.txt`
  `loki enc -f file.txt -k 'top secret, keep out!'`  

    Or one of these  
  `loki enc --key 'top secret, keep out!' --filepath file.txt`
  `loki enc --filepath file.txt --key 'top secret, keep out!'`


- to decrypt:  
  You can do it like this  
  `loki dec 'top secret, keep out!' file.txt`  

  Or one of these  
  `loki dec -k 'top secret, keep out!' -f file.txt`
  `loki dec -f file.txt -k 'top secret, keep out!'`  

    Or one of these  
  `loki dec --key 'top secret, keep out!' --filepath file.txt`
  `loki dec --filepath file.txt --key 'top secret, keep out!'`


- to decrypt & print the result to terminal:  
  You can do it like this  
  `loki decp 'top secret, keep out!' file.txt`  

  Or one of these  
  `loki decp -k 'top secret, keep out!' -f file.txt`
  `loki decp -f file.txt -k 'top secret, keep out!'`  

    Or one of these  
  `loki decp --key 'top secret, keep out!' --filepath file.txt`
  `loki decp --filepath file.txt --key 'top secret, keep out!'`


## Cry for help
To encourage the building of more terrible sassy CLI tools, send the developer a meme coin at this address: 0xEca8a4a97aF13d40E196411AA843A18Cea4c4caf

Remeber: meme coins and shit coins are best since the developer refuses to be held half accountable for maintaining this code.