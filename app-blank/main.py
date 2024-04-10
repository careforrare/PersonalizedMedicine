from bottle import Bottle

from FeatureCloud.app.api.http_ctrl import api_server
from FeatureCloud.app.api.http_web import web_server

from FeatureCloud.app.engine.app import app

import states

server = Bottle()

if __name__ == "__main__":
    app.register()
    server.mount("/api", api_server)
    server.mount("/web", web_server)
    server.run(host="localhost", port=5000)

import logging
import os
from logging.config import dictConfig
import yaml

import random
import string
import time

from neo4j import GraphDatabase, Query, Record
from neo4j.exceptions import ServiceUnavailable
from pandas import DataFrame

# from dotenv import load_dotenv

# load_dotenv()


# Define function to load neo4j credentials from config.yml
def load_neo4j_credentials(file_path="/mnt/input/config.yml"):
    try:
        with open(file_path, "r") as config_file:
            config = yaml.safe_load(config_file)
            neo4j_credentials = config.get("neo4j_credentials", {})
            NEO4J_URI = neo4j_credentials.get("NEO4J_URI", "")
            NEO4J_USERNAME = neo4j_credentials.get("NEO4J_USERNAME", "")
            NEO4J_PASSWORD = neo4j_credentials.get("NEO4J_PASSWORD", "")
            return NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD
    except FileNotFoundError:
        print(f"Config file '{file_path}' not found.")
        return None, None, None


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Check if logs directory exists, if not create it
# This folder is created inside the docker container
if not os.path.exists("logs"):
    os.makedirs("logs")

# Load neo4j credentials
NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD = load_neo4j_credentials()


# Driver instantiation
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

node_count_query = "MATCH (n)-[r]->(m) RETURN count(m)"

if __name__ == "__main__":

    # Create a driver session
    with driver.session() as session:
        # Use .data() to access the results array
        results = session.run(node_count_query).data()
        print(results)

        # Close the driver connection
        driver.close()
