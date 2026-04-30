import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  template: `
    <div class="flex items-center justify-center h-full">
      <div class="bg-white p-8 rounded shadow-md w-96">
        <h2 class="text-2xl font-bold mb-4 text-center">Iniciar Sesión</h2>
        <form (submit)="onLogin($event)">
          <div class="mb-4">
            <label class="block text-gray-700">Usuario</label>
            <input type="text" class="w-full border p-2 rounded mt-1" />
          </div>
          <div class="mb-6">
            <label class="block text-gray-700">Contraseña</label>
            <input type="password" class="w-full border p-2 rounded mt-1" />
          </div>
          <button type="submit" class="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700">Ingresar</button>
        </form>
      </div>
    </div>
  `
})
export class LoginComponent {
  constructor(private router: Router) {}

  onLogin(event: Event) {
    event.preventDefault();
    this.router.navigate(['/dashboard']);
  }
}
