""" Fetch Northern Powergrid outage data """
import requests
import json
import sys

s = requests.session()
s.headers.update({
    'authority': 'www.northernpowergrid.com',
    'origin': 'https://www.northernpowergrid.com',
    'referer': 'https://www.northernpowergrid.com/power-cuts'
})


res = s.post('https://www.northernpowergrid.com/___at')
res.raise_for_status()

at = res.json()['at']

res = s.post('https://www.northernpowergrid.com/powercutsgetallbyincno', data={
    'method': 'incno',
    'categoryFilters': 'Service Cutout Change,Asset repairs by Troublecall,Metering,Emergency Disconnection,Emergency Disconnection (Charge),Cat A,Cat B,Cat C',
    'authenticityToken': at
})
res.raise_for_status()
json.dump(json.loads(res.json()['data']), sys.stdout)
