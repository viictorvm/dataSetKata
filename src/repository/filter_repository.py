
from src.repository.base_repository import BaseRepository


class FilterRepository(BaseRepository):

    def __init__(self):
        super(FilterRepository, self).__init__()

    def filter_by(self, query, filter):
        for attr, value in filter.items():
            current_attr = getattr(self.current_class, attr)
            if current_attr is self.current_class.date_to:
                custom_filter = current_attr.date <= value
            else:
                custom_filter = current_attr.like("%%%s%%" % value)
            query = query.filter(custom_filter)

        return query
