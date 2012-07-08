#!/bin/sh
    read CC SS FF
    ## echo child: $CC $SS $FF

    if [ $CC = "track" ]; then
        ###play the requested file taking commands from /tmp/omxcmd
        ### remove >/dev/null to see stdout from omxplayer
        # echo $CC $SS $FF
        omxplayer $SS $FF </tmp/omxcmd
        # echo child terminated
	exit
    fi

    # echo DISCARDED $CC $SS $FF

