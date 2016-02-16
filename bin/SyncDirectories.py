import dirsync

class CustomLogger:
    def __init__(self):
        self.messages = []

    def info(self, record):
        self.messages.append(record)


class FolderSyncer:
    def __init__(self):
        self.messages = []

    def syncFolder(self, source, target):
        print("Syncing folders, source " + source + " target" + target)

        logger = CustomLogger()
        result = dirsync.sync(source, target, 'sync', verbose=True, logger=logger)

        print(logger.messages)
        print(result)

        return result