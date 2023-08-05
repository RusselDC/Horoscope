import urllib3;
from bs4 import BeautifulSoup
from tqdm import tqdm
horoscope = {
    'ARIES' : 1,
    'TAURUS' : 2,
    'GEMINI': 3,
    'CANCER':4,
    'LEO':5,
    'VIRGO':6,
    'LIBRA':7,
    'SCORPIO':8,
    'SAGITTARIUS':9,
    'CAPRICON':10,
    'AQUARIUS':11,
    'PISCES':12
}

name = input("What's your horoscope? :")

if name in horoscope:
    url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=" + str(horoscope[name.strip().upper()])
    r = urllib3.PoolManager().request('GET',url).data
    soup = BeautifulSoup(r, 'html.parser')
    main = soup.find('div', class_='main-horoscope')
    matches = soup.find('div',class_='inner flex-center-inline')
    details = matches.find_all('a', class_='flex-center-column')
    print('Compatibilities...')
    for d in details:
        print(d.find('h4').get_text()+" : "+d.find('p').get_text())
    paragraphs = main.find_all('p')
    print('Daily Quotes')
    for p in paragraphs:
        print(p.get_text())
        break
else:
    print("THERE'S NO HOROSCOPE WITH THAT NAME!")
