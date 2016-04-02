# Build a Jukebox

## Objectives
1. Integrate procedural Python basics to create a simple CLI Jukebox.

## What is a CLI?

A CLI, or command line interface, allows a user to interface, or interact with, a computer's operating system or a particular application. In a command line application, the user will respond to a prompt that your program will output to the terminal. The user's response, or input, will be received by the application and the application will then carry out the programmed response based on that input.

For example, I might have a command line application which, once run, will ask the user for their location and in return output the current weather for that location to the terminal.


## Overview

You're going to write a jukebox that introduces itself to the user and then asks for the user's input on the command line.

To demonstrate the example of user input via the command line, let's walk through a quick example in the Python command line. Our program will ask a user for their name, collect the user input via the `user_input()` function, and then say hello to that user. Let's follow the code block below:

Remember, if you are using Python version 3 or higher, use `input()`  instead of `raw_input.`

```python
def say_hello(name):
  return "Hi {}!".format(name)

users_name= raw_input("Enter your name:")
print say_hello(users_name)
```


Your jukebox should respond to 4 commands: `help`, `play`, `list`, and `exit`.

When you run the program in the command line it should greet the user and prompt them for input. Your jukebox should respond to 4 commands: `help`, `play`, `list`, and `exit`.

1. The help command should output instructions for the user on how to use the jukebox.
2. The list command should output a list of songs that the user can play.
3. The play command should ask a user to input a song name or number. It should then output 'Playing Phoenix - 1901' or whatever the song name is.
4. If the user types in exit, the jukebox should say goodbye and the program should shut down.

Let's take a closer look at the methods we'll need to build in order to get our Jukebox up and running as described here.

## Instructions

We'll be building a series of methods that enact the desired behavior of our Jukebox. In `jukebox.py` we'll create a `help`, `play`, `list` and `exit_jukebox` method. Then, we'll build a `run` method that calls on all of these "helper" methods to implement the behavior of our program.

Open up `jukebox.py` and you should see this:

```python

```

This is the list of songs that our jukebox will be working with. The methods we will write will operate on this dictionary of songs.

### The `help` Method

This method should `print` out the following:

```bash
I accept the following commands:
- help : displays this help message
- list : displays a list of songs you can play
- play : lets you choose a song to play
- exit : exits this program
```

### The `list` Method

This method takes in an argument of the `songs` dictionary and `prints` out the jukebox_id, title and artist.

Remember, that dictionaries are unordered, so the list will not be in order of jukebox_id. You can accomplish sorting by somehow getting the output into a list and sorting that list before printing.

```bash
1. Sunday Morning - No Doubt
2. Give it Away - Red Hot Chilli Peppers
3. Santeria - Sublime
```

**Hint:** Use `iteritems` to loop through both the keys and values in the songs dictionary.

### The `play` Method

This method also takes in an argument of the `songs` array. It first `prints` the prompt: `"Please enter a song name or number:"`. It then stores the user's response using `input()`.

If the user's response is a valid jukebox_id number or song name, the method should `print`: `"Now Playing <song name>"`. Otherwise, it should `print`: `"Invalid input, please try again"`.

**Hint:** the `isdigit()` method is one way to check if the user enters a number or a string

### The `exit_jukebox` Method

This method is simple. It `prints`: `"Goodbye"`.

### The `run` Method

This method combines the other methods we built, our "helper" methods, to actually enact the running of our Jukebox.

First, this method should call on the `help` method to show the user the available commands. Then, it should `print` out the prompt: `"Please enter a command:"`. It should capture the user's response using `input()`.

We need to keep our program running as long as the user's input is *not* `"exit"`. Use a loop to continue asking the user for input until or unless their input is `"exit"`. Use conditional statements to determine how your program will respond to a user's input. For example, if their input is `"list"`, call the `list` method, if their input is `"play"`, call the `play` method, if their input is `"help"`, call the `help` method and if their input is `"exit"`, call the `exit_jukebox` method *and* break out of your loop to stop the program.


## Extra: Playing Music from Python

As a bonus, we can use a Python library to play the actual mp3 files in the audio directory of this lab. This is not test-driven but you'll know pretty quickly if it worked because you'll hear the songs!

### Setting Up the Songs Dictionary
In `jukebox.py` make sure to change `music_path` to the correct file path for the `audio` directory. For example, if this jukebox-cli directory is in `Users/<your name>/Desktop/Dev/`, the value of `music_path` should be `Users/<your name>/Desktop/Dev/jukebox-cli/audio/`. If you're not sure what the path to the file is, cd into the directory of this lab in your terminal and type `pwd`. This stands for "print working directory" and will return the path to your current location.

The mp3 files in the audio folder were downloaded from the [Free Music Archive](freemusicarchive.org) which provides a library of free, high quality music files.

### Playing mp3 Files
On a Mac, `afplay()` (which stands for audio file player) will open any mp3.

For example, from the command line, you could type `afplay('Bye_Bye_Bye.mp3')` to start replicating Justin Timberlake's dance moves. To see options like volume control or to indicate how long to play the song for, type `afplay -h`

To stop playing the song, just press <kbd>Control<kbd> + <kbd>Z<kbd> which stops any running process.


####Simulating Command Line Prompts in a Python Script
In order to use command line commands in our Pyhton scripts, we need to import the subprocess module, which replicates calls to the command line. The first parameter in the `call` method is the command which we are replicating. Any arguments that that command might need should follow the first parameter.

```python
subprocess.call(["afplay", "ByeByeBye.mp3"])
```

This is the code that you'll be adding to your `play` method in order to play the audio files we've provided for you. Instead of `ByeByeBye.mp3` being the filename, use the songs_dictionary to access the file path.
