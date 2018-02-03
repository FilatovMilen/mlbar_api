# mlbar_api
The ML Bar back-end

## Setup

1. git clone https://github.com/FilatovMilen/mlbar_api
2. ./setup.sh

The _setup.sh_ script sets up a new virtualenv, installs dependencies in _requirements.txt_, and builds the initial database.

## Usage

After running the setup.sh script you can use:

* _source /lib/bin/activate_ - to activate the python3 virtualenv
* _./migrate.sh_ - to migrate db if you have made any changes to the models/db schema
* _./runserver.sh_ - to run the back-end server locally
