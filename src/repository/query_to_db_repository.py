from src.repository.base_repository import BaseRepository
from src.repository.filter_repository import FilterRepository
from src.repository.group_repository import GroupRepository
from src.repository.sort_repository import OrderRepository


class QueryToDBRepository(BaseRepository):

    def __init__(self):
        super(QueryToDBRepository, self).__init__()
        self.filter_repository = FilterRepository()
        self.group_repository = GroupRepository()
        self.sort_repository = OrderRepository()

    def make_query(self, filter, group, sort):
        query = self.session.query(self.current_class)
        query = self.filter_repository.filter_by(query, filter)
        query = self.group_repository.group_by(query, group)
        query = self.sort_repository.sort_by(query, sort)

        return query.all()
