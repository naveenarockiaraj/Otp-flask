
from .models import Base
from .database_utils import engine

Base.metadata.create_all(bind=engine)