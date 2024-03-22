import logging
import os
from logging.config import dictConfig

import random
import string
import time

from neo4j import GraphDatabase, Query, Record
from neo4j.exceptions import ServiceUnavailable
from pandas import DataFrame

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Check if logs directory exists, if not create it
# This folder is created inside the docker container
if not os.path.exists("logs"):
    os.makedirs("logs")

NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

# Driver instantiation
driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
)

node_count_query = "MATCH ()-->() RETURN count(*)"

if __name__ == "__main__":
    
    # Create a driver session
    with driver.session() as session:
        # Use .data() to access the results array
        results = session.run(node_count_query).data()
        print(results)
    
        # Close the driver connection
        driver.close()