"""Health endpoint response construction."""

from typing import Any


def health_response(service_name: str, *, ready: bool) -> dict[str, Any]:
    return {
        "service": service_name,
        "status": "ready" if ready else "starting",
    }
