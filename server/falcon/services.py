"""falcon services."""
import json

from django.conf import settings

import requests

from .models import User


class UserService(object):
    """User service."""

    @classmethod
    def login(cls, name, password):
        """User login."""
        data = {'name': name, 'password': password}
        url = '{}/user/login'.format(settings.API_ADDR)

        resp = requests.post(url, data=data)

        if resp.status_code != 200:
            raise Exception(resp.text)

        retdata = resp.json()

        return retdata

    @classmethod
    def get_profile(cls, token):
        """Get user profile."""
        headers = {
            'Content-type': 'application/json',
            'Apitoken': json.dumps({'name': token.name, 'sig': token.sig})
        }
        url = '{}/user/current'.format(settings.API_ADDR)
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            return {}

        retdata = resp.json()
        return User(retdata['id'], retdata['name'], retdata['cnname'],
                    retdata['email'], retdata['phone'], retdata['im'],
                    retdata['qq'], retdata['role'])
