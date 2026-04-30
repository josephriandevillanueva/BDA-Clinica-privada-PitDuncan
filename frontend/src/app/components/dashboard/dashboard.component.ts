import { Component } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  template: `
    <div class="bg-white p-6 rounded shadow-md h-full">
      <h2 class="text-2xl font-bold mb-4">Panel de Control</h2>
      <p>Bienvenido al Panel de Control de Pit Duncan. Por favor, seleccione un módulo en el menú.</p>
    </div>
  `
})
export class DashboardComponent {}
