import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ComandoService {

  private apiUrl = 'http://10.0.0.112:8080/api/comandos';

  constructor(private http: HttpClient) {}

  enviarComando(comando: string): Observable<any> {
    return this.http.post(this.apiUrl, { comando });
  }
}
