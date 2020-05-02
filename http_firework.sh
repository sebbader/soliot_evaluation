today=`date +%Y-%m-%d_%H-%M-%S`
today=$today'1'
END=10

for i in $(seq 1 $END); do 
    python http_check.py $today$i &
    echo "started $i"
done