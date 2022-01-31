#!/bin/sh
curl -s https://ssen-powertrack-api.opcld.com/gridiview/reporter/info | jq . > ssen.json

curl -s 'https://www.enwl.co.uk/power-outages/search?pageSize=1000&postcodeOrReferenceNumber=&pageNumber=1&includeCurrent=true&includeResolved=false&includeTodaysPlanned=false&includeFuturePlanned=false&includeCancelledPlanned=false' | jq . > enwl.json

python3 ./scraper/fetch_npg.py > ./npg.json
