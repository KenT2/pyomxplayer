pyomxplayer uses the ideas recorded at http://www.raspberrypi.org/phpBB3/viewtopic.php?f=38&t=7987 to provide a python wrapper for omxplayer. The test harness I produced to test the wrapper can also be used as simple python based media player using omxplayer.

There is now a different implementation of the python wrapper which uses PEXPECT. It is at https://github.com/jbaiter/pyomxplayer

TBOPlayer in this git repository (KenT2) is a much better gui for omxplayer.


INSTALLATION
============

pyomxplayer.py and omxchild.sh must be in the same directory

to run -  python pyomxplayer.py from a terminal opened in the same directory

track to play is a file name e.g. my_track.mp4

developed with python 2.7, not tried on python 3.

videos must be in a directory set in the main program.

Running this with Idle produces funny results, just run from a terminal.