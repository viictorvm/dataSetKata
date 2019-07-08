from tornado import escape

from src.data_transformer.transform_query_to_json_output import TransformQueryToJSONOutput
from src.handlers.custom_request_handler import CustomRequestHandler
from src.services.dataset_service import DataSetService


class SingleFilterDataHandler(CustomRequestHandler):
    SUPPORTED_METHODS = "POST"
    data_set_service = DataSetService()

    def post(self):
        data = escape.json_decode(self.request.body)
        filter = data.get('filter')
        group = data.get('group')
        sort = data.get('sort')
        data_filtered = self.data_set_service.exec(filter, group, sort)
        self.write(TransformQueryToJSONOutput.transform(data_filtered))
        self.finish()
