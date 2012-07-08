pyomxplayer
===========

pyomxplayer uses the ideas recorded here http://www.raspberrypi.org/phpBB3/viewtopic.php?f=38&t=7987
to produce a simple python based video player using omxplayer

It can be used as a stand alone player or the omx_play can be used in your program.

Instructions

pyomxplayer.py and omxchild.sh must be in the same directory
to run -  python pyomxplayer.py from a terminal opened in the same directory
track to play is a file name e.g. my_track.mp4

developed with python 2.7, not tried on python 3.
+,- commands do not work in Wheezy beta 18/08 unless you have installed a later version of omxplayer.
videos must be in a directory set in the main program.
you need a long video or else the controls will not work (bug in omxplayer)
Running this with Idle produces funny results, just run from a terminal.