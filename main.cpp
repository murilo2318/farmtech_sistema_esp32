#include <DHT.h>

#define DHTPIN 15
#define DHTTYPE DHT22
#define BUTTON_P 4
#define BUTTON_K 5
#define LDR_PIN 34
#define RELAY_PIN 2

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  pinMode(BUTTON_P, INPUT_PULLUP);
  pinMode(BUTTON_K, INPUT_PULLUP);
  pinMode(LDR_PIN, INPUT);
  pinMode(RELAY_PIN, OUTPUT);

  digitalWrite(RELAY_PIN, LOW);
}

void loop() {
  bool fosforoPresente = digitalRead(BUTTON_P) == LOW;
  bool potassioPresente = digitalRead(BUTTON_K) == LOW;
  int valorLDR = analogRead(LDR_PIN);
  float umidade = dht.readHumidity();

  if (isnan(umidade)) {
    Serial.println("Erro ao ler umidade!");
    return;
  }

  bool ligarBomba = false;

  if (umidade < 40 || !fosforoPresente || !potassioPresente || valorLDR > 3000) {
    ligarBomba = true;
  }

  digitalWrite(RELAY_PIN, ligarBomba ? HIGH : LOW);

  Serial.println("----- LEITURA DOS SENSORES -----");
  Serial.print("Fósforo presente: "); Serial.println(fosforoPresente ? "Sim" : "Não");
  Serial.print("Potássio presente: "); Serial.println(potassioPresente ? "Sim" : "Não");
  Serial.print("pH (LDR): "); Serial.println(valorLDR);
  Serial.print("Umidade do solo: "); Serial.print(umidade); Serial.println(" %");
  Serial.print("Bomba de irrigação: "); Serial.println(ligarBomba ? "LIGADA" : "DESLIGADA");
  Serial.println("--------------------------------\n");

  delay(3000);
}
