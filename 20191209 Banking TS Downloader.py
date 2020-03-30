import pandas as pd
import numpy as np
from pyjstat import pyjstat
from pprint import pprint
import requests, json
import matplotlib.pyplot as plt


''' DATA SERIES:

__NAME__________SOURCE__FREQ___

- SI RGDP		SURS	Q
- SI HICP  		SURS	M
- SI RPPI 		SURS	Q	
- SI UNEMPL 	SURS	Q
- EURIBOR3M 	ECB  	M
- SI GOV10Y 	FRED	M

+ EU RGDP 		FRED	Q
+ EU HICP  		ECB 	M
+ EA19 CPPI 	ECB 	Q
+ EA19 GOVY 	ECB	 	M


https://stackoverflow.com/questions/40497199/how-to-convert-monthly-data-to-quarterly-in-pandas

'''


datalist = {
	
	'SI_RGDP': {
	'SOURCE' : 'SURS',
	'FREQ' : 'Q',
	'URL'  : 'https://pxweb.stat.si/SiStatDb/pxweb/sl/20_Ekonomsko/20_Ekonomsko__03_nacionalni_racuni__10_03002_BDP_cetrtletni/0300220S.px/',
	'API' : 'https://pxweb.stat.si:443/SiStatDb/api/v1/sl/20_Ekonomsko/03_nacionalni_racuni/10_03002_BDP_cetrtletni/0300220S.px'
	},


	'SI_HICP': {
	'SOURCE' : 'SURS',
	'FREQ' : 'M',
	'URL'  : 'https://pxweb.stat.si/SiStatDb/pxweb/sl/20_Ekonomsko/20_Ekonomsko__04_cene__04006_ICZP/0400600S.px/',
	'API' : 'https://pxweb.stat.si:443/SiStatDb/api/v1/sl/20_Ekonomsko/04_cene/04006_ICZP/0400600S.px'
	},

	'SI_RPPI': {
	'SOURCE' : 'SURS',
	'FREQ' : 'Q',
	'URL'  : 'https://pxweb.stat.si/SiStatDb/pxweb/sl/20_Ekonomsko/20_Ekonomsko__04_cene__04190_ICSN/0419001S.px/',
	'API' : 'https://pxweb.stat.si:443/SiStatDb/api/v1/sl/20_Ekonomsko/04_cene/04190_ICSN/0419001S.px'
	},

	'SI_UNEMPLOYMENT': {
	'SOURCE' : 'SURS',
	'FREQ' : 'Q',
	'URL'  : 'https://pxweb.stat.si/SiStatDb/pxweb/sl/10_Dem_soc/10_Dem_soc__07_trg_dela__02_07008_akt_preb_po_anketi__01_07620_akt_preb_ADS_cetrt/0762003S.px/'
	},

	'EURIBOR3M': {
	'SOURCE' : 'ECB',
	'FREQ' : 'M',
	'URL'  : 'http://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=143.FM.M.U2.EUR.RT.MM.EURIBOR3MD_.HSTA'
	},

	'SIGOV10Y': {
	'SOURCE' : 'FRED',
	'FREQ' : 'M',
	'URL'  : 'https://fred.stlouisfed.org/series/IRLTLT01SIM156N',
	'API' : 'https://api.stlouisfed.org/fred/series/observations?series_id=IRLTLT01SIM156N&api_key=8c0fd5a88740ffebd63b5208ac54ee15&file_type=json&frequency=q'
	},



}

# print('Available data series:\n', datalist.keys())


# SURS 
# url = "https://pxweb.stat.si:443/SiStatDb/api/v1/sl/20_Ekonomsko/03_nacionalni_racuni/10_03002_BDP_cetrtletni/0300220S.px?&transakcije=B1GQ&meritve=L"
# dataset = pyjstat.Dataset.read(url)
# pprint(dataset)


# FRED
url2 = datalist['SIGOV10Y']['API']
dataset = requests.get(url2).json()
data = pd.DataFrame(dataset['observations'])
data.set_index(data['date'], inplace=True)
data["value"] = pd.to_numeric(data["value"], errors="coerce")



print(data.tail())
plt.plot(data['date'], data['value'])
plt.show()

