"""Identifier formatting helpers."""

import re

_VALID_IDENTIFIER = re.compile(r"^[a-z][a-z0-9_-]{2,63}$")


def normalize_identifier(value: str) -> str:
    normalized = value.strip().lower().replace(" ", "-")
    if not _VALID_IDENTIFIER.fullmatch(normalized):
        raise ValueError(f"invalid identifier: {value!r}")
    return normalized
