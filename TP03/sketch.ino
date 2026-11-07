const byte BTN=2,LED=8,POT=A0,N=5;
int janela[N]={0};long soma=0;byte indice=0,quantidade=0;
unsigned long anterior=0,amostra=0;
void setup(){pinMode(BTN,INPUT_PULLUP);pinMode(LED,OUTPUT);Serial.begin(9600);Serial.println("amostra,botao,bruto,pct,temp_C,estado,filtrado");}
void loop(){
 if(millis()-anterior<500)return; anterior=millis();
 int bruto=analogRead(POT);soma-=janela[indice];janela[indice]=bruto;soma+=bruto;indice=(indice+1)%N;if(quantidade<N)quantidade++;
 float pct=100.0*bruto/1023.0;
 const char* estado=pct>=85?"PERIGO":pct>=70?"ATENCAO":"NORMAL";
 digitalWrite(LED,pct>=85);
 Serial.print(amostra++);Serial.print(',');Serial.print(digitalRead(BTN)==LOW);Serial.print(',');Serial.print(bruto);Serial.print(',');Serial.print(pct,2);Serial.print(',');Serial.print(pct,2);Serial.print(',');Serial.print(estado);Serial.print(',');Serial.println((float)soma/quantidade,2);
}
