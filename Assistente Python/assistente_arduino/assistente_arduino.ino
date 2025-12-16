String comando;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT); // LED
}

void loop() {
  if (Serial.available()) {
    comando = Serial.readStringUntil('\n');
    comando.trim();

    if (comando == "LED_ON") {
      digitalWrite(13, HIGH);
      Serial.println("OK LED_ON");
    }
    else if (comando == "LED_OFF") {
      digitalWrite(13, LOW);
      Serial.println("OK LED_OFF");
    }
    else {
      Serial.println("CMD_DESCONHECIDO");
    }
  }
}
