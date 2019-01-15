# fastslack

send slack message from shell the easy way
use: https://api.slack.com/custom-integrations/legacy-tokens to get your auth key
```
usage: fastslack [-h] [--store] [-u USER | -c CHANNEL] [-a AUTH] [-m MESSAGE]
                 [--as-user]

optional arguments:
  -h, --help            show this help message and exit
  --store               store defaults
  -u USER, --dest-user USER
                        destination slack user
  -c CHANNEL, --dest-channel CHANNEL
                        destination slack channel
  -a AUTH, --auth AUTH  slack authentication token
  -m MESSAGE, --message MESSAGE
  --as-user             send message as user
```
