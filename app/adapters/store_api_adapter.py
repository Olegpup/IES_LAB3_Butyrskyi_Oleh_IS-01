import json
import logging
from typing import List

import pydantic_core
import requests

from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_gateway import StoreGateway
from config import STORE_API_BASE_URL
class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]):
        """
        Save the processed road data to the Store API.
        Parameters:
            processed_agent_data_batch (dict): Processed road data to be saved.
        Returns:
            bool: True if the data is successfully saved, False otherwise.
        """
        url = STORE_API_BASE_URL + "/processed_agent_data"

        d = "["
        for i, model in enumerate(processed_agent_data_batch):
            d += str(model.json()) + ("" if i == len(processed_agent_data_batch) - 1 else ",")
        d += "]"

        requests.post(url, data=d)
