from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


def prepare_cors_middleware(
        app: FastAPI,
        allow_origins: list[str] = ["*"],
        allow_credentials: bool = True,
        allow_methods: list[str] = ["*"],
        allow_headers: list[str] = ["*"],
        expose_headers: list[str] = ["*"],
) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=allow_credentials,
        allow_methods=allow_methods,
        allow_headers=allow_headers,
        expose_headers=expose_headers,
    )
