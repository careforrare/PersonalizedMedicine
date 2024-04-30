import os
import logging

from neo4j import GraphDatabase, Query, Record
from neo4j.exceptions import ServiceUnavailable

from utils import read_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run(output_dir, neo4j_config):
    # Get Neo4j credentials from config
    neo4j_credentials = neo4j_config.get("neo4j_credentials", {})
    NEO4J_URI = neo4j_credentials.get("NEO4J_URI", "")
    NEO4J_USERNAME = neo4j_credentials.get("NEO4J_USERNAME", "")
    NEO4J_PASSWORD = neo4j_credentials.get("NEO4J_PASSWORD", "")
    NEO4J_DB = neo4j_credentials.get("NEO4J_DB", "")
    logger.info(f"Neo4j Connect to {NEO4J_URI} using {NEO4J_USERNAME}")

    # Driver instantiation
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

    # Create a driver session with defined DB
    with driver.session(database=NEO4J_DB) as session:

        # Example Query to Count Nodes
        node_count_query = "MATCH (n) RETURN count(n)"

        # Use .data() to access the results array
        results = session.run(node_count_query).data()
        logger.info(results)

    with open(os.path.join(output_dir, 'results.txt'), 'w') as text_file:
        text_file.write(f"{results}")

    # Close the driver connection
    driver.close()

if __name__ == "__main__":
    import sys
    output_dir = 'data/output'
    config_path = 'config.yml'
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    if len(sys.argv) > 2:
        config_path = sys.argv[2]
    config = read_config(config_path)
    run(output_dir, config)
