import pytest
import dirsync
import os.path
from bin.SyncDirectories import FolderSyncer
import tempfile


def test_syncFolders_nothing_to_sync():
    source, target, syncDirectories = __createFixture()

    result = syncDirectories.syncFolder(source, target)

    assert len(result) == 0

def test_sync_files():
    sourceDir, targetDir, syncDirectories = __createFixture()

    print("Source dirpath: " + sourceDir)

    __writeToFile(sourceDir, "/newFile.txt", "content")

    result = syncDirectories.syncFolder(sourceDir, targetDir)

    print("result " + str(result))

    assert "newFile.txt" in str(result)

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