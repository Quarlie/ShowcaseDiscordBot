## Discord Bot

### CaseBot 

---

### main

- Setting global "bot." variables
- Start running the bot
- Deal with keep_alive and restarter

---

### keep_alive

- Starts a server for pings
- Makes sure the bot stays online

---

### restarter 

- Restarts and kills the bot in case of a Ratelimit Exception to start a new one under a different IP

---

### my_utils

- Deals with frequently used functions

---

### cogs directory 

- Stores categories and commands
- Stores onReady

---

### onReady

- Loads more global variables
- Loads Cogs
- Calls Command-Function, that should work after a restart

---

### data directory 

- Stores .json files containing various data

---

### errors directory 

- Stores empty .txt files, which get created in case of an Exception (name contains date and time the exception occurred)