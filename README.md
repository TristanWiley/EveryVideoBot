I made this script to power https://twitter.com/everyvideobot

It'll post a few random videos a day (depending on the cron job) to my Twitter from YouTube.

This is the cron job I'm using, hopefully it works:
`0 0,8,16 * * * sleep $(( RANDOM \% 14400 )); python3 ~/videotweet.py`
