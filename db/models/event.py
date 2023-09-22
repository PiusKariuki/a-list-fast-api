from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from db.base_class import Base


class Event(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
