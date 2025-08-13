# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401



class BaseManagementApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseManagementApi.subclasses = BaseManagementApi.subclasses + (cls,)
    async def get_version(
        self,
    ) -> str:
        """Endpoint to retrieve the current version of the API"""
        ...


    async def health_check(
        self,
    ) -> None:
        """Endpoint to check if the application is up and running"""
        ...
