# Getting last minecraft awakening backup

This software allow you to download the last minecraft awakening backup available
It uses the backupstore.txt provided by the "/backup" command in game each time a backup is run to know which backup file is the lastest.

## Configure it !
Copy the .env.example and rename it to ".env" then use your own credentials !

### Env data
+ FTP_HOST : Your FTP hostname
+ FTP_USER : Your FTP username
+ FTP_PASSWORD : Your FTP password
+ FTP_PORT : The used FTP port, by default 21
+ OUTPUT_DIRECTORY : The directory used to save the backup and the registry
+ MINECRAFT_WORLD_NAME : Your minecraft world name, by default "world"

## Contributing
You could update this package by opening a ticket and propose something
Or fork this project !

## Licence
This project is under MIT licence