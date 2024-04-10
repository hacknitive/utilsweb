from src.setting import FAST_API_APP
from fastapi.middleware.cors import CORSMiddleware

FAST_API_APP.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
