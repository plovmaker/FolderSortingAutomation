from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json


class MyHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        for filename in os.listdir(folder_destination):
            if '.mp3' in filename or '.wav' in filename or 'mp.4' in filename:
                src = folder_destination + '/' + filename
                new_destination = folder_to_store_music + '/' + filename
                os.rename(src, new_destination)
            elif '.pdf' in filename or '.doc' in filename or '.pages' in filename:
                src = folder_destination + '/' + filename
                new_destination = folder_to_store_text + '/' + filename
                os.rename(src, new_destination)
            else:
                continue



folder_to_track = '/Users/suleymanyusupov/Downloads'
folder_destination = '/Users/suleymanyusupov/Desktop/Destination'
folder_to_store_music = '/Users/suleymanyusupov/Desktop/NewMusic'
folder_to_store_text = '/Users/suleymanyusupov/Desktop/NewText'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_destination, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
