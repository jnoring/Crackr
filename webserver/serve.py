import web, json
from RAKE import rake
import candygen as cgen  

urls = (
    
    '/' , 'index' ,
    '/add', 'add' ,

    )

class index:
    def GET(self):
        # redirect to the static file ...
        raise web.seeother('/static/index.html')

class static:
    def GET(self, media, file1):
        try:
            f = open(media+'/'+file1, 'r')
            return f.read()
        except:
            return '' # you can send an 404 error here if you want

"""
class index:
    def GET(self):
        return open("index.html",'r').read()
"""
class add:
    def POST(self):
        i = web.input()
        print i
        text = i.get('text')
        text = text.encode("utf-8")
        print "Running"
        topresults = rake.extract(text)
        naive_skills, expanded_skills = cgen.performTask(text)
        ls = {}
        ls["rake"] = topresults["0"]+topresults["1"]+topresults["2"]
        print "RAKE:",ls["rake"]
        ls["naive"] = list(naive_skills)
        print "NAIVE:", ls["naive"]
        ls ["crakr"] = expanded_skills[1]
        print "CRAKR:", ls["crakr"]
        s1= json.dumps(ls)
        s = "Content-Type: application/json \n\n"+  json.dumps (ls)
        print ls
        return s1    


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()