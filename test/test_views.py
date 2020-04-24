import unittest
import json
import xml.etree.cElementTree as ET
from hello_world import app
from hello_world.formater import SUPPORTED

name = "Marcin"
msg = 'Hello World!'


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output_json(self):
        data = {
          "imie": name,
          "mgs": msg
        }
        rv = self.app.get('/?output=json&name=' + name)
        self.assertEqual(json.dumps(data), rv.data.decode("utf-8"))

    def test_msg_with_output_xml(self):
        # <greetings>
        greetings = ET.Element("greetings")
        # <name>
        ET.SubElement(greetings, "name").text = name
        # <msg>
        ET.SubElement(greetings, "msg").text = msg
        xml = self.app.get('/?output=xml&name=' + name)
        self.assertEqual(ET.tostring(greetings), xml.data)
