from app.database import engine, Base
from app.models.user import User
from app.models.habit import Habit
from app.models.habit_log import HabitLog

Base.metadata.create_all(bind=engine)

print("Baza danych utworzona pomyślnie!")