
class TransformQueryToJSONOutput:

    @staticmethod
    def transform(data):
        result = []
        for single_data in data:
            result.append(single_data.to_json())

        return {'result': result}
