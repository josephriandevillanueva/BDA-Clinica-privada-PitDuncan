from pydantic import BaseModel, Field
from typing import Optional, Any

class InventoryBase(BaseModel):
    categoria: str
    marca: str
    stock_total: int
    nombre_comercial: Optional[str] = Field(None, alias="nombre comercial")
    descripcion: Optional[str] = None
    unidad_medida: Optional[str] = None
    precio_por_unidad: Optional[float] = None
    lotes: Optional[list] = None
    proveedor: Optional[dict] = None
    sustancia_activa: Optional[str] = None
    presentacion: Optional[str] = None
    codigo_barras: Optional[str] = None
    recetado: Optional[bool] = None # Requires prescription indicator
    
    # Specific to equipment
    sku_interno: Optional[str] = None
    nombre_equipo: Optional[str] = None
    modelo: Optional[str] = None
    numero_serie: Optional[str] = None
    codigo_activo_fijo: Optional[str] = None
    ultima_certificacion: Optional[Any] = None
    vencimiento_certificacion: Optional[Any] = None

class InventoryCreate(InventoryBase):
    pass

class InventoryDB(InventoryBase):
    id: str = Field(alias="_id")
