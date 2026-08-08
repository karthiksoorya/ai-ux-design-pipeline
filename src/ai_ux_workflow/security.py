"""Small authentication helpers for optional public-demo controls."""

from __future__ import annotations

import hmac


def valid_live_password(supplied: str, configured: str) -> bool:
    """Compare a user-entered password without leaking comparison timing."""
    if not supplied or not configured:
        return False
    return hmac.compare_digest(supplied.encode("utf-8"), configured.encode("utf-8"))

