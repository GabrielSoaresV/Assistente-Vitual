import { Component, signal } from '@angular/core';
import { ComandoService } from './services/comando';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  standalone: false,
  styleUrl: './app.css'
})
export class App {

  status = 'Aguardando comando';

  constructor(private comandoService: ComandoService) {}

  ligar() {
    this.comandoService.enviarComando('LED_ON')
      .subscribe({
        next: (res) => {
          this.status = 'LED ligado';
          console.log(res);
        },
        error: () => this.status = 'Erro ao ligar LED'
      });
  }

  desligar() {
    this.comandoService.enviarComando('LED_OFF')
      .subscribe({
        next: (res) => {
          this.status = 'LED desligado';
          console.log(res);
        },
        error: () => this.status = 'Erro ao desligar LED'
      });
  }
}
