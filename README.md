# optimusbahn

<p align="center">
 <img src="https://raw.githubusercontent.com/posixpascal/optimusbahn/master/optimus/api/static/optimus/images/optimus.png">
 
 **OptimusBahn** is a script which visualizes train delays and other informations for easy infrastructure problem detection.
</p>

This is my submission for the **DB Open Data Contest** – unfortunately I only discovered this contest last friday therefore
I couldn't add all the features I initially planned.  

## Feature Overview

OptimusBahn collects train delay information on a mySQL database and shows insights on how many trains are delayed (per day, per hour, per month).

It's capable of tracking multiple trains and train stations in near realtime thanks to threading support.

It automatically exports snapshots from the database into a graphs in the webfrontend.

Optimus by default does not make any assumptions on why a certain train is delayed.


## Installation

**Note**: You need at least Python 3.6 for this project.

Clone the repository and install the dependencies using pip:

```bash
pip install -r requirements.txt
```

Then edit your `config.cfg` file and add the required mySQL connection credentials:

```ini
[app]
threads = 1

[mysql]
host = 127.0.0.1
user = root
passwd = root
db = optimus
```

Be sure that the mySQL database is created beforehand.

Now start optimus by running:
```bash
python optimusbahn.py
```

## Screenshots

Due to limited timing I can't show you a live version of this script as of now.
Therefore I'll add a few screenshots to satisfy the curiosity.

 <img src="https://raw.githubusercontent.com/posixpascal/optimusbahn/master/screenshots/dashboard.png">
 
 <img src="https://raw.githubusercontent.com/posixpascal/optimusbahn/master/screenshots/trains.png">
 
 <img src="https://raw.githubusercontent.com/posixpascal/optimusbahn/master/screenshots/stations.png">
 
 <img src="https://raw.githubusercontent.com/posixpascal/optimusbahn/master/screenshots/settings.png">
 

## Gotchas

Depending on how many threads you are using the database might crash if you're on MacOS and using MAMP because of default configuration
limitations.

Adjust to meet the specifications of your current machine/server.

## License
```
MIT License

Copyright (c) 2017 Creative Tim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Copyright
Software:
Copyright (C) 2017 - Pascal Raszyk <posixpascal@googlemail.com>
 

Deutsche Bahn Logo (Part of Optimus Logo): 
Copyright (C) 2017 - Deutsche Bahn AG

Admin Theme:
Copyright (C) 2017 - Creative Tim (MIT License)

ICE Teaser Image:
Taken from [s2.germany.travel](http://s2.germany.travel/media/microsites_media/lgbt/07_how_to_get_there/db/header_01_db_SGG2013.jpg) - Probably (C) Deutsche Bahn AG