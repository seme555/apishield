import uuid
from datetime import datetime, timedelta
from sqlalchemy import (
    Column, String, Integer, DateTime, ForeignKey
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from core.config import settings


class Invitation(Base):
    __tablename__ = "invitations"
    __table_args__ = {'extend_existing': True}
    
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    full_name = Column(String(150), nullable=False)
