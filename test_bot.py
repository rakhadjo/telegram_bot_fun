import pytest
import requests

def testJoke():
	response = requests.get('https://sv443.net/jokeapi/v2/joke/Any?format=json').json()
	assert response['error'] is False