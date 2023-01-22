# DATABASE BACKUP
The backup of the database should be placed in this folder in event of Restore. It if a work around for Data backup of the system since no online Database platform is free anymore.

## Backup
Only an admin can initiate a Database backup on the systems dashboard. This will save the backups to our cloudinary storage (which is free for the mean time).
Not that this MUST be done before our free database subcription expires!

## Restore
On expiration of our free Database subription, all data on the database will be deleted by the hosting provider. So upon getting a new database, an admin would manually download the backed-up files from our cloudinary storage, place these files in the format specified below, and initiate the Database restore on the admin dashboard. This will resaved all backed-up data to the new database.

### File Format / Naming
It should be in json file format with the following file name:
- files.json (for File model data)
- qrcodes.json (for QrCode model data)
- qrtypes.json (for QrType model data)
- users.json (for User model data)

Each file should contain the a json list of objects representing an entry for the particular model. The fields of this object must match that of the model as defined in their repective models.py file.
