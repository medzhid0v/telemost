from urllib.parse import urljoin

import requests

from .shemas import (
    AccessLevel,
)


class TelemostManager:
    def __init__(self, url: str, client_id: str, client_secret: str, oauth: str):
        self._url = url
        self._client_id = client_id
        self._client_secret = client_secret
        self._oauth = oauth

        self._headers = {
            'Authorization': f'OAuth {self._oauth}',
            'Content-Type': 'application/json',
        }

    def _make_request(self, method: str, endpoint: str, json: dict | None = None):
        url = urljoin(self._url, endpoint)
        response = requests.request(method, url, headers=self._headers, json=json)
        response.raise_for_status()
        return response.json()

    def create_conference(
            self,
            waiting_room_level: AccessLevel,
            live_stream_title: str | None = None,
            live_stream_description: str | None = None,
            live_stream_access: AccessLevel | None = None,
            cohosts: list[str] | None = None,
    ):
        payload = {
            "waiting_room_level": waiting_room_level.value,
        }

        if live_stream_title and live_stream_access:
            payload["live_stream"] = {
                "access_level": live_stream_access.value,
                "title": live_stream_title,
                "description": live_stream_description or ""
            }

        if cohosts:
            payload["cohosts"] = [{"email": email} for email in cohosts]

        return self._make_request('POST', 'conferences', json=payload)

    def get_conference_info(self, conference_id: str):
        return self._make_request('GET', 'conferences/{}'.format(conference_id))

    def get_conference_cohosts(self, conference_id: str):
        return self._make_request('GET', 'conferences/{}/cohosts'.format(conference_id))
