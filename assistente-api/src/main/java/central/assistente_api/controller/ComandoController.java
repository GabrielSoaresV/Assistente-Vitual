package central.assistente_api.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import central.assistente_api.dto.ComandoRequest;
import central.assistente_api.service.PythonClientService;
import jakarta.validation.Valid;

@RestController
@RequestMapping("/api/comandos")
@CrossOrigin(origins = "*")
public class ComandoController {

    private final PythonClientService pythonClientService;

    public ComandoController(PythonClientService pythonClientService) {
        this.pythonClientService = pythonClientService;
    }

    @PostMapping
    public ResponseEntity<?> receberComando(
            @Valid @RequestBody ComandoRequest request
    ) {
        String comando = request.getComando();

        String respostaPython =
                pythonClientService.enviarComando(comando);

        return ResponseEntity.ok(respostaPython);
    }

    @GetMapping
    public String status() {
        return "API do Assistente está online";
    }
}
