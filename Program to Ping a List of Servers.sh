#!/bin/bash
# ping_servers.sh
# Script to ping a list of servers and log their status

SERVER_LIST="servers.txt"         # Input file with server names/IPs
LOG_FILE="ping_results.log"       # Output log file

echo "===================================" >> $LOG_FILE
echo "Server Ping Report - $(date)" >> $LOG_FILE
echo "===================================" >> $LOG_FILE

# Read each server from file
while read -r server
do
    if [ -n "$server" ]; then
        echo -n "Pinging $server ... "
        ping -c 2 "$server" &> /dev/null

        # Check if ping was successful
        if [ $? -eq 0 ]; then
            echo "UP ✅"
            echo "$server - UP" >> $LOG_FILE
        else
            echo "DOWN ❌"
            echo "$server - DOWN" >> $LOG_FILE
        fi
    fi
done < "$SERVER_LIST"

echo "===================================" >> $LOG_FILE
echo "Ping check completed at $(date)" >> $LOG_FILE
echo "===================================" >> $LOG_FILE

echo "Report saved to $LOG_FILE"
