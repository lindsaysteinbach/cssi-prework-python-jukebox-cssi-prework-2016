import unittest
from cStringIO import StringIO
import sys
from jukebox import Jukebox
from contextlib import contextmanager


@contextmanager
#change raw_input() to input() for Python 3 and higher
def mockRawInput(mock):
    original_raw_input = __builtins__.raw_input
    __builtins__.raw_input = lambda _: mock
    yield
    __builtins__.raw_input = original_raw_input


class TestJukebox(unittest.TestCase):
    def setUp(self):
        self.songs={"Sunday Morning" : {"artist" : "No Doubt", "path": "songs/path", "jukebox_id": 1},
                    "Give it Away" : {"artist" : "Red Hot Chilli Peppers", "path": "songs/path", "jukebox_id": 2},
                    "Santeria" : {"artist" : "Sublime", "path": "songs/path", "jukebox_id": 3}}
        self.jukebox=Jukebox()
        #this allows us to test the output to the terminal, stdout
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdout = self.held

    def test_help(self):
        """It prints a list of commands"""
        self.jukebox.help()
        self.assertEqual(sys.stdout.getvalue(), "I accept the following commands:\n"+
        "- help : displays this help message\n"
        "- list : displays a list of songs you can play\n"
        "- play : lets you choose a song to play\n"+
        "- exit : exits this program\n")

    def test_list(self):
        """It lists the songs by jukebox_id, name and artist"""
        self.jukebox.list(self.songs)
        self.assertEqual(sys.stdout.getvalue(),"1. Sunday Morning - No Doubt\n"+
        "2. Give it Away - Red Hot Chilli Peppers\n"+
        "3. Santeria - Sublime\n")

    def test_play_1(self):
        """It plays Sunday Morning when `1` is entered by the user"""
        with mockRawInput('1'):
            self.jukebox.play(self.songs)
            self.assertEqual(sys.stdout.getvalue(),"Now Playing: Sunday Morning\n")

    def test_play_11(self):
        """It prints an error message when `11` is entered by the user"""
        with mockRawInput('11'):
            self.jukebox.play(self.songs)
            self.assertEqual(sys.stdout.getvalue(),"Invalid input, please try again\n")

    def test_play_Santeria(self):
        """It plays Santeria when `Santeria` is entered by the user"""
        with mockRawInput('Santeria'):
            self.jukebox.play(self.songs)
            self.assertEqual(sys.stdout.getvalue(),"Now Playing: Santeria\n")

    def test_play_Bye_Bye_Bye(self):
        """It prints an error message when `Bye Bye Bye` is entered by the user"""
        with mockRawInput('Bye Bye Bye'):
            self.jukebox.play(self.songs)
            self.assertEqual(sys.stdout.getvalue(),"Invalid input, please try again\n")

    def test_exit_jukebox(self):
        """It prints 'Goodbye'"""
        self.jukebox.exit_jukebox()
        self.assertEqual(sys.stdout.getvalue(),"Goodbye\n")

    def test_run(self):
        """It will ask for a new command after listing the songs"""
        with mockRawInput('exit'):
            self.jukebox.run(self.songs)
            self.assertEqual(sys.stdout.getvalue(),"I accept the following commands:\n"+
            "- help : displays this help message\n"+
            "- list : displays a list of songs you can play\n"+
            "- play : lets you choose a song to play\n"
            "- exit : exits this program\n"+
            "Goodbye\n")



if __name__ == '__main__':
    unittest.main()
