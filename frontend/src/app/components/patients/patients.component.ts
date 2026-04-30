import { Component } from '@angular/core';

@Component({
  selector: 'app-patients',
  standalone: true,
  template: `
    <div class="bg-white p-6 rounded shadow-md h-full">
      <h2 class="text-2xl font-bold mb-4">Pacientes</h2>
      <p>La gestión de pacientes se implementará aquí.</p>
    </div>
  `
})
export class PatientsComponent {}
