import asyncio
import logging

import aiohttp

from parsetron.utils.AddressAnalyzer.dto import FetchDto
from parsetron.utils.AddressAnalyzer.preparation_strategies import AddressPreparationStrategy

logger = logging.getLogger(__name__)


class NominatimGeocoder:
    def __init__(
        self,
        geo_url: str,
        max_retries: int,
        strategies: list[AddressPreparationStrategy],
    ):
        self.geo_url = geo_url
        self.max_retries = max_retries
        self.strategies = strategies

    async def _execute_network_request(
        self, session: aiohttp.ClientSession, params: dict, semaphore
    ) -> list:
        for attempt in range(self.max_retries):
            try:
                async with session.get(self.geo_url, params=params) as response:
                    if response.status == 200:
                        return await response.json()

                    if not (response.status == 429 or 500 <= response.status < 600):
                        logger.warning(f"Network Error ({type(e).__name__}) for '{params['q']}'.")
                        raise ValueError(
                            f"Unexpected HTTP Status `{response.status}`"
                        )
                    logger.warning(
                        f"Retryable Error `{response.status}`. Attempt {attempt+1}/{self.max_retries} for '{params["q"]}"
                    )
            except (asyncio.TimeoutError, aiohttp.ClientError) as e:
                logger.warning(
                    f"Network Error ({type(e).__name__}) for '{params["q"]}'."
                )
            if attempt < self.max_retries - 1:
                await asyncio.sleep(2**attempt)
        return []

    async def fetch_address(
        self,
        session: aiohttp.ClientSession,
        data: FetchDto,
        semaphore: asyncio.Semaphore,
    ) -> FetchDto:
        if not data:
            return data

        async with semaphore:
            for strategy in self.strategies:
                address = strategy.prepare_address(data)
                if not address:
                    continue
                params = {
                    "limit": 5,
                    "accept-language": "ru",
                    "addressdetails": 1,
                    "q": address,
                }

                try:
                    result = await self._execute_network_request(session, params, semaphore)
                except Exception as e:
                    logger.error(f"`{address}` Unexpected error during API request: {e}", exc_info=True)
                    return data

                response = strategy.prepare_response(address, result)
                if response:
                    data.response = response
                    break
        return data
