#include <DHT.h>
const byte BTN=2, LED=8, DHTPIN=4;
DHT dht(DHTPIN,DHT22);
// Enviar f no Serial injeta falha de software; n restaura leitura real.
// h habilita o exercício de histerese; b restaura a atividade básica.
bool falhaTeste=false, usarHisterese=false, alarmeTermico=false;
unsigned long ultimo=0;
const char* classificar(float t,int bruto) {
  if(isnan(t)) return "FALHA DE SENSOR";
  if(usarHisterese) {
    if(t>=40.0) alarmeTermico=true;
    else if(t<=37.0) alarmeTermico=false;
  } else alarmeTermico=(t>=40.0);
  if(alarmeTermico || bruto>=750) return "ALARME";
  if(t>=30.0 || bruto>=400) return "ATENCAO";
  return "NORMAL";
}
void setup(){pinMode(BTN,INPUT_PULLUP);pinMode(LED,OUTPUT);Serial.begin(9600);dht.begin();Serial.println("ms,botao,bruto,temp_C,estado,modo");}
void loop(){
  bool pressionado=digitalRead(BTN)==LOW;
  digitalWrite(LED,pressionado); // LED responde ao botão sem esperar o sensor.
  while(Serial.available()) {char c=Serial.read();if(c=='f')falhaTeste=true;if(c=='n')falhaTeste=false;if(c=='h')usarHisterese=true;if(c=='b'){usarHisterese=false;alarmeTermico=false;}}
  if(millis()-ultimo<2000)return;
  ultimo=millis();
  int bruto=analogRead(A0);float t=falhaTeste?NAN:dht.readTemperature();
  Serial.print(ultimo);Serial.print(',');Serial.print(pressionado);Serial.print(',');Serial.print(bruto);Serial.print(',');
  Serial.print(t);Serial.print(',');Serial.print(classificar(t,bruto));Serial.print(',');Serial.println(usarHisterese?"HISTERESE":"BASE");
}
