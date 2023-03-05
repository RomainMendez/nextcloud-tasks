# Nextcloud Tasks API

[![Python package](https://github.com/Sinkmanu/nextcloud-tasks/actions/workflows/test-todo.yml/badge.svg?branch=main)](https://github.com/Sinkmanu/nextcloud-tasks/actions/workflows/test-todo.yml)

A [Nextcloud Tasks](https://github.com/nextcloud/tasks) API wrapper with some useful examples for CLI

```py
from nextcloudtasks import *

nextcloud = NextcloudTask("foo.bar.org:443/remote.php/dav/calendars/foobar/", "Daily")
nextcloud.connect("foobar", "foopass")
nextcloud.printTODOs("summary,categories,created,priority")
nextcloud.close()
```

It is a custom API wrapper that is not developed nor maitained by Nextcloud. 

## Installation

```sh
pip install nextcloudtasks
```

## Examples

The following example is a tool that manages the a Nextcloud TODO list from the command line. It can be found in [examples](/examples)

.tasks.rc
```
[DEFAULT]
url=your.nextclouddomain.foo:443/remote.php/dav/calendars/youruser/
user=youruser
password=yourpassword
list=yourlist
```

nc-tasks.py:
```
Welcome to Nextcloud tasks CLI.   Type help or ? to list commands.
(Nextcloud Tasks) ?

Documented commands (type help <topic>):
========================================
add    complete  delete  exit  load       print    
close  connect   edit    help  nextcloud  print_all

(Nextcloud Tasks) load
(Nextcloud Tasks) print
+---------------------------------+--------------------------------------+------------+----------+
|             SUMMARY             |                 UID                  | RELATED-TO | PRIORITY |
+---------------------------------+--------------------------------------+------------+----------+
|   "Add license to repository"   | 83d03d4b-42ae-4895-907d-ece9f7824b9d |    None    |    0     |
| "Readme.md with examples"       | bee1985e-1ff1-4ba1-80fb-2afeaaff2fb1 |    None    |    0     |
|       Create a repository       | 0a71a3ac-8682-4a0e-97cd-1d93a067ef90 |    None    |    1     |
+---------------------------------+--------------------------------------+------------+----------+
```

## Hacking

Pull requests are welcome. 

## License

[GPL](https://www.gnu.org/licenses/gpl-3.0.txt)
