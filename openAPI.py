#https://www.forest.go.kr/kfsweb/opda/dataMng/pblicDataView.do?pblicDataId=PBD0000055&tabs=3&mn=NKFS_06_08_02

#import urllib2
#from urllib2 import Request, urlopen
from urllib import parse
import requests

url = 'http://apis.data.go.kr/1400000/service/cultureInfoService/mntInfoOpenAPI'
queryParams = '?' + parse.urlencode({ parse.quote_plus('ServiceKey') : '서비스키', 
                                    parse.quote_plus('searchWrd') : '북한산' })

request = requests(url + queryParams)
request.get_method = lambda: 'GET'
response_body = request.urlopen.read()
print(response_body)