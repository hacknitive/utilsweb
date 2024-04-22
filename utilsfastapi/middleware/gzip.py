from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware


def prepare_gzip_middleware(
        app: FastAPI,
        minimum_size: int,
) -> None:
    app.add_middleware(
        GZipMiddleware,
        minimum_size=minimum_size
    )
