import pytest
import dirsync
import os.path
from bin.SyncDirectories import FolderSyncer
import tempfile
from shutil import copyfile
from datetime import datetime
import time
from datetime import timedelta


def test_syncFolders_nothing_to_sync():
    source, target, syncDirectories = __createFixture()

    result = syncDirectories.syncFolder(source, target)

    assert len(result) == 0

def test_syncFilesOneFileDifference_fileShouldBeCopied():
    sourceDir, targetDir, syncDirectories = __createFixture()

    print("Source dirpath: " + sourceDir)

    __writeToFile(sourceDir, "/newFile.txt", "content")

    result = syncDirectories.syncFolder(sourceDir, targetDir)

    print("result " + str(result))

    assert "newFile.txt" in str(result)


def test_syncFileAlreadyExist_doNothing():
    sourceDir, targetDir, syncDirectories = __createFixture()

    print("Source dirpath: " + sourceDir)

    file = __writeToFile(sourceDir, "newFile.txt", "content")
    copyfile(file.name, targetDir + "/newFile.txt")

    result = syncDirectories.syncFolder(sourceDir, targetDir)

    print("result " + str(result))

    assert len(result) == 0


def test_syncFileAlreadyExistWithNewerLastModificationTimestamp_doNothing():
    sourceDir, targetDir, syncDirectories = __createFixture()

    print("Source dirpath: " + sourceDir)

    file = __writeToFile(sourceDir, "newFile.txt", "content")
    newFile = copyfile(file.name, targetDir + "/newFile.txt")
    future_time =  (datetime.now() + timedelta(minutes = 10)).timestamp()
    os.utime(newFile, (future_time, future_time))
    result = syncDirectories.syncFolder(sourceDir, targetDir)

    print("result " + str(result))


    assert len(result) == 0

def test_syncFileAlreadyExistWithOlderLastModificationTimestamp_doNothing():
    sourceDir, targetDir, syncDirectories = __createFixture()

    print("Source dirpath: " + sourceDir)

    file = __writeToFile(sourceDir, "newFile.txt", "content")
    newFile = copyfile(file.name, targetDir + "/newFile.txt")
    os.utime(file.name)
    result = syncDirectories.syncFolder(sourceDir, targetDir)

    print("result " + str(result))

    assert len(result) == 0

def __writeToFile(path, fileName, content):
    f = open(path + "/" + fileName, 'w')
    f.write(content)
    f.close()
    return f

def __createFixture():
    tmpdir = tempfile.mkdtemp()

    sourceDir = tmpdir + "/source"
    targetDir = tmpdir + "/target"
    os.mkdir(sourceDir)
    os.mkdir(targetDir)

    syncDirectories = FolderSyncer()

    return sourceDir, targetDir, syncDirectories