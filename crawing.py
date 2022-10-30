import requests
import pandas as pd

"""
소상공인시장진흥공단_상가(상권)정보_API
"""

serviceKey = 'A7sYOSfH5sou0Un0tp8+fPAZcyHvnOs0i438bZsLCbmBFVR3aM94Gd4C+NE5NjCGoSAmYY/RnpRFvu/4pDLGag=='
url = f'http://apis.data.go.kr/B553077/api/open/sdsc2/storeZoneOne?key={key}&ServiceKey={serviceKey}'
date = '20220101'
key = ''

params ={'serviceKey' : serviceKey, 'key': key, 'type' : 'json'}

response = requests.get(url, params=params).text
print(response)