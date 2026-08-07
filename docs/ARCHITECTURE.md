# Architecture

```
NAS (SMB) --rclone copy--> Pixel buffer --> Google Photos (Original)
                              |
                           hold/
                              |
                     delete + mark done.list
```

Goals: unlimited library size relative to phone storage; no endless re-copy; survive reboot.
