#Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
#choco install pip
#pip install beautifulsoup4
#pip install google
#& C:/Users/dns/AppData/Local/Programs/Python/Python37-32/python.exe -m pip install -U requests --user
'''
https://www.geeksforgeeks.org/performing-google-search-using-python-code/

query : query string that we want to search for.
tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
lang : lang stands for language.
num : Number of results we want.
start : First result to retrieve.
stop : Last result to retrieve. Use None to keep searching forever.
pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
'''
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

try: 
    import requests
except ImportError:  
    print("No module named 'requests' found") 


try: 
    from bs4 import BeautifulSoup as bs
except ImportError:  
    print("No module named 'BeautifulSoup' found")

try: 
    import datetime
except ImportError:  
    print("No module named 'datetime' found") 



def check_cy(j):
    Cont_ya = ('http://counter.yadro.ru/values?site=' +(j.split('/')[2]).strip() )
    session = requests.Session()
    request = session.get(Cont_ya, headers=headers)
    if request.status_code == 200 and 'LI_error' not in str(bs(request.content, 'html.parser')) :
        soup = bs(request.content, 'html.parser')
        pre=soup.text
        pre=(pre.split('=')[3].split(';')[0])
    else:
        pre=100000
    return(pre)
    

# to search 
#query = "Сиськи"
query  = input("Please, enter the request for search engine:")
vizit_limit = 10000
now = str(datetime.datetime.now()).split('.')[0]
headers = {'accept': '*/*' , 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' }
outputfile = now + ".txt"
outputfile = outputfile.replace(' ','-')
outputfile = outputfile.replace(':','-')
myfile = open(outputfile , mode='w' , encoding='utf-8')

#Открыть файл
  
for i in search(query, tld="ru", num=1, stop=None, pause=2): 
    #Cont_ya = ('http://counter.yadro.ru/values?site=' +(j.split('/')[2]) )
    if int(check_cy(i)) > vizit_limit:
        print(i)#write to file
        myfile.write(i)
        myfile.write('\n')

myfile.close()
