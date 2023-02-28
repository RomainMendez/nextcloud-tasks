#!/usr/bin/env python3

from nextcloudtasks import *

user=""
password=""
url="foo.bar.foo:443/remote.php/dav/calendars/foobar/"

nextcloud = NextcloudTask(url, "Daily")
nextcloud.connect(user, password)
#nextcloud.addTodo("A new task with status need actions", 0, 0)
#nextcloud.printTODOs("created,summary,categories,priority,percent-complete,status")
#nextcloud.printTODOs("summary,categories,created")
uid = nextcloud.getUidbySummary("A new task with prioity 0 lol")
nextcloud.printTODO(uid)
nextcloud.updateTodo(uid, categories=["Foobar","courses"])
#print("UID: " + nextcloud.getUidbySummary("This is the second task"))
#nextcloud.deleteByUid("b1351d4e-9d99-11ed-bb7a-05975c776481")
#nextcloud.deleteBySummary("This is the second task")
nextcloud.close()
