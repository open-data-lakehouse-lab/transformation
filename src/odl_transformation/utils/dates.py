from datetime import datetime, timezone

def get_current_utc_date_str() -> str:
    """Returns current UTC date in YYYY-MM-DD format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")
