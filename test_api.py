import unittest

from flask import Flask

from app.blueprint.example_blueprint import geolocation, geolocation_main

app = Flask(__name__)

app.register_blueprint(geolocation_main)
app.register_blueprint(geolocation)


class BluePrintTest(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_main(self):
        main_response = self.app.get('/')
        return self.assertEqual(main_response.status_code, 200)

    def distance_result(self, address="Mexico City"):
        return self.app.post(
        '/distance',
        data=dict(address=address),
        )

    def test_distance_endpoit(self):
        response = self.distance_result("Mexico City")
        return self.assertEqual(response.status_code, 200)
        

if __name__ == "__main__":
    unittest.main()
