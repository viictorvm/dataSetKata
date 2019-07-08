from src.repository.base_repository import BaseRepository


class OrderRepository(BaseRepository):

    def __init__(self):
        super(OrderRepository, self).__init__()

    def sort_by(self, query, sort):
        for current_sort in sort:
            query = query.order_by(getattr(self.current_class, current_sort).desc())
        return query
