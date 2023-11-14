import pymongo
import certifi

me = {
    "name": "Jessie",
    "last_name": "Guerrero",
    'email': "jesenia.guerrero136@outlook.com",
    "github": "https://github.com/Jessie1331",


}


con_str = "mongodb+srv://fsdi:Test1235@cluster0.wodxmeh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str.TlsCAFile+certifi.where())
db = client.get_database("Diss") 
