"""
Script for establishing a connection to a Cassandra database using secure authentication.

This script imports required modules and configures a connection to a Cassandra database
using secure connection details and authentication credentials stored in a token file.

Modules:
- json: Handling JSON files for authentication credentials
- cassandra.cluster: Cluster for establishing connections to Cassandra
- cassandra.auth: PlainTextAuthProvider for providing authentication credentials

Usage:
- Set up the required database configuration bundle and token file paths.
- Access the authentication details from the token file and establish a secure connection to the Cassandra database.

Note: Ensure the paths to the database configuration bundle and token file are correctly specified.
"""

import json
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

DATABASE_CONFIG_BUNDLE = 'AI/database/secure-connect-gpt-world.zip'
DATABASE_TOKEN = 'AI/database/gpt-world-token.json'

cloud_config= {
  'secure_connect_bundle': DATABASE_CONFIG_BUNDLE
}

is_connected = False
try:
    with open(DATABASE_TOKEN) as f:
        secrets = json.load(f)

    CLIENT_ID = secrets["clientId"]
    CLIENT_SECRET = secrets["secret"]

    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()

    row = session.execute("select release_version from system.local").one()
    if row:
        print(row[0])
        is_connected = True
    else:
        print("An error occurred.")
except:
    pass