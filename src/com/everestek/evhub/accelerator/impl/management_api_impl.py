from http import HTTPStatus
import toml
from com.everestek.evhub.accelerator.api.management_api_base import BaseManagementApi

class ManagementApiImpl(BaseManagementApi):
    async def health_check(self) -> None:
        """returns the service status"""
        return HTTPStatus.OK

    async def get_version(self) -> str:
        """Read the version from either [project] or [tool.poetry] in pyproject.toml"""
        with open("pyproject.toml", "r") as file:
            pyproject_data = toml.load(file)

        # Try [project] format first (PEP 621 standard)
        version = pyproject_data.get("project", {}).get("version")
        if version:
            return version

        # Fallback to [tool.poetry] format
        version = pyproject_data.get("tool", {}).get("poetry", {}).get("version")
        if version:
            return version

        return "unknown"