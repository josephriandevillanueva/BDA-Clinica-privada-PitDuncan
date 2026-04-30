from pydantic import BaseModel, Field
from datetime import datetime

class AppointmentBase(BaseModel):
    nombre: str
    especialista: str
    fecha_hora: datetime

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentDB(AppointmentBase):
    id: str = Field(alias="_id")
