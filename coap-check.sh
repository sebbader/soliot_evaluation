#!/bin/bash

main() {
  node ./coap-execute.js --uri "$1" --method "$2" | tr -d '\n\r' >> coap_logs/"$3"_coap-log.txt
  echo '' >> coap_logs/"$3"_coap-log.txt
}

today=$1
if [ -z "$today" ]
then
      today=`date +%Y-%m-%d_%H-%M-%S`
fi

END=100
echo "code, time total, target uri, method, date, time" >> coap_logs/"$today"_coap-log.txt
IFS=$'\n' read -d '' -r -a urls < coap_uris.txt

for i in $(seq 1 $END); do
  IFS=$'\n' read -d '' -r -a urls < coap_uris.txt
  for url in "${urls[@]}"; do
    main "$url" get "$today"
  done

  IFS=$'\n' read -d '' -r -a urls < coap_unsafe_uris.txt
  for url in "${urls[@]}"; do
    main "$url""$today" put "$today"
    main "$url""$today" get "$today"
    main "$url""$today" delete "$today"
    main "$url""$today" post "$today"
    main "$url""$today" get "$today"
    main "$url""$today" delete "$today"
  done
done