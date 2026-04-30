import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterLink],
  template: `
    <div class="bg-white p-10 rounded shadow-md h-full text-center flex flex-col justify-center items-center">
      <h1 class="text-4xl font-bold mb-6 text-blue-600">Bienvenido a la Clínica Pit Duncan</h1>
      <p class="text-lg text-gray-700 mb-8 max-w-2xl">
        Su salud es nuestra prioridad. Ofrecemos consultas de especialistas, así como una farmacia en línea para la compra de sus medicamentos con envío directo a su domicilio.
      </p>
      <div class="flex space-x-6">
        <a routerLink="/appointments" class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 text-lg shadow">
          Agendar Cita Médica
        </a>
        <a routerLink="/store" class="bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700 text-lg shadow">
          Farmacia en Línea
        </a>
      </div>
    </div>
  `
})
export class HomeComponent {}
