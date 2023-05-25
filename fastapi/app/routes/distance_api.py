from fastapi import APIRouter
from .. import schemas
import math

router = APIRouter(
    prefix="/api/v1/distance",
    tags=["Distance"]
)


@router.post("/calculate")
def calculate_distance(request: schemas.Location):
    print(request.point1)
    x1, y1 = request.point1.latitude, request.point1.longitude
    x2, y2 = request.point2.latitude, request.point2.longitude
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return distance

