# experiments

## Developing

To build:

```
uv run pelican public
```

To publish, copy the `output` folder somewhere. 

rsync -avz -e "ssh -p 8321 -i ~/.ssh/do_old_priv" output/* root@104.236.110.199:/srv/main/sites/unified-designs.com
