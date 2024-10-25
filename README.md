# Remote PC Lock

This is a simple server that will lock windows machine on API call.
Tested on Windows 11 machine.
This essensienly simpler version of [Airytec Switch Off](https://www.airytec.com/en/switch-off/) API but since it's bugged and doesn't have 'Predefined scripts' working in the API, I just wrote it myself. 

## Installation
There is no instalation, just run the script.
In order to have the script running when the PC start, you can put it in "shell:startup" (AKA: %AppData%\Microsoft\Windows\Start Menu\Programs\Startup)

## API 
localhost:55443/lock - Will lock PC \
localhost:55443/heartbeat - Heartbeat \
Anything else yeild 404.
