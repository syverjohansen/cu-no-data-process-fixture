"""Configuration validation without environment or file access."""

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class AppConfig:
    service_name: str
    log_level: str = "INFO"

    @classmethod
    def from_mapping(cls, values: Mapping[str, str]) -> "AppConfig":
        service_name = values.get("service_name", "").strip()
        if not service_name:
            raise ValueError("service_name is required")

        log_level = values.get("log_level", "INFO").strip().upper()
        if log_level not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
            raise ValueError(f"unsupported log_level: {log_level}")
        return cls(service_name=service_name, log_level=log_level)
