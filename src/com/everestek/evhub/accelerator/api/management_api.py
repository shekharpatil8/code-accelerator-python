# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from com.everestek.evhub.accelerator.api.management_api_base import BaseManagementApi
import com.everestek.evhub.accelerator.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from com.everestek.evhub.accelerator.dto.extra_models import TokenModel  # noqa: F401


router = APIRouter()

ns_pkg = com.everestek.evhub.accelerator.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/version",
    responses={
        200: {"model": str, "description": "Successfully retrieved the version"},
        500: {"description": "Internal server error"},
    },
    tags=["management"],
    summary="Get the current version of the API",
    response_model_by_alias=True,
)
async def get_version(
) -> str:
    """Endpoint to retrieve the current version of the API"""
    if not BaseManagementApi.subclasses:
        raise HTTPException(status_code=501, detail="Not implemented")

    if len(BaseManagementApi.subclasses) > 1:
        raise HTTPException(status_code=500, detail="Multiple implementations found, You can have only one implementation for the base class")
            
    return await BaseManagementApi.subclasses[0]().get_version()


@router.get(
    "/healthcheck",
    responses={
        200: {"description": "Application is healthy"},
        503: {"description": "Service unavailable"},
    },
    tags=["management"],
    summary="Check the health of the application",
    response_model_by_alias=True,
)
async def health_check(
) -> None:
    """Endpoint to check if the application is up and running"""
    if not BaseManagementApi.subclasses:
        raise HTTPException(status_code=501, detail="Not implemented")

    if len(BaseManagementApi.subclasses) > 1:
        raise HTTPException(status_code=500, detail="Multiple implementations found, You can have only one implementation for the base class")
            
    return await BaseManagementApi.subclasses[0]().health_check()
