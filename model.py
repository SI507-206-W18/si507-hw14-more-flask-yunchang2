import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
idnum = 0

def init():
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, idnum
    now = datetime.now()
    #time_string = now.strftime("%b %d, %Y %-I:%M %p")
    time_string = str(now)
    # create an attribute ID for each post
    entry = {"author": name, "text": text, "timestamp": time_string, "ID": idnum}
    idnum += 1 # increase ID number whem it is called every time
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id_number):
    f = open(GUESTBOOK_ENTRIES_FILE)
    entries = json.loads(f.read())
    f.close()
    for ele in entries:
        if ele["ID"] == id_number:
            position = entries.index(ele)
            entries.pop(position)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not delete entries to file.")
