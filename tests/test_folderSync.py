import pytest
import dirsync
import os.path
from bin.SyncDirectories import FolderSyncer

def test_syncFolders_nothing_to_sync(tmpdir):
    source = tmpdir.mkdir("source")
    target = tmpdir.mkdir("target")

    syncDirectories = FolderSyncer()

    result = syncDirectories.syncFolder(str(source.dirpath()), str(target.dirpath()))

    assert len(result) == 0


def test_sync