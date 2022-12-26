#!/bin/bash 


#date +%S
d=`date +%S`
start_time="12:45:00"
end_time="04:45:00"
d_h=`date +%H`
d_m=`date +%M`
start_time_h=12
end_time_h=16
start_time_m=00
end_time_m=20
echo $d_h $d_m
echo "$d_h -ge $start_time_h && $d_h -le $end_time_h && $d_m -ge $start_time_m && $d_m -le $end_time_m"
while [[ $d_h -ge $start_time_h && $d_h -le $end_time_h && $d_m -ge $start_time_m && $d_m -le $end_time_m ]];
do
    # echo "Time now : date +%T"
    python /home/vvdn/Videos/Project/Updated_NEW/mysite/manage.py runserver 172.17.166.37:7000
    d_h=`date +%H`
    d_m=`date +%M`
    echo "$d_h $d_m"
    break
done
    #while [[ $(date +%S) -gt $start_time || $(date +%S) -lt $end_time ]];