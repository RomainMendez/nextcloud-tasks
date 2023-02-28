#!/usr/bin/env python3

from nextcloudtasks import *

user=""
password=""
url="foo.bar.org:443/remote.php/dav/calendars/foobar/"

nextcloud = NextcloudTask(url, "Daily")
nextcloud.connect(user, password)
nextcloud.printTODOs("summary,categories,created,priority")
nextcloud.close()
