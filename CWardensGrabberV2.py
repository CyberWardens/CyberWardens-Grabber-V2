from __future__ import print_function
import os
import sys,os,re,socket,binascii,time,json,random,threading,Queue,pprint,urlparse,smtplib,telnetlib,os.path,hashlib,string,urllib2,glob,sqlite3,urllib,argparse,marshal,base64,colorama,requests
from colorama import *
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
import socket
import requests,os
import time,re
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore,Style, init
import requests,re,time,random ,os, sys, socket
from multiprocessing.dummy import Pool
from colorama import Fore
from bs4 import BeautifulSoup
from colorama import Fore
from colorama import init
from termcolor import colored
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pyfiglet
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
sd  =   Style.DIM  
colorama.init()
os.system('cls')



print(fm+'''
         ______      __             _       __               __               
        / ____/_  __/ /_  ___  ____| |     / /___ __________/ /__  ____  _____
       / /   / / / / __ \/ _ \/ ___/ | /| / / __ `/ ___/ __  / _ \/ __ \/ ___/
      / /___/ /_/ / /_/ /  __/ /   | |/ |/ / /_/ / /  / /_/ /  __/ / / (__  ) 
      \____/\__, /_.___/\___/_/    |__/|__/\__,_/_/   \__,_/\___/_/ /_/____/  
           /____/                                                             
                      '''+'\033[90m'+'''- Copyright '''+'\033[92m'+'''[2023]'''+'\033[91m'+''' [@ShiroMoriaty]'''+'\033[0m'+fc+''' [CWardensGrabberV2]''')


ttr = '''\n\n
\t\t 1 - Grabing IPs Options ( 1: By Domains,2: By API) \n
\t\t 2 - Reverse IPs ( IPs -> Domains ) \n
\t\t 3 - List optimisation ( - Add Http:// - remove Http:// )\n
\t\t 4 - Grabbing Websites from Zone-Xsec\n
\t\t 5 - Grabbing Websites from Zone-H\n
\t\t 6 - Grabbing Websites using TLD
'''

print((colored(ttr, 'magenta', 'on_green')))
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\033[0m'
bzl = "\t\t[>]Enter your option :"
vet = '\n\t\t[>]Domains List:'
vlz = '[GRABBING ... ]'
dde = '[WAITING ... ]'
ftf = '\t\t[>]PHPSESSID:'
tlt = '\t\t[>]ZHE:'
wtr = '\t\t[>]NOF:'
vanip = '\t\t[+] Grabbing {} Domain | Page {}'
exptx = '\t\tENTER TLD (for example: com, gov, org,etc..) :'
ego = '\t\t[+] {} :Grabbed'
ego1 = '\t\t[>]Enter the first page number:'
ego2 = '\t\t[>]Enter the last page number:'


zelta ='''
\t\t1. usings.ru API1\n
\t\t2. bitverzo.com API2\n 
\t\t3. macrobyte.net API3\n
\t\t4. viewsforcash.com API4'''

delma = '\t\t[>]Choose :'
bbv = "\n\t\t[>]1:By domains\ 2: by API :"

zerf ='''
\t\t 1-Removes Http Or Https \n 
\t\t 2-Add Http or Https\033[0m '''

ztbot = raw_input((colored(bzl, 'green', 'on_magenta')) + ' ')


    

if ztbot == '1':
    os.system('cls' if os.name == 'nt' else 'clear')
    ttbot = raw_input((colored(bbv, 'green', 'on_magenta'))+ ' ')
    
    if ttbot == '1':
        def getIP(site):
            site = site.strip()
            try:
                if 'http://' not in site:
                    IP1 = socket.gethostbyname(site)
                    print(GREEN + "[+]" +   WHITE + "IP: "+ GREEN + IP1)
                    open('ips.txt', 'a').write(IP1+'\n')
                
            except:
                print(RED + "[-]" + WHITE + "DOMAIN: " + RED + site)
                pass
            
        list = raw_input('\n' + (colored(vet, 'green', 'on_magenta')))
        with open(list) as f:
            for i in f:
                getIP(i) 
                
    if ttbot == '2':
        
        print (colored(zelta, 'cyan', 'on_white'))
        

        shironpilih = raw_input('\n' +(colored(delma, 'green', 'on_magenta'))+ ' ')
        print(" ") 
        def getipe1():
            SHIroNX = raw_input(fc+'\t\t1ST : ')
            CODEE = raw_input(fc+'\t\tLast : ')
            try:
                for page in range(int(SHIroNX), int(CODEE)):
                    urls = 'http://usings.ru/bots.php?bot=&page='+str(page)
                    SHIroNGET = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
                    if 'IP' in SHIroNGET:
                        REGEX = re.findall("[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}",SHIroNGET)
                        for SHIN in REGEX:
                            print(Fore.GREEN + colored(vlz, 'red', 'on_green')+ Fore.WHITE + SHIroN)
                            open('result.txt','a').write(SHIroN+'\n')
                        else:
                            print(Fore.RED + colored(dde, 'green', 'on_red') + Fore.WHITE)
            except:
                pass

        

        def getipe3():
            SHIroNX = raw_input('\t\t1ST : ')
            CODEE = raw_input('\t\tLast : ')
            try:
                for page in range(int(SHIroNX), int(CODEE)):
                    urls = 'http://bitverzo.com/recent_ip?p='+str(page)
                    SHIroNGET = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
                    if 'Recent IP reviews' in SHIroNGET:
                        REGEX = re.findall('<a href="http://bitverzo.com/ip/(.*?)">',SHIroNGET)
                        for SHIroN in REGEX:
                            print(Fore.GREEN + colored(vlz, 'red', 'on_green') + Fore.WHITE + SHIroN)
                            open('result.txt','a').write(SHIroN+'\n')
                            
                        else:
                            print(Fore.RED + colored(dde, 'green', 'on_red') + Fore.WHITE)
            except:
                pass

        def getipe4():
            try:
                SHIroNX = raw_input('\t\t1ST : ')
                CODEE = raw_input('\t\tLast : ')
                ua = {
                'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
                }
                for page in range(int(SHIroNX), int(CODEE)):
                    urls = "http://macrobyte.net/recent_ip?p="+str(page)
                    SHIroNGET = requests.post(urls,headers=ua, timeout=10).text
                    if 'Recent IP reviews' in SHIroNGET:
                        REGEX = re.findall('<a href="http://macrobyte.net/ip/(.*?)">',SHIroNGET)
                        for SHIroN in REGEX:
                            print(Fore.GREEN + colored(vlz, 'red', 'on_green') + Fore.WHITE + SHIroN)
                            open('result.txt','a').write(SHIroN+'\n')
                        else:
                            print(Fore.RED + colored(dde, 'green', 'on_red') + Fore.WHITE)
            except:
                pass

        def getipe5():
            try:
                SHIroNX = raw_input('\t\t1ST : ')
                CODEE = raw_input('\t\tLast : ')
                ua = {
                'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
                }
                for page in range(int(SHIroNX), int(CODEE)):
                    urls = "http://viewsforcash.com/recent_ip?p="+str(page)
                    SHIroNGET = requests.post(urls,headers=ua, timeout=10).text
                    if 'Recent IP reviews' in SHIroNGET:
                        REGEX = re.findall('<a href="http://viewsforcash.com/ip/(.*?)">',SHIroNGET)
                        for SHIroN in REGEX:
                            print(Fore.GREEN + colored(vlz, 'red', 'on_green') + Fore.WHITE + SHIroN)
                            open('result.txt','a').write(SHIroN+'\n')
                        else:
                            print(Fore.RED + colored(dde, 'green', 'on_red') + Fore.WHITE)
            except:
                pass
    
        def DELETE_DUPLICATE():
            with open('result.txt', 'r') as SHIroNXX:
                SHIroNXXX = list(dict.fromkeys(SHIroNXX.read().splitlines()))
                with open('result.txt.tmp','a') as new:
                    new.write('\n'.join(SHIroNXXX))
                    new.close()
                SHIroNXX.close()
            os.remove('result.txt')
            os.rename('result.txt.tmp','result.txt')

        def Main():
            try:
                if shironpilih == '1':
                    getipe1()
                elif shironpilih == '2':
                    getipe3()
                elif shironpilih == '3':
                    getipe4()
                elif shironpilih == '4':
                    getipe5()
            except:
                pass

        if __name__ == '__main__':
            Main()
            DELETE_DUPLICATE()
            
        else:
            print('\n\t\t [-] Unavailable option')

if ztbot == '2':
    os.system('cls' if os.name == 'nt' else 'clear')
    def askdns(url):
        try:
            headers = {
                'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'
            }
            x = requests.get('https://askdns.com/ip/'+url, headers=headers, timeout=30).content
            if 'Domain Name' in x:
                regex = re.findall('<a href="/domain/(.*?)">', x)
                for jan in regex:
                    print("[+] GET {} DOMAIN FROM {}".format(len(jan), url))
                    open('rdms.txt', 'a').write('http://' + jan + '\n')
            else:
                print("BAD RAP" + url)
        except:
            pass

    def rapid(url):
        try:
            headers = {
                'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'
            }
            x = requests.get('https://rapiddns.io/s/' + url + '?full=1&down=1#result/', headers=headers, timeout=30).content
            if '<th scope="row ">' in x:
                regex = re.findall(
                    '<td>(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}</td>', x)
                for jan in regex:
                    cok = jan.replace('<td>', '').replace('</td>', '').replace('ftp.', '').replace('images.',
                                                                                                     '').replace(
                        'cpanel.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('webmail.',
                                                                                                      '').replace(
                        'webdisk.', '').replace('hostmaster.', '').replace('mail.', '').replace('ns1.', '').replace(
                        'ns2.', '').replace('autodiscover.', '')
                    print("\033[32m[+] GET {} DOMAIN FROM {}\033[0m\n".format(len(cok), url))
                    open('rdms.txt', 'a').write('http://' + cok + '\n')
            else:
                print("\033[31mNOT FOUNDED\033[0m")
        except:
            pass

    def revip(url):
        try:
            rapid(url)
            askdns(url)
        except:
            pass

    def Main():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[35mThreading ... /  | {}ShiroMoriaty\033[0m".format(Fore.YELLOW, Fore.CYAN))
        try:
            list = raw_input("\033[95mYOUR LIST PLEASE :\033[0m")
            url = open(list, 'r').read().splitlines()
            THREAD = raw_input("THREAD (for average internet between 50 to 1000)  : ")
            pp = ThreadPool(int(THREAD))
            pr = pp.map(revip, url)
        except:
            pass

    if __name__ == '__main__':
        Main()
        

if ztbot == '3':
    os.system('cls' if os.name == 'nt' else 'clear')
    print((colored(zerf, 'cyan', 'on_white')))
    
    
    xrrr = raw_input('\n' +(colored(bzl, 'green', 'on_magenta')) + ' ')

    if xrrr == '':
        print("Option Not Found[!]")
    elif xrrr == '1':
        input_filename = raw_input("\n\t\t\t [+] Enter the file name: ").strip("'\"")

        # Open the input file and read the lines
        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()

        # Process each line and print the modified result
        with open("rslt.txt", 'w') as output_file:
            for line in lines:
                modified_line = line.replace('http://', '').replace('https://', '')
                output_file.write(modified_line)
                # Print the modified line with a [+] marker in red color
                print(Fore.RED + '[+]' + Style.RESET_ALL + ' ' + Fore.GREEN + modified_line.strip() + Style.RESET_ALL)
        print("The modified URLs have been saved in 'rslt.txt'.")
    elif xrrr == '2':
        input_filename = raw_input("\t\t\t Enter the input file name: ").strip("'\"")

        # Open the input file and read the lines
        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()

        # Process each line and print the modified result
        with open("rslt2.txt", 'w') as output_file:
            for line in lines:
                domain = line.strip()
                try:
                    # Use the requests library to send a HEAD request to the website
                    response = requests.head(domain)
                    if response.status_code == 200:
                        # If the website responds with a 200 OK status code, use the protocol of the request URL
                        protocol = response.url.split(':')[0]
                        modified_domain = protocol + '://' + domain
                        output_file.write(modified_domain + '\n')
                        # Print the modified line with a [+] marker in green color
                        print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' ' + modified_domain)
                    else:
                        # If the website responds with a status code other than 200, assume http protocol
                        modified_domain = 'http://' + domain
                        output_file.write(modified_domain + '\n')
                        # Print the modified line with a [+] marker in green color
                        print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' ' + modified_domain)
                except:
                    # If the request fails, assume http protocol
                    modified_domain = 'http://' + domain
                    output_file.write(modified_domain + '\n')
                    # Print the modified line with a [+] marker in green color
                    print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' ' + modified_domain)
        print("The modified domains have been saved in 'rslt2.txt'.")
    else:
        print("Option Not Found[!]")
        
        
    
if ztbot == '5':
    os.system('cls' if os.name == 'nt' else 'clear')
    # Prompt the user to input their PHPSESSID and ZHE cookies
    phpssid = raw_input('\n' +(colored(ftf, 'green', 'on_magenta')) + ' ')
    zhe_cookie = raw_input('\n' +(colored(tlt, 'green', 'on_magenta')) + ' ')
    number_of_pages = raw_input('\n' +(colored(wtr, 'green', 'on_magenta')) + ' ')

    cookie = {"ZHE" : zhe_cookie, "PHPSESSID" : phpssid}

    # Create an empty list to store notifiers
    nfrs=[]

    print("\t\tGet all notifiers from -> 'https://zone-h.org/archive/published=0/page=', \n\t\tThe Please wait a moment while we begin the grabbing process. !")

    for page_number in range(int(number_of_pages)):
        response = requests.get('https://zone-h.org/archive/published=0/page='+str(page_number+1), cookies=cookie).content
        if 'If you often get this captcha when gathering data' in response.decode('utf-8'):
            input("\n Please verify the CAPTCHA and then press 'Enter'.")
            response = requests.get('https://zone-h.org/archive/published=0/page='+str(page_number+1), cookies=cookie).content
        soup = BeautifulSoup(response, 'html.parser')
        links = soup.findAll('a')
        for i in range(len(links)):
            if '/archive/notifier=' in str(links[i]):
                vv = str(links[i]).replace('<a href="/archive/notifier=', '')
                notif = ''
                for j in range(len(vv)-1):
                    if not(vv[j]+vv[j+1] == '">'):
                        notif = notif + vv[j]
                    else:
                        break
                if notif not in nfrs:
                    nfrs.append(notif)
                    open('notifiers.txt', 'a+').write(notif + '\n')

    print('\t\tTotal notifiers: '+str(len(nfrs)))

    # Create an empty list to store unique site URLs
    sts = []

    for i in range(len(nfrs)):
        print('\t\tGrabbing Sites From : '+str(nfrs[i]))
        for j in range(50):
            response = requests.get('http://www.zone-h.org/archive/notifier=' + str(nfrs[i]) + '/page=' + str(j+1), cookies=cookie).content
            if 'If you often get this captcha when gathering data' in response.decode('utf-8'):
                input("\n Please press 'Enter' buton avter verify the CAPTCHA")
                response = requests.get('http://www.zone-h.org/archive/notifier=' + str(nfrs[i]) + '/page=' + str(j+1), cookies=cookie).content
            soup = BeautifulSoup(response, 'html.parser')
            links = soup.findAll("td", {"class": "defacepages"})
            if '<strong>0</strong>' in str(links[0]):
                break
            else:
                response = response.decode('utf-8')
                pages = re.findall('<td>(.*)\n							</td>', response)
                for page in pages:
                    new_url = 'http://' + str(page.split('/')[0])
                    if str(new_url) not in sts:
                        sts.append(new_url)
                        retless = '\t\t' + new_url
                        open('zonehWeb.txt', 'a+').write(new_url + '\n')
                        print('\n' + (colored(retless, 'cyan', 'on_white')))
    

if ztbot == '6':
    os.system('cls' if os.name == 'nt' else 'clear')
    

    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days) + 1):
            yield start_date + timedelta(n)

    def checkTLD(domain):
        req = requests.get("https://zoxh.com/tld").text
        all_tld = re.findall('/tld/(.*?)"', req)
        if domain in all_tld:
            return True
        else:
            return False

    def TLD(domain_tld):
        req = requests.get("https://zoxh.com/tld/{}".format(domain_tld)).text
        total_domain = int(re.findall('href="/tld/{}/(.*?)"'.format(domain_tld), req)[-2])

        for i in range(total_domain):
            i += 1
            try:
                req_grab = requests.get("https://zoxh.com/tld/{}/{}".format(domain_tld, i)).text
                all_domain = "\n".join(re.findall('/i/(.*?)"', req_grab)).strip("\r\n")
                total_domain = len(all_domain.split("\n"))
                open("tld_{}.txt".format(domain_tld), "a").write(all_domain + "\n")
                print('\n'+(colored(vanip, 'green', 'on_white')).format(total_domain, i))
            except:
                pass

    if __name__ == "__main__":
        
        input_tld = raw_input('\n'+(colored(exptx, 'green', 'on_magenta')) + ' ') 

        if checkTLD(input_tld):
            TLD(input_tld)
        else:
            exit('\n\t\t[-] Unknown TLD')
 
 
if ztbot == '4':
    os.system('cls' if os.name == 'nt' else 'clear')
    # Replace the URL with your website's URL
    url_template = 'https://zone-xsec.com/archive/page={}'
    first_page = int(raw_input('\n'+(colored(ego1, 'green', 'on_magenta') + ' ')))
    last_page = int(raw_input('\n' + (colored(ego2, 'green', 'on_magenta'))+ ' '))

    urls = []
    for page in range(first_page, last_page+1):
        # Construct the URL for the current page using the template and the current page number
        url = url_template.format(page)

        # Send a GET request to the URL and get the HTML content
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all the text in the HTML and extract any strings that look like website URLs
        for text in soup.stripped_strings:
            if '.' in text:
                # Add the http:// prefix to the URL if it doesn't have it already
                if not text.startswith('http://') and not text.startswith('https://'):
                    text = 'http://' + text

                # Parse the URL using the urlparse function from the urlparse module
                parsed_url = urlparse(text)

                # Extract only the domain name from the parsed URL
                domain_name = parsed_url.netloc.split(':')[0]

                # Remove any subdomains and any additional path or query parameters
                domain_parts = domain_name.split('.')
                if len(domain_parts) >= 2:
                    tld = domain_parts[-1]
                    if len(tld) <= 3:
                        domain_name = '.'.join(domain_parts[-2:])
                    else:
                        domain_name = '.'.join(domain_parts[-3:])

                # Add the domain name to the list of URLs if it hasn't been added before
                if domain_name not in urls:
                    urls.append(domain_name)
                    print('\n'+(colored(ego, 'magenta', 'on_white')).format(domain_name))

    # Write the extracted URLs to a new text file
    with open('zonexecweb.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')
    
   
    print('Grabbing completed!')        
 
else:
    print("\n\t\t[!]This is a wrong number")