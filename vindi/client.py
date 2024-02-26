from typing import Literal

from vindi.handlers.customer import CustomerHandler
from vindi.http_client.httpx_client import HttpxClient
from vindi.http_client.protocols import HttpClient
from .config import Config


class Client:
    def __init__(
        self,
        api_key: str,
        environment: Literal["prod", "sandbox"] = "sandbox",
        http_client: HttpClient = HttpxClient(),
    ) -> None:
        self._config = Config(api_key=api_key, environment=environment)
        self._http_client = http_client

    @property
    def api_key(self) -> str:
        return self._config.api_key

    @property
    def environment(self) -> str:
        return self._config.environment

    @property
    def customer(self) -> CustomerHandler:
        return CustomerHandler(http_client=self._http_client, config=self._config)
