# 🧠 Projeto Assistente Residencial Distribuído (IA + IoT)

Este projeto implementa uma **arquitetura de automação residencial distribuída**, onde a **inteligência e a lógica ficam centralizadas em um servidor**, enquanto os **dispositivos de hardware (ESP32)** atuam apenas como **executores de comandos**.

O sistema foi pensado para funcionar **100% em rede local (LAN/Wi-Fi)**, sem dependência de internet externa, garantindo **baixo tempo de resposta, segurança e escalabilidade**.

---

## 📐 Visão Geral da Arquitetura

```
📱 Celular / 💻 PC
        |
        | HTTP (rede local)
        v
🌐 Interface Web (Angular)
        |
        | HTTP
        v
☕ API (Spring Boot)
        |
        | chamada interna
        v
🧠 IA / Lógica (Python)
        |
        | MQTT (mensagem)
        v
📡 Broker MQTT (Mosquitto)
        |
        | Wi-Fi (mensagem)
        v
🔌 ESP32 (executores)
```

---

## 🧠 Conceito do Projeto

- O **servidor é o cérebro**:
  - Interpreta comandos
  - Aplica regras
  - Pode usar IA (voz, NLP, automações)
- Os **ESP32 são membros executores**:
  - Não tomam decisões
  - Apenas recebem comandos e executam ações físicas
- A comunicação é **desacoplada**, permitindo crescer o sistema sem retrabalho.

---

## 🧩 Componentes do Sistema

### 📱 Interface Web (Angular)
- Interface acessível via celular ou computador
- Envia comandos HTTP para o backend
- Não conhece hardware nem pinos físicos

Exemplo de requisição:
```json
{
  "comodo": "sala",
  "acao": "ligar_luz"
}
```

---

### ☕ API Backend (Spring Boot)
- Porta de entrada do sistema
- Valida requisições
- Gerencia segurança (futuro)
- Encaminha comandos para a camada de lógica/IA

---

### 🧠 Lógica / IA (Python)
- Interpreta a intenção do usuário
- Traduz comandos humanos em ações físicas
- Publica mensagens no broker MQTT

Exemplo de publicação MQTT:
```
Topic: casa/sala/luz
Payload: ON
```

---

### 📡 Broker MQTT (Mosquitto)
- Atua como **central de mensagens**
- Distribui comandos para os dispositivos corretos
- Não executa lógica nem ações físicas

Características:
- Leve
- Escalável
- Padrão em automação residencial e IoT

---

### 🔌 ESP32 (Dispositivos Executores)
- Conectados via Wi-Fi
- Inscritos em tópicos específicos
- Executam comandos ao receber mensagens

Exemplo:
```cpp
Topic: casa/sala/luz
Mensagem: ON
→ Liga o relé da luz da sala
```

---

## 🔄 Fluxo de Funcionamento

1. Usuário acessa a interface pelo celular ou PC
2. Interface envia requisição HTTP para o Spring Boot
3. Spring chama a lógica/IA em Python
4. Python publica mensagem no MQTT
5. Broker entrega a mensagem ao ESP32 correto
6. ESP32 executa a ação física

---

## 📡 Padrão de Tópicos MQTT

```
casa/<comodo>/<dispositivo>
```

Exemplos:
```
casa/sala/luz
casa/quarto/ventilador
casa/cozinha/tomada
```

---

## 🔐 Segurança (Planejado)

- Sistema funciona apenas em rede local
- MQTT pode usar usuário e senha
- Cada ESP se inscreve apenas nos seus tópicos
- Futuro suporte a autenticação na API

---

## 🚀 Tecnologias Utilizadas

- **Frontend:** Angular
- **Backend:** Spring Boot (Java)
- **Lógica / IA:** Python
- **Mensageria:** MQTT (Mosquitto)
- **Hardware:** ESP32
- **Comunicação:** Wi-Fi (LAN)

---

## 📌 Objetivos do Projeto

- Automação residencial modular
- Arquitetura escalável
- Separação clara de responsabilidades
- Base sólida para IA e automações avançadas
- Projeto educacional e de portfólio

---

## 🛠️ Próximos Passos

- Implementar autenticação
- Criar histórico de comandos
- Adicionar reconhecimento de voz
- Criar dashboards em tempo real
- Migrar para servidor dedicado / Raspberry Pi

---

## 📄 Licença
Projeto em desenvolvimento para fins educacionais e experimentais.
