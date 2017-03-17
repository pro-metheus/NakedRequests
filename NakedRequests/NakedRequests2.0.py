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
            
                      
