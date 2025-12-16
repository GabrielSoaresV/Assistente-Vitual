package central.assistente_api.dto;

import jakarta.validation.constraints.NotBlank;

public class ComandoRequest {

    @NotBlank(message = "O comando não pode ser vazio")
    private String comando;

    public String getComando() {
        return comando;
    }

    public void setComando(String comando) {
        this.comando = comando;
    }
}
