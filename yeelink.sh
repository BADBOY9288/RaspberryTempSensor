sudo python /home/pi/temp.py
curl --request POST --data-binary @"/home/pi/datafile.txt" --header "U-ApiKey:0a427c10155a6ae1782784abfa37ba18" http://api.yeelink.net/v1.0/device/172125/sensor/222699/datapoints
