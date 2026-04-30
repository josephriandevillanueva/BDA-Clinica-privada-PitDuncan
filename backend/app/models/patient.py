from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Any
from datetime import datetime

class PatientBase(BaseModel):
    nombre: str
    ap_paterno: str
    ap_materno: str
    fecha_nacimiento: str
    telefono: str
    email: EmailStr
    direccion: str
    contacto_de_emergencia: str
    datos_medicos: str
    activo: bool = True

class PatientCreate(PatientBase):
    pass

class PatientDB(PatientBase):
    id: str = Field(alias="_id")
    fecha_registro: datetime
