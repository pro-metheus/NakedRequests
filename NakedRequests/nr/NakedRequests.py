DOCUMENTATION = '''

module: nr

short_description: This simple module combines the power of requests library and bs4 to make stuff easier

version_added: 0.0.1

author: Ajay Ajith (pro-metheus)

options:  NakedRequests : takes an url as argument 
          
          cook_response: returns a get response as done in requests module


          analyze: takes an html tag as a string input return a list of such tags in the html file


          get_defaults: takes html tag as argument and returns a dictionary of the tah and their default values
            

          tag_exists: takes a tag as argument and returns a boolean value according to its presence in the html

          download: takes name to be saved as, extension of file, and location to be saved as args and downloads the response content

          get_ext_urls: returns list of external links present in html


          selected_defaults: takes tag and names of the tags and return their dictionary of values

          


'''





import requests
from bs4 import BeautifulSoup as bs


class NakedRequests:

    def __init__(self,url):   
        self.url=url


        
    def cook_response(self):
        resp=requests.get(self.url)
        return resp


        
    def analyze(self,tag):
        r=NakedRequests.cook_response(self)
        soup=bs(r.text,'html.parser')
        tags=soup.find_all(tag)
        return tags

    
    def get_defaults(self,tag):
        tags=NakedRequests.analyze(self,tag)
        defaults={}
        for tag in tags:
            defaults[str(tag.get('name'))]=str(tag.get('value'))
        return defaults


    def tag_exists(self,tag):
        tags=NakedRequests.analyze(self,tag)
        if len(tags)==0:
            return False
        else:
            return True

    def download(self,name,extension,to):
        with open(to+name+extension,'wb') as f:
            f.write((NakedRequests.cook_response(self)).content)



    def get_ext_urls(self):
        res=[]
        links=NakedRequests.analyze(self,'a')
        for link in links:
            temp=link.get('href')
            temp=str(temp)
            try:
                if(temp[0:4]=='http'):
                    res.append(temp)
                else:
                    continue
            except TypeError:
                res.append('')

        return res
    
    def selected_defaults(self,arg1,*args):
        res={}
        defaults=NakedRequests.get_defaults(self,arg1)
        for arg in args:
            try:
                res[arg]=defaults[arg]
            except KeyError:
                continue

        return res
            
                      
