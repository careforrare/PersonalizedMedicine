from FeatureCloud.app.engine.app import AppState, app_state, Role
import time
import os

from pandas import DataFrame

from run import run
from utils import read_config

INPUT_DIR='/mnt/input'
OUTPUT_DIR='/mnt/output'

@app_state('initial')
class ExecuteState(AppState):

    def register(self):
        self.register_transition('terminal', Role.BOTH)

    def run(self):
        run(output_dir=OUTPUT_DIR, neo4j_config=read_config(f'{INPUT_DIR}/config.yml'))
        return 'terminal'
