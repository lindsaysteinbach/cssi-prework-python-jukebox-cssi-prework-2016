#!/usr/bin/env python
#this library allows us to play music
import subprocess


#make sure you edit the music_path to that it points to wherever you cloned this lab
music_path="/Users/administrator/desktop/CSSI/python/jukebox-cli/audio/"

#Here is the song dictionary you will be working with.
songs={"Something Elated": {"artist" : "Broke for Free", "path": music_path + "Broke_For_Free-Something_Elated.mp3", "jukebox_id": 1},
"Springish": {"artist" : "Gillicuddy", "path": music_path + "Gillicuddy-Springish.mp3", "jukebox_id": 2},
"Siesta": {"artist" : "Jahzzar", "path": music_path + "Jahzzar-Siesta.mp3", "jukebox_id": 3},
"Happy Go Lucky": {"artist" : "Scott Holmes", "path": music_path + "Scott_Holmes-Happy_Go_Lucky.mp3", "jukebox_id": 4},
"Favorite Secrets": {"artist" : "Waylon Thorton", "path": music_path + "Waylon_Thorton-Favorite_Secrets.mp3", "jukebox_id": 5}
}

#Add the 4 helper methods and the run() method to the Jukebox class
class Jukebox:
    def help(self):
        print("I accept the following commands:\n"+
        "- help : displays this help message\n"
        "- list : displays a list of songs you can play\n"
        "- play : lets you choose a song to play\n"+
        "- exit : exits this program")


    def list(self,song_list):
        songs=[]
        for (song, info) in song_list.iteritems():
            songs.append("{}. {} - {}".format(info['jukebox_id'],song, info['artist']))
        songs.sort()
        for song in songs:
            print song



    def play(self, song_list):
        user_song=raw_input("Please enter a song name or number:")
        if user_song.isdigit():
            song_exists= False
            for (song,info) in song_list.iteritems():
                if info['jukebox_id'] == int(user_song):
                   song_to_play = song
                   print "Now Playing: {}".format(song)
                   subprocess.call(["afplay", info['path']])
                   song_exists = True
            if song_exists == False:
                print "Invalid input, please try again"
        elif user_song in song_list:
            print "Now Playing: {}".format(user_song)
            subprocess.call(["afplay",song_list[user_song]['path']])
        else:
            print "Invalid input, please try again"

    def exit_jukebox(self):
        print 'Goodbye'

    def run(self, songs):
        self.help()
        user_response=""
        while user_response != "exit":
            user_response=raw_input("Please Enter a Command:")
            if user_response=="list":
                self.list(songs)
            elif user_response=="play":
               self.play(songs)
            elif user_response=="help":
               self.help()
        self.exit_jukebox()
