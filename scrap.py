
# data collection api
# PTT 5 years 2018-12-21 - 2023-12-21
import pandas as pd
import requests

cookies = {
    'visid_incap_2685215': 'Ta4CUOCnSlOpjBWvRC+0TISlemUAAAAAQUIPAAAAAACO4DawQH2amwHM+AV6XZqb',
    'nlbi_2685215': 'OwP9G1FieQRlm2+0aPsPSwAAAADLgiH8deOgKY2Py66cmCM/',
    'route': '3d64b3424ad92089eaa38aa58222db78',
    'incap_ses_1526_2685215': 'jDwzEGB9T2RdpPA8jXEtFZ4ae2UAAAAA3ksMJS3EjPNRcW51PEF20w==',
    'incap_ses_1038_2685215': '6nPdClXx5z7lWuKJpbhnDpQ/fWUAAAAACn0tROPYGSJrm6guG6uUeQ==',
    'SET_COOKIE_POLICY': '20231111093657',
    'incap_ses_411_2685215': 'H37yafXYEUwg0izxaSu0BYcxgWUAAAAAGGA5i6J7ihNZ3Hq0zAVvwQ==',
    'incap_ses_897_2685215': 'dApPehLM3CGBCwB6MclyDGU3gWUAAAAAAIRMv5ksgq2uEO/JYyXUSQ==',
    'incap_ses_1263_2685215': 'ZdobVaPI027k21CraBSHETPSg2UAAAAApr7asB25rqfduGSTDFbMqQ==',
    'charlot': '78be8c86-e6f5-4452-ab6d-07ccd707d77e',
}

headers = {
    'authority': 'www.settrade.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'visid_incap_2685215=Ta4CUOCnSlOpjBWvRC+0TISlemUAAAAAQUIPAAAAAACO4DawQH2amwHM+AV6XZqb; nlbi_2685215=OwP9G1FieQRlm2+0aPsPSwAAAADLgiH8deOgKY2Py66cmCM/; route=3d64b3424ad92089eaa38aa58222db78; incap_ses_1526_2685215=jDwzEGB9T2RdpPA8jXEtFZ4ae2UAAAAA3ksMJS3EjPNRcW51PEF20w==; incap_ses_1038_2685215=6nPdClXx5z7lWuKJpbhnDpQ/fWUAAAAACn0tROPYGSJrm6guG6uUeQ==; SET_COOKIE_POLICY=20231111093657; incap_ses_411_2685215=H37yafXYEUwg0izxaSu0BYcxgWUAAAAAGGA5i6J7ihNZ3Hq0zAVvwQ==; incap_ses_897_2685215=dApPehLM3CGBCwB6MclyDGU3gWUAAAAAAIRMv5ksgq2uEO/JYyXUSQ==; incap_ses_1263_2685215=ZdobVaPI027k21CraBSHETPSg2UAAAAApr7asB25rqfduGSTDFbMqQ==; charlot=78be8c86-e6f5-4452-ab6d-07ccd707d77e',
    'referer': 'https://www.settrade.com/th/technical-chart?symbol=PTT',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

params = {
    'symbol': 'PTT',
    'from': '1422057600',
    'to': '1703203200',
    'resolution': '1D',
    'countback': '1974',
}

response = requests.get(
    'https://www.settrade.com/api/set/technical-chart/history',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.json())

json1=response.json()
ptt_df = pd.DataFrame(json1)
ptt_df = ptt_df.drop(['s'],axis=1)
ptt_df.columns = ['date','close','open','high','low','volume']
ptt_df['date'] = pd.to_datetime(ptt_df['date'], unit='s')

# delta 5 years

cookies = {
    'visid_incap_2685215': 'Ta4CUOCnSlOpjBWvRC+0TISlemUAAAAAQUIPAAAAAACO4DawQH2amwHM+AV6XZqb',
    'nlbi_2685215': 'OwP9G1FieQRlm2+0aPsPSwAAAADLgiH8deOgKY2Py66cmCM/',
    'route': '3d64b3424ad92089eaa38aa58222db78',
    'incap_ses_1526_2685215': 'jDwzEGB9T2RdpPA8jXEtFZ4ae2UAAAAA3ksMJS3EjPNRcW51PEF20w==',
    'incap_ses_1038_2685215': '6nPdClXx5z7lWuKJpbhnDpQ/fWUAAAAACn0tROPYGSJrm6guG6uUeQ==',
    'SET_COOKIE_POLICY': '20231111093657',
    'incap_ses_411_2685215': 'H37yafXYEUwg0izxaSu0BYcxgWUAAAAAGGA5i6J7ihNZ3Hq0zAVvwQ==',
    'incap_ses_897_2685215': 'dApPehLM3CGBCwB6MclyDGU3gWUAAAAAAIRMv5ksgq2uEO/JYyXUSQ==',
    'incap_ses_1263_2685215': 'ZdobVaPI027k21CraBSHETPSg2UAAAAApr7asB25rqfduGSTDFbMqQ==',
    'charlot': '78be8c86-e6f5-4452-ab6d-07ccd707d77e',
}

headers = {
    'authority': 'www.settrade.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'visid_incap_2685215=Ta4CUOCnSlOpjBWvRC+0TISlemUAAAAAQUIPAAAAAACO4DawQH2amwHM+AV6XZqb; nlbi_2685215=OwP9G1FieQRlm2+0aPsPSwAAAADLgiH8deOgKY2Py66cmCM/; route=3d64b3424ad92089eaa38aa58222db78; incap_ses_1526_2685215=jDwzEGB9T2RdpPA8jXEtFZ4ae2UAAAAA3ksMJS3EjPNRcW51PEF20w==; incap_ses_1038_2685215=6nPdClXx5z7lWuKJpbhnDpQ/fWUAAAAACn0tROPYGSJrm6guG6uUeQ==; SET_COOKIE_POLICY=20231111093657; incap_ses_411_2685215=H37yafXYEUwg0izxaSu0BYcxgWUAAAAAGGA5i6J7ihNZ3Hq0zAVvwQ==; incap_ses_897_2685215=dApPehLM3CGBCwB6MclyDGU3gWUAAAAAAIRMv5ksgq2uEO/JYyXUSQ==; incap_ses_1263_2685215=ZdobVaPI027k21CraBSHETPSg2UAAAAApr7asB25rqfduGSTDFbMqQ==; charlot=78be8c86-e6f5-4452-ab6d-07ccd707d77e',
    'referer': 'https://www.settrade.com/th/technical-chart?symbol=DELTA',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

params = {
    'symbol': 'DELTA',
    'from': '1422057600',
    'to': '1703203200',
    'resolution': '1D',
    'countback': '1974',
}

response = requests.get(
    'https://www.settrade.com/api/set/technical-chart/history',
    params=params,
    cookies=cookies,
    headers=headers,
)

json2=response.json()
delta_df = pd.DataFrame(json2)
delta_df = delta_df.drop(['s'],axis=1)
delta_df.columns = ['date','close','open','high','low','volume']
delta_df['date'] = pd.to_datetime(delta_df['date'], unit='s')

# Advanc (ais)

cookies = {
    'visid_incap_2685215': 'Ta4CUOCnSlOpjBWvRC+0TISlemUAAAAAQUIPAAAAAACO4DawQH2amwHM+AV6XZqb',
    'nlbi_2685215': 'OwP9G1FieQRlm2+0aPsPSwAAAADLgiH8deOgKY2Py66cmCM/',
    'route': '3d64b3424ad92089eaa38aa58222db78',
    'incap_ses_1526_2685215': 'jDwzEGB9T2RdpPA8jXEtFZ4ae2UAAAAA3ksMJS3EjPNRcW51PEF20w==',
    'incap_ses_1038_2685215': '6nPdClXx5z7lWuKJpbhnDpQ/fWUAAAAACn0tROPYGSJrm6guG6uUeQ==',
    'SET_COOKIE_POLICY': '20231111093657',
    'incap_ses_411_2685215': 'H37yafXYEUwg0izxaSu0BYcxgWUAAAAAGGA5i6J7ihNZ3Hq0zAVvwQ==',
    'incap_ses_897_2685215': 'dApPehLM3CGBCwB6MclyDGU3gWUAAAAAAIRMv5ksgq2uEO/JYyXUSQ==',
    'charlot': '78be8c86-e6f5-4452-ab6d-07ccd707d77e',
    'incap_ses_1263_2685215': 'YLUdNwtSCx0c84araBSHETsNhGUAAAAAu0lo6m4CXX5SqE3S1P31zw==',
}

headers = {
    'authority': 'www.settrade.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'visid_incap_2685215=Ta4CUOCnSlOpjBWvRC+0TISlemUAAAAAQUIPAAAAAACO4DawQH2amwHM+AV6XZqb; nlbi_2685215=OwP9G1FieQRlm2+0aPsPSwAAAADLgiH8deOgKY2Py66cmCM/; route=3d64b3424ad92089eaa38aa58222db78; incap_ses_1526_2685215=jDwzEGB9T2RdpPA8jXEtFZ4ae2UAAAAA3ksMJS3EjPNRcW51PEF20w==; incap_ses_1038_2685215=6nPdClXx5z7lWuKJpbhnDpQ/fWUAAAAACn0tROPYGSJrm6guG6uUeQ==; SET_COOKIE_POLICY=20231111093657; incap_ses_411_2685215=H37yafXYEUwg0izxaSu0BYcxgWUAAAAAGGA5i6J7ihNZ3Hq0zAVvwQ==; incap_ses_897_2685215=dApPehLM3CGBCwB6MclyDGU3gWUAAAAAAIRMv5ksgq2uEO/JYyXUSQ==; charlot=78be8c86-e6f5-4452-ab6d-07ccd707d77e; incap_ses_1263_2685215=YLUdNwtSCx0c84araBSHETsNhGUAAAAAu0lo6m4CXX5SqE3S1P31zw==',
    'referer': 'https://www.settrade.com/th/technical-chart?symbol=ADVANC',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

params = {
    'symbol': 'ADVANC',
    'from': '1422057600',
    'to': '1703203200',
    'resolution': '1D',
    'countback': '42',
}

response = requests.get(
    'https://www.settrade.com/api/set/technical-chart/history',
    params=params,
    cookies=cookies,
    headers=headers,
)

json3=response.json()
advanc_df = pd.DataFrame(json3)
advanc_df = advanc_df.drop(['s'],axis=1)
advanc_df.columns = ['date','close','open','high','low','volume']
advanc_df['date'] = pd.to_datetime(advanc_df['date'], unit='s')

ptt_df.to_csv('ptt_df.csv',index=True)
delta_df.to_csv('delta_df.csv',index=True)
advanc_df.to_csv('advanc_df.csv',index=True)