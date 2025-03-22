from sqlalchemy import Column, String, UUID, DateTime, text, Integer
from db.pg import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"), unique=True, nullable=False)
    title = Column(String(255), nullable=True)
    description = Column(String, nullable=True)
    priority = Column(Integer, nullable=True)
    created_at = Column(DateTime, server_default=text("now()"))
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, descr={self.description}, priority={self.priority}, created_at={self.created_at}, deleted_at={self.deleted_at})>"