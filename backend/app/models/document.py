from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class InvoiceBase(BaseModel):
    fecha_emision: datetime
    paciente: str
    doctor: str
    concepto: str
    monto_total: float
    archivo_pdf: str # Path or URL to the generated PDF
    estado: str # e.g., "PAGADA", "PENDIENTE"

class InvoiceDB(InvoiceBase):
    id: str = Field(alias="_id")

class DocumentType(str, Enum):
    PRESCRIPTION = "PRESCRIPTION"
    INVOICE = "INVOICE"
    TICKET = "TICKET"

class DocumentRegistryBase(BaseModel):
    document_type: DocumentType
    steganographic_hash: str # The cryptographic hash embedded in the PDF
    created_at: datetime = Field(default_factory=datetime.utcnow)
    issued_to_patient_id: str
    issued_by_doctor_id: str
    
    # Specific to Prescriptions to prevent re-use
    is_used: bool = False
    used_at: Optional[datetime] = None
    file_path: str

class DocumentRegistryDB(DocumentRegistryBase):
    id: str = Field(alias="_id")
