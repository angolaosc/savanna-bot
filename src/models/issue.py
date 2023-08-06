from pydantic import BaseModel
from typing import Optional

class GoodFirstIssue(BaseModel):
    """Model to represent a good first issue"""
    title: str
    html_url: Optional[str] = None
    state: Optional[str] = None
    issue_number: Optional[int] = None
    created_at: Optional[str] = None
    user: Optional[dict] = None
    