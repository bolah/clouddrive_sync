import dirsync
import logging


class FileLogger:
    def __init__(self):
        logging.basicConfig(filename='sync.log',level=logging.DEBUG)

    def info(self, record):
        logging.info(record)

class FolderSyncer:
    def __init__(self):
        self.messages = []

    def syncFolder(self, source, target):
        print("Syncing folders, source " + source + " target" + target)

        logger = FileLogger()
        result = dirsync.sync(source, target, 'sync', verbose=True, logger=logger)

        return result