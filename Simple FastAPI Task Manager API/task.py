from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

import crud
import schemas

from database import SessionLocal

router = APIRouter(tags=["Task Management"])


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/tasks", response_model=schemas.TaskResponse, status_code=201)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):

    return crud.create_task(db, task)


@router.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(
    title: str = None,
    status: str = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    

    return crud.get_tasks(
        db=db,
        title=title,
        status=status,
        skip=skip,
        limit=limit
    )


@router.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_task(db, task_id, task)

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_task(db, task_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task Deleted Successfully"
    }