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
            id: Primary key value

        Returns:
            Model instance or None if not found
        """
        return db.query(self.model).filter(self.model.id == id).first()

    def get_by_field(self, db: Session, field: str, value: Any) -> Optional[ModelType]:
        """
        Retrieve a single record by field value.

        Args:
            db: Database session
            field: Field name to filter by
            value: Value to match

        Returns:
            Model instance or None if not found

        Raises:
            AttributeError: If field doesn't exist on model
        """
        if not hasattr(self.model, field):
            raise AttributeError(f"Model {self.model.__name__} has no field '{field}'")

        return db.query(self.model).filter(getattr(self.model, field) == value).first()

    def get_multi_by_field(
        self, db: Session, field: str, value: Any, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """
        Retrieve multiple records by field value.

        Args:
            db: Database session
            field: Field name to filter by
            value: Value to match
            skip: Number of records to skip
            limit: Maximum number of records to return

        Returns:
            List of model instances

        Raises:
            AttributeError: If field doesn't exist on model
        """
        if not hasattr(self.model, field):
            raise AttributeError(f"Model {self.model.__name__} has no field '{field}'")

        return (
            db.query(self.model)
            .filter(getattr(self.model, field) == value)
            .offset(skip)
            .limit(limit)
