"""Tokenisation bridge."""
from __future__ import annotations

from typing import List


def event_to_token(event: str) -> int:
    return len(event)


def token_to_event(token: int) -> str:
    return "x" * token
