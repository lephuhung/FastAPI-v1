from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.relationship import RelationshipCreate, RelationshipUpdate, Relationship
from app.crud.crud_relationship import relationship
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/relationships", tags=["Relationships"])

@router.get("/", response_model=List[Relationship])
async def get_relationships(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve relationships.
    """
    relationships = relationship.get_multi(db, skip=skip, limit=limit)
    return relationships

@router.post("/", response_model=Relationship)
async def create_relationship(
    *,
    db: Session = Depends(deps.get_db),
    relationship_in: RelationshipCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new relationship.
    """
    relationship_obj = relationship.create(db=db, obj_in=relationship_in)
    return relationship_obj

@router.put("/{id}", response_model=Relationship)
async def update_relationship(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    relationship_in: RelationshipUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a relationship.
    """
    relationship_obj = relationship.get(db=db, id=id)
    if not relationship_obj:
        raise HTTPException(status_code=404, detail="Relationship not found")
    relationship_obj = relationship.update(db=db, db_obj=relationship_obj, obj_in=relationship_in)
    return relationship_obj

@router.get("/{id}", response_model=Relationship)
async def get_relationship(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get relationship by ID.
    """
    relationship_obj = relationship.get(db=db, id=id)
    if not relationship_obj:
        raise HTTPException(status_code=404, detail="Relationship not found")
    return relationship_obj

@router.delete("/{id}", response_model=Relationship)
async def delete_relationship(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a relationship.
    """
    relationship_obj = relationship.get(db=db, id=id)
    if not relationship_obj:
        raise HTTPException(status_code=404, detail="Relationship not found")
    relationship_obj = relationship.remove(db=db, id=id)
    return relationship_obj 