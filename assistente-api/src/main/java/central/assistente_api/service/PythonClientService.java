package central.assistente_api.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PythonClientService {

    private final RestTemplate restTemplate = new RestTemplate();

    private final String PYTHON_URL =
            "http://127.0.0.1:5000/executar?comando={comando}";

    public String enviarComando(String comando) {

        return restTemplate.postForObject(
                PYTHON_URL,
                null,          // sem body
                String.class,
                comando        // query param
        );
    }
}
