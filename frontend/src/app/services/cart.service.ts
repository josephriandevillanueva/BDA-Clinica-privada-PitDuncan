import { Injectable } from '@angular/core';
import { InventoryItem } from '../models/inventory';

export interface CartItem {
  product: InventoryItem;
  quantity: number;
}

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private cartItems: CartItem[] = [];
  private readonly CART_KEY = 'pit_duncan_cart';

  constructor() {
    this.loadCart();
  }

  private loadCart() {
    const saved = localStorage.getItem(this.CART_KEY);
    if (saved) {
      try {
        this.cartItems = JSON.parse(saved);
      } catch (e) {
        console.error('Error parsing cart from localStorage', e);
        this.cartItems = [];
      }
    }
  }

  private saveCart() {
    localStorage.setItem(this.CART_KEY, JSON.stringify(this.cartItems));
  }

  addToCart(item: InventoryItem, quantity: number) {
    const existing = this.cartItems.find(c => c.product._id === item._id);
    if (existing) {
      // Don't exceed stock
      existing.quantity = Math.min(existing.quantity + quantity, item.stock_total);
    } else {
      this.cartItems.push({ product: item, quantity: Math.min(quantity, item.stock_total) });
    }
    this.saveCart();
  }

  getCartItems(): CartItem[] {
    return this.cartItems;
  }

  getCartTotalItems(): number {
    return this.cartItems.reduce((acc, curr) => acc + curr.quantity, 0);
  }

  clearCart() {
    this.cartItems = [];
    this.saveCart();
  }
}
