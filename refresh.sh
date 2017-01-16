#!/bin/bash
working_dir=$(pwd)

LASTFILE=$( ls -t | head -n1 )
FULLPATH=$( readlink -f ${LASTFILE} )
echo $FULLPATH

psql revmax_dev -v LAST_FILE="${FULLPATH}" -f /home/ubuntu/scripts/refresh_events.sql