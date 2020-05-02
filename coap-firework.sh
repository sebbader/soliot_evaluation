today=`date +%Y-%m-%d_%H-%M-%S`
today=$today'1'
END=10

for i in $(seq 1 $END); do 
    ./coap-check.sh $today$i &
    echo "started $i"
done