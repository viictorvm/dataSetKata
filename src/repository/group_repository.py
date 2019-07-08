from src.repository.base_repository import BaseRepository


class GroupRepository(BaseRepository):

    def __init__(self):
        super(GroupRepository, self).__init__()

    def group_by(self, query, group):
        query = query.group_by(getattr(self.current_class, "id"))
        for current_group in group:
            query = query.group_by(getattr(self.current_class, current_group))

        return query
