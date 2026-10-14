# India IPTV Playlists

Category-wise IPTV playlists with **only Indian channels**, with channel
name, channel logo (`tvg-logo`) and stream URL in every entry.

Base URL: https://project9793.github.io/hindi-tv/

## Add channels yourself (web app)

Open **[the Add Channel app](https://project9793.github.io/hindi-tv/add-channel.html)** — enter a channel's
name, logo and stream URL, and it commits it straight into any playlist here.
It needs a GitHub fine-grained token (Contents: Read and write) for this repo.

## Playlists

| Category | Channels/streams | Playlist URL |
|---|---|---|
| All India | 1243 | https://project9793.github.io/hindi-tv/india.m3u |
| News | 467 | https://project9793.github.io/hindi-tv/news.m3u |
| Entertainment | 194 | https://project9793.github.io/hindi-tv/entertainment.m3u |
| Religious | 154 | https://project9793.github.io/hindi-tv/religious.m3u |
| Movies | 103 | https://project9793.github.io/hindi-tv/movies.m3u |
| Music | 99 | https://project9793.github.io/hindi-tv/music.m3u |
| General | 60 | https://project9793.github.io/hindi-tv/general.m3u |
| Other | 54 | https://project9793.github.io/hindi-tv/other.m3u |
| Kids | 27 | https://project9793.github.io/hindi-tv/kids.m3u |
| Sports | 21 | https://project9793.github.io/hindi-tv/sports.m3u |
| Education | 16 | https://project9793.github.io/hindi-tv/education.m3u |
| Documentary | 14 | https://project9793.github.io/hindi-tv/documentary.m3u |
| Lifestyle | 13 | https://project9793.github.io/hindi-tv/lifestyle.m3u |
| Business | 11 | https://project9793.github.io/hindi-tv/business.m3u |
| Culture | 7 | https://project9793.github.io/hindi-tv/culture.m3u |
| Animation | 7 | https://project9793.github.io/hindi-tv/animation.m3u |
| Legislative | 4 | https://project9793.github.io/hindi-tv/legislative.m3u |
| Travel | 4 | https://project9793.github.io/hindi-tv/travel.m3u |
| Comedy | 3 | https://project9793.github.io/hindi-tv/comedy.m3u |
| Cooking | 3 | https://project9793.github.io/hindi-tv/cooking.m3u |
| Classic | 3 | https://project9793.github.io/hindi-tv/classic.m3u |
| Outdoor | 2 | https://project9793.github.io/hindi-tv/outdoor.m3u |
| Science | 1 | https://project9793.github.io/hindi-tv/science.m3u |

## Checking which streams are working

Run the included `check_streams.py` on your own network:

```
python3 check_streams.py movies.m3u movies-working.m3u
```

## Note

Streams come from the iptv-org public database. Availability and legality vary
by broadcaster - use only streams you are allowed to access.
