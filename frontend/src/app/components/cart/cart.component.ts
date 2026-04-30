import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { CartService, CartItem } from '../../services/cart.service';

@Component({
  selector: 'app-cart',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="bg-white p-6 rounded shadow-md h-full">
      <h2 class="text-2xl font-bold mb-4 text-yellow-600">Tu Carrito de Compras</h2>
      
      @if (cartItems.length === 0) {
        <div class="text-center py-10">
          <p class="text-gray-500 mb-4">Tu carrito está vacío.</p>
          <a routerLink="/store" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Regresar a la Farmacia</a>
        </div>
      } @else {
        <div class="overflow-x-auto shadow-sm rounded-lg border border-gray-200">
          <table class="min-w-full bg-white">
            <thead class="bg-gray-100 border-b border-gray-200">
              <tr>
                <th class="py-3 px-4 text-left text-xs font-semibold text-gray-600 uppercase">Producto</th>
                <th class="py-3 px-4 text-center text-xs font-semibold text-gray-600 uppercase">Precio Unitario</th>
                <th class="py-3 px-4 text-center text-xs font-semibold text-gray-600 uppercase">Cantidad</th>
                <th class="py-3 px-4 text-right text-xs font-semibold text-gray-600 uppercase">Subtotal</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
              @for (item of cartItems; track item.product._id) {
                <tr>
                  <td class="py-4 px-4 font-bold">{{ item.product['nombre comercial'] || item.product.categoria }}</td>
                  <td class="py-4 px-4 text-center">{{ item.product.precio_por_unidad | currency:'MXN' }}</td>
                  <td class="py-4 px-4 text-center">{{ item.quantity }}</td>
                  <td class="py-4 px-4 text-right font-bold">{{ (item.product.precio_por_unidad || 0) * item.quantity | currency:'MXN' }}</td>
                </tr>
              }
            </tbody>
            <tfoot class="bg-gray-50 border-t border-gray-200">
              <tr>
                <td colspan="3" class="py-4 px-4 text-right font-bold text-lg">Total a Pagar:</td>
                <td class="py-4 px-4 text-right font-extrabold text-xl text-green-700">{{ total | currency:'MXN' }}</td>
              </tr>
            </tfoot>
          </table>
        </div>
        
        <div class="mt-6 flex justify-between">
          <button (click)="clearCart()" class="text-red-600 hover:text-red-800 font-semibold underline">Vaciar Carrito</button>
          <button class="bg-green-600 text-white px-6 py-3 rounded-lg font-bold shadow hover:bg-green-700 transition">Proceder al Pago</button>
        </div>
      }
    </div>
  `
})
export class CartComponent implements OnInit {
  cartItems: CartItem[] = [];
  total: number = 0;

  constructor(private cartService: CartService) {}

  ngOnInit() {
    this.cartItems = this.cartService.getCartItems();
    this.calculateTotal();
  }

  calculateTotal() {
    this.total = this.cartItems.reduce((acc, curr) => acc + ((curr.product.precio_por_unidad || 0) * curr.quantity), 0);
  }

  clearCart() {
    this.cartService.clearCart();
    this.cartItems = [];
    this.total = 0;
  }
}
