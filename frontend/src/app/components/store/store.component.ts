import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { CartService } from '../../services/cart.service';
import { InventoryItem } from '../../models/inventory';

@Component({
  selector: 'app-store',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="bg-white p-6 rounded shadow-md h-full">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-6">
        <div>
          <h2 class="text-2xl font-bold text-green-600">Farmacia en Línea</h2>
          <p class="text-gray-600">Catálogo de medicamentos. Seleccione cantidad y agregue al carrito.</p>
        </div>
        
        <!-- Controls -->
        <div class="mt-4 md:mt-0 flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-4">
          <!-- Search Bar -->
          <div class="relative">
            <input type="text" [(ngModel)]="searchTerm" (input)="filterItems()" list="medications"
                   placeholder="Buscar medicamento..."
                   class="border border-gray-300 rounded px-3 py-2 w-full md:w-64 focus:ring-green-500 focus:border-green-500">
            <datalist id="medications">
              @for (item of items; track item._id) {
                <option [value]="item['nombre comercial'] || item.categoria"></option>
              }
            </datalist>
          </div>
          
          <!-- Pagination Size -->
          <div class="flex items-center space-x-2">
            <label class="text-sm text-gray-600">Mostrar:</label>
            <select [(ngModel)]="itemsPerPage" (change)="changePage(1)" class="border border-gray-300 rounded px-2 py-2 focus:ring-green-500 focus:border-green-500">
              <option [ngValue]="10">10</option>
              <option [ngValue]="20">20</option>
              <option [ngValue]="50">50</option>
              <option [ngValue]="100">100</option>
              <option [ngValue]="999999">Todos</option>
            </select>
          </div>
        </div>
      </div>
      
      @if (loading) {
        <div class="text-center py-10">
          <p class="text-gray-500 text-xl font-bold">Cargando inventario... Espere un momento.</p>
        </div>
      } @else if (errorMsg) {
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative">
          <strong class="font-bold">Error:</strong>
          <span class="block sm:inline"> {{ errorMsg }}</span>
        </div>
      } @else {
        <div class="overflow-x-auto shadow-sm rounded-lg border border-gray-200">
          <table class="min-w-full bg-white">
            <thead class="bg-gray-100 border-b border-gray-200">
              <tr>
                <th class="py-3 px-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Producto</th>
                <th class="py-3 px-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Marca</th>
                <th class="py-3 px-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Detalles</th>
                <th class="py-3 px-4 text-right text-xs font-semibold text-gray-600 uppercase tracking-wider">Precio</th>
                <th class="py-3 px-4 text-center text-xs font-semibold text-gray-600 uppercase tracking-wider">Cantidad</th>
                <th class="py-3 px-4 text-center text-xs font-semibold text-gray-600 uppercase tracking-wider">Acción</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
              @if (paginatedItems.length === 0) {
                <tr><td colspan="6" class="text-center py-6 text-gray-500">No se encontraron productos.</td></tr>
              }
              @for (item of paginatedItems; track item._id) {
                <tr class="hover:bg-gray-50">
                  <td class="py-3 px-4">
                    <div class="font-bold text-gray-900">{{ item['nombre comercial'] || item.categoria }}</div>
                    @if (item.recetado) {
                      <span class="inline-block mt-1 px-2 py-0.5 rounded text-xs font-medium bg-red-100 text-red-800">
                        Requiere Receta
                      </span>
                    }
                  </td>
                  <td class="py-3 px-4 text-sm text-gray-600">{{ item.marca }}</td>
                  <td class="py-3 px-4 text-sm text-gray-500">
                    <div class="truncate max-w-xs" title="{{ item.descripcion }}">{{ item.descripcion || 'N/A' }}</div>
                  </td>
                  <td class="py-3 px-4 text-sm text-right font-bold text-gray-900">
                    {{ item.precio_por_unidad ? (item.precio_por_unidad | currency:'MXN') : 'N/A' }}
                  </td>
                  <td class="py-3 px-4 text-center">
                    <input type="number" min="1" [max]="item.stock_total" [(ngModel)]="quantities[item._id]"
                           class="w-16 border border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 text-center py-1"
                           [disabled]="item.stock_total <= 0">
                    <div class="text-xs text-gray-400 mt-1">Stock: {{ item.stock_total }}</div>
                  </td>
                  <td class="py-3 px-4 text-center">
                    <button (click)="addToCart(item)"
                            class="bg-green-500 text-white px-3 py-1.5 rounded-md hover:bg-green-600 disabled:opacity-50 disabled:cursor-not-allowed shadow-sm text-sm font-semibold transition"
                            [disabled]="item.stock_total <= 0 || !quantities[item._id] || quantities[item._id] < 1">
                      {{ item.stock_total > 0 ? 'Agregar' : 'Agotado' }}
                    </button>
                  </td>
                </tr>
              }
            </tbody>
          </table>
        </div>
        
        <!-- Pagination Controls -->
        @if (totalPages > 1) {
          <div class="flex justify-between items-center mt-4 px-2">
            <span class="text-sm text-gray-600">Página {{ currentPage }} de {{ totalPages }} ({{ filteredItems.length }} resultados)</span>
            <div class="space-x-2">
              <button (click)="changePage(currentPage - 1)" [disabled]="currentPage === 1" class="px-3 py-1 border rounded bg-white hover:bg-gray-50 disabled:opacity-50">Anterior</button>
              <button (click)="changePage(currentPage + 1)" [disabled]="currentPage === totalPages" class="px-3 py-1 border rounded bg-white hover:bg-gray-50 disabled:opacity-50">Siguiente</button>
            </div>
          </div>
        }
      }
    </div>
  `
})
export class StoreComponent implements OnInit {
  items: InventoryItem[] = [];
  filteredItems: InventoryItem[] = [];
  paginatedItems: InventoryItem[] = [];
  
  loading: boolean = true;
  errorMsg: string = '';
  
  // Controls
  searchTerm: string = '';
  itemsPerPage: number = 20;
  currentPage: number = 1;
  totalPages: number = 1;
  
  quantities: { [key: string]: number } = {};

  constructor(
    private apiService: ApiService, 
    private cartService: CartService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.apiService.getInventory().subscribe({
      next: (data) => {
        try {
          if (!Array.isArray(data)) throw new Error("Datos inválidos.");
          this.items = data.filter(i => i.precio_por_unidad !== null && i.precio_por_unidad !== undefined);
          
          // Initialize quantities to 1
          this.items.forEach(item => this.quantities[item._id] = 1);
          
          this.filterItems();
        } catch (e: any) {
          this.errorMsg = e.message;
        } finally {
          this.loading = false;
          this.cdr.detectChanges();
        }
      },
      error: (err) => {
        this.errorMsg = "No se pudo conectar con el servidor.";
        this.loading = false;
        this.cdr.detectChanges();
      }
    });
  }
  
  filterItems() {
    if (this.searchTerm.trim() === '') {
      this.filteredItems = [...this.items];
    } else {
      const term = this.searchTerm.toLowerCase();
      this.filteredItems = this.items.filter(item => {
        const name = (item['nombre comercial'] || '').toLowerCase();
        const cat = (item.categoria || '').toLowerCase();
        const desc = (item.descripcion || '').toLowerCase();
        return name.includes(term) || cat.includes(term) || desc.includes(term);
      });
    }
    this.currentPage = 1;
    this.updatePagination();
  }
  
  updatePagination() {
    this.totalPages = Math.ceil(this.filteredItems.length / this.itemsPerPage) || 1;
    const start = (this.currentPage - 1) * this.itemsPerPage;
    this.paginatedItems = this.filteredItems.slice(start, start + this.itemsPerPage);
  }
  
  changePage(page: number) {
    if (page >= 1 && page <= this.totalPages) {
      this.currentPage = page;
      this.updatePagination();
    }
  }

  addToCart(item: InventoryItem) {
    const qty = this.quantities[item._id] || 1;
    this.cartService.addToCart(item, qty);
    
    // Simple notification feedback
    alert(`Agregado: ${qty} x ${item['nombre comercial'] || item.categoria} al carrito.`);
  }
}
