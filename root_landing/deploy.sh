#!/bin/bash
# Sync the root domain landing page to the target server
rsync -avz -e "ssh -i /Users/alec/Pictures/Work/lindsay/event-coordinator/deploy/keys/id_rsa -o StrictHostKeyChecking=no" --delete public/ root@138.197.8.215:/var/www/unified-designs.com/html/
