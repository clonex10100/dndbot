import urllib.request
import re
import json
class Api5e:
    indexPages = {}
    def __init__(self):
        pass

    def getPage(self, url):
        page = urllib.request.urlopen(url)
        return json.loads(page.read().decode('utf-8'))

class SpellDatabase:
    def __init__(self, api):
        self.database = {}
        self.api = api
        
        page = self.api.getPage("http://dnd5eapi.co/api/spells/")
        for spell in page.get("results"):
            self.database[spell.get("name").lower()] = re.search("[0-9]+$", spell.get("url"))[0]
            print(self.database)
    def getSpell(self, name):
        return Spell(self.api, self.database.get(name.lower()))

class Spell:
    def __init__(self, api, index):
        self.page = api.getPage("http://dnd5eapi.co/api/spells/" + str(index) + "/")

    def getPage(self):
        return self.page

    def string(self):
        string = self.page.get("name") + "   lvl: " + str(self.page.get("level"))
        string += "\n------------\n"
        try:
            for i in self.page.get("desc"):
                string += i + "\n\n"

            for i in self.page.get("higher_level"):
                string += i + "\n\n"
        except:
            pass

        return string

    
api = Api5e()
spellBase = SpellDatabase(api)
acidBolt = Spell(api,1)
print(acidBolt.string())
while True:
    print(spellBase.getSpell(input()).string())

