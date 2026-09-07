from sqlalchemy import ForeignKey
import enum
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime



class FrequencyEnum(str, enum.Enum):
    DAILY = "daily"
    WEEKLY = "weekly"

class Habit(Base):  
    __tablename__ = "habits"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    frequency: Mapped[FrequencyEnum] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    user: Mapped["User"] = relationship(back_populates="habits")
    logs: Mapped[list["HabitLog"]] = relationship(back_populates="habit")
