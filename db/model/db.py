from tinydb import TinyDB, Query, table

class Database:
    def __init__(self, username = ""):
        """
        Constructor for database
        Parameters: username, a string representing current user
        Initalizes a new table for each user in media_db.json
        """
        self.username = username
        self.db = TinyDB('media_db.json')
        self.table = self.db.table(username)
        if len(self.table.all()) == 0:
            self.table.upsert(table.Document({'empty': True}, doc_id=-1))
       
    def lookup_library(self):
        """
        Gets library from the database
        Returns library as a dict, else a dict showing library is empty
        """
        ret = {}
        for i in self.table.all():
            if i.doc_id == -1:
                if i.get('empty') == True:
                    return {'-1': {'MEDIA_TYPE': 'Empty'}}
                continue
            ret[i['media_id']] = i
        return ret

    def lookup_media(self, media_id) -> dict:
        """
        Gets a single MediaEntry from library
        Parameter: media_id, int corresponding to MediaEntry removed
        Returns a dict matching media_id from data, or error dict
        """
        q = Query()
        result = self.table.search(q.media_id == media_id)[0]
        if len(result) == 0:
            return {"Results": False and "Media not found"}
        return result[0]

    def add_media(self, data):
        """
        Adds media to library, and sets empty to false
        Parameter: data, a dict containing serialized MediaEntry
        Returns: Dict indicating result of operation
        """
        self.table.upsert(table.Document(data, doc_id = data.get("media_id")))
        self.table.upsert(table.Document({'empty': False}, doc_id=-1))
        return {"Results": True and "Successfully added media"}

    def remove_media(self, media_id):
        """
        Removes media from library, may set empty to true
        Parameter: media_id, int corresponding to MediaEntry removed
        Returns: Dict indicating result of operation
        """
        q = Query()
        self.table.remove(q.media_id == media_id)
        if len(self.table.all()) == 1:
            self.table.upsert(table.Document({'empty': True}, doc_id=-1))
        return {"Results": True and "Successfully removed media"}
