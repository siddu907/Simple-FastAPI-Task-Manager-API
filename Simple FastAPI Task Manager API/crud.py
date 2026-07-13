from sqlalchemy.orm import Session
import models
import schemas


def create_task(db: Session, task: schemas.TaskCreate):

    new_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks(
    db: Session,
    title: str = None,
    status: str = None,
    skip: int = 0,
    limit: int = 10
):
    query = db.query(models.Task)

    # Search by title
    if title:
        query = query.filter(models.Task.title.ilike(f"%{title}%"))

    # Filter by status
    if status:
        query = query.filter(models.Task.status == status)

    # Pagination
    tasks = query.offset(skip).limit(limit).all()

    return tasks


def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):

    db_task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if db_task is None:
        return None

    db_task.title = task.title
    db_task.description = task.description
    db_task.status = task.status

    db.commit()
    db.refresh(db_task)

    return db_task


def delete_task(db: Session, task_id: int):

    db_task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if db_task is None:
        return None

    db.delete(db_task)
    db.commit()

    return db_task