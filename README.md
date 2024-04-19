# tachi-backup-to-json

This is a simple dump script to dump tachiyomi backup files to json.
This is a compiled version at least allows us to read the protobuf file. `tachi/` houses the compiled protobuf definitions. Look at Contributions if you need to modify the `.proto` file.

## Motivation

Mainly to document how I got things out of Tachiyomi and to provide reference for other technically minded people on how to dump their backups to more usable formats.

Do what you want with it, but don't expect help.

## Usage

The following is enough to get this to install all the requirements (outside of `protoc`, either install it manually or see if your package manager can do so).

```bash
git clone https://github.com/zamu-flowerpot/tachi-backup-to-json
cd tachi-backup-to-json
python -m venv --copies venv
venv/bin/pip install -r requirements.txt
venv/bin/python script.py $BACKUP_FILE
```

At this point you should have `backup.json` in your currrent directory. 
Once you copy the `backup.json` file away feel free to delete this repo and uninstall `protoc`.

## Contribution

Requires you to install `protoc`, compile the `tachi.proto` definitions to code, then modify the script.

