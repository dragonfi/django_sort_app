from django.test import TestCase, Client

import json

class TestSortingView(TestCase):
    def test_sorting_view(self):
        data = {
            "items":[
                {"a": 1, "b": 10},
                {"a": 0, "b": 100},
                {"a": 0.5, "b": 1}],
            "weights": {"a": 2, "b": -1}}
        expected_response = {"sorted": [
            {"b": 100, "a": 0},
            {"b": 1, "a": 0.5},
            {"b": 10, "a": 1}]}
        response = Client().get("/sort/?json={}".format(json.dumps(data)))
        decoded_content = json.loads(response.content.decode("utf-8"))
        self.assertEquals(decoded_content, expected_response)

