# retry
Retry terminal commands until they either succeed or time out.


## Installation

Just copy the script and run it. Nothing too fancy here.

## Usage

```
$ ./retry.py [options] -- command

options:
  -h: display this help message
  -i, --interval: the interval between attempts in seconds (default 60s)
  -d --timeout: the timeout in seconds (default 3600s)
  
examples:
# retry a command every second for 10 minutes
$ ./retry.py -i 1 -t 600 -- cat marsupial.txt

# retry a command every minute for 5 minutes
$ ./retry.py --interval=60 --timeout=300 -- true
```



