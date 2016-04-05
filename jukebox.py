
#this module allows us to play music
import subprocess


#make sure you edit the music_path to that it points to wherever you cloned this lab
music_path="/Users/nicki/desktop/CSSI/python/jukebox-cli/audio/"

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
      "replace with code"


    def list(self,song_list):
      "replace with code"



    def play(self, song_list):
      "replace with code"


    def exit_jukebox(self):
      "replace with code"


    def run(self, songs):
      "replace with code"
