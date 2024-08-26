#!/usr/bin/env python
import json
from sys import stdin
import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen


def main(url, output_path):
    content = urlopen(url)
    if output_path:
        with open(output_path,'wb') as output:
            output.write(content.read())
    return json.dumps({'status': 'success', 'output_path': output_path})


args = json.loads(stdin.read())
print(
    main(args.get('url'), args.get('output_path'))
)