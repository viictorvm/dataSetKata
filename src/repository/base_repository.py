from src.models.dataset import DataSet
from src.utils.db import Connect


class BaseRepository:
    def __init__(self, current_class=DataSet):
        self.session = Connect.getConnection()
        self.current_class = current_class

