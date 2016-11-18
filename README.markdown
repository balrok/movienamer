# Fork of Movienamer2

## Changes:

* This version works with python3
* If your move is named "james bond cd1.mp4" it will be put into "james bond (2008)/james bond (2008) cd1.mp4"
* Removed cache: i mean the amount of requests is minimal and if tmdb has an error online, you fix it and want to redownload, the cache is in your way
    * if this should be really implemented use `filecache`
* pressing enter will accept first result
* added more file extensions


# MovieNamer2 #

(c) 2010-current GNU GPL v3

Author: Nathan Overall

Movienamer does exactly as it's name implies. Given the name of any movie file,
Movienamer will try to find the most likely movie and rename the file.

# Operation #

At this point the program is very much interactive. Below is an example of the
program running.

```
Loaded blacklist: 720p,1080p,bluray,x264,dvdrip,LiMiTED,HDRip,unrated,brrip,XviD,bdrip,eng,extended
Loaded cache file: /home/nathan/.movienamer/searches.cache

Processing The.Raid.Redemption.2011.BDRip.XviD-MeRCuRY.avi...
Searching for "the raid redemption" with year 2011
Using cached result
	1 - The Raid: Redemption (2011) http://www.themoviedb.org/movie/94329
	Result?: 1
	Renaming 'The.Raid.Redemption.2011.BDRip.XviD-MeRCuRY.avi' -> 'The Raid, Redemption (2011).avi'
```

# Installation #

Download [Movienamer](https://github.com/shweppsie/movienamer/archive/master.zip)

MovieNamer requires Python to run. Installing python is very platform specific, therefore you will need to check your platforms documenation for instructions on installing python.

Movienamer also uses PyYAML and themoviedb libraries.

The easiest way to install the libraries is using pip

       pip install PyYAML
       pip install themoviedb

Then run

	./movienamer2 --help
