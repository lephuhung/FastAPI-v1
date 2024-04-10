from fastapi import APIRouter, Body, Depends, HTTPException, Security, Form
from typing import Annotated
from app.schemas.permission import PermissionCreate, PermissionUpdate
from app.crud.crud_permission import CURD_Permission
from app.Routes import deps
from elasticsearch import Elasticsearch
from datetime import datetime
from sqlalchemy.orm import Session

router = APIRouter(prefix="/search", tags=["Elastic Search"])
es = Elasticsearch(
    "http://elasticsearch:9200",
    api_key="RXRVdnlJNEJqUWQwZndGTXFlQVc6LWVZQnNUdG1SZm15UkZhZDRaUDJsQQ==",
)

@router.post("/trichtin")
async def getTrichtin(
    keyword: str,
    start_date: datetime = datetime(2024, 1, 1),
    end_date: datetime = datetime(2050, 12, 31),
    db: Session = Depends(deps.get_db),
):
    try:

        query = {
            "query": {
                "bool": {
                    "must": [
                        {"query_string": {"query": f"*{keyword}*"}},
                        {"range": {"created_at": {"gte": start_date, "lte": end_date}}},
                    ]
                }
            },
            "sort": [
                {
                    "created_at": {"order": "asc"}
                }  # Sorting by created_at column in ascending order
            ],
        }
        indices = ["trichtin_index"]
        response = es.search(index=indices, body=query)
        hits = response["hits"]["hits"]
        return hits
    except Exception as e:
        raise HTTPException(status_code=400, detail=(e))


@router.post("/doituong")
async def getDoituong(
    keyword: str,
    start_date: datetime = datetime(2024, 1, 1),
    end_date: datetime = datetime(2050, 12, 31),
    db: Session = Depends(deps.get_db),
):
    try:

        query = {
            "query": {
                "bool": {
                    "must": [
                        {"query_string": {"query": f"*{keyword}*"}},
                        {"range": {"created_at": {"gte": start_date, "lte": end_date}}},
                    ]
                }
            },
            "sort": [
                {
                    "created_at": {"order": "asc"}
                }  # Sorting by created_at column in ascending order
            ],
        }
        indices = ["doituong_index"]
        response = es.search(index=indices, body=query)
        hits = response["hits"]["hits"]
        return hits
    except Exception as e:
        raise HTTPException(status_code=400, detail=(e))


@router.post("/uid")
async def getUid(
    keyword: str,
    start_date: datetime = datetime(2024, 1, 1),
    end_date: datetime = datetime(2050, 12, 31),
    db: Session = Depends(deps.get_db),
):
    try:

        query = {
            "query": {
                "bool": {
                    "must": [
                        {"query_string": {"query": f"*{keyword}*"}},
                        {"range": {"created_at": {"gte": start_date, "lte": end_date}}},
                    ]
                }
            },
            "sort": [
                {
                    "created_at": {"order": "asc"}
                }  # Sorting by created_at column in ascending order
            ],
        }
        indices = ["uid_index"]
        response = es.search(index=indices, body=query)
        hits = response["hits"]["hits"]
        return hits
    except Exception as e:
        raise HTTPException(status_code=400, detail=(e))



