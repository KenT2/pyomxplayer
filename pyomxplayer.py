import sys, os

# simple python interface to omxplayer
# ------------------------------------
# developed with python 2.7, not tried on python 3.
# +,- commands do not work in Wheezy beta.
# create a folder ~/tmp in home folder first
# videos must be in ~/videos
# you need a long video or else the controls will not work (bug in omxplayer)
# bug - player does not terminate properly if the video runs to its end.
# I haven't a clue what some of the commands do.

# create a fifo to be used between the process and subprocess
os.system("rm ~/tmp/cmd")
os.system("mkfifo ~/tmp/cmd")


while True:
	print("File to Play, bye to exit?")
	file = sys.stdin.readline()
	file = file.rstrip()
	if file == 'bye': break
	
	# start omxplayer in a subprocess (this is the bit that stumped me for a few weeks). Input is from the FIFO, output is to null
	# remove the null output if you want to "Have a Nice Day"
	command = "omxplayer -ohdmi ~/videos/" + file + "<~/tmp/cmd >/dev/null &"
	os.system (command)
	
	while True:
		print (" . - start\n p - pause/play\n spacebar - pause/play\n q - quit\n + - increase volume\n - - decrease volume")
		print (" z - tv show info\n 1 - reduce speed\n 2 - increase speed\n j - reduce audio index\n k - increase audio index\n i - back a chapter\n o - forward a chapter")
		print (" n - reduce subtitle index\n m - increase subtitle index\n s - toggle subtitles\n >cursor - skip forward\n <cursor - skip back\n ^cursor - large forward skip\n _^cursor - large reverse skip")
		# you need to press [enter] after the command. Exercise for the reader to improve this.
		choice = raw_input ('key [enter]')
		# sending q through the FIFO quits omxplayer and terminates the subprocess
		if choice == 'q':
			command="echo -n '" + choice + "'>~/tmp/cmd"
			os.system(command)
			break
		else:
			# send other commands through the FIFO to omxplayer
			command="echo -n '" + choice + "'>~/tmp/cmd"
			print(command)
			os.system(command)
	
print ("bye")
os.quit()
