# Sport log Management

This is a personal project created with Tkinter to manage all sport activities that you do.

## Installation

You need install all requeriments that you can found in [requirements](requirements.txt) with package manager [pip](https://pip.pypa.io/en/stable/).

```bash
pip install numpy==1.19.3
pip install mysql-connector
pip install tkcalendar==1.6.1
```
Note that numpy have an specific version. It is because of a bug with actual numpy (December 2020) that will be fixed in January 2021.

You need also MySQL server. I recommend install [XAMPP](https://www.apachefriends.org/index.html), then go to [seeds](seeds/sql_create_database_and_mocked_sports_and_difficulties.sql) file and execute this file in SQL server. Note that sports only have two. If you practice more sports or simpy do different activities, you can insert different sports, it does not matter. Same for difficulties.

Finally you need to create a JSON file for credentials of DB created (name of file: credentialsDB.json). and put it on **root directory**. This file must be like this:
```json
{
   "host":"hostDB",
   "user":"userDB",
   "password":"passwordDB",
   "database":"DBName"
}
```

Then you will be able to use this!
## Usage

```bash
python ./logsSport.py
```

## Created by
Francesc Ferré Tarrés - December, 2020.