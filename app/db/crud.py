from datetime import datetime
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Generic CRUD operations for SQLAlchemy models.

    Provides standard Create, Read, Update, Delete operations with type safety.
    """

    def __init__(self, *, model: Type[ModelType]) -> None:
        """
        Initialize CRUD operations for a specific model.

        Args:
            model: A SQLAlchemy model class
        """
        self.model = model

    def get(self, db: Session, id: str) -> Optional[ModelType]:
        """
        Retrieve a single record by primary key.

        Args:
            db: Database session
