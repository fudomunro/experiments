#!/bin/bash
uv run pelican -s pelicanconf.py
rsync -avz -e "ssh -i /Users/alec/Pictures/Work/lindsay/event-coordinator/deploy/keys/id_rsa -o StrictHostKeyChecking=no" --delete output/ root@138.197.8.215:/var/www/writing.unified-designs.com/html/
