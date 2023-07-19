from abc import ABC
from .vk_api import VkApi


class Report(ABC):
    def __init__(self, api: VkApi):
        self.api = api

    def get_data(self, user_id: int):
        pass