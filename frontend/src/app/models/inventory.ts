export interface InventoryItem {
  _id: string;
  categoria: string;
  marca: string;
  stock_total: number;
  "nombre comercial"?: string;
  descripcion?: string;
  precio_por_unidad?: number;
  recetado?: boolean;
}
