const int LDR_E = A0, LDR_O = A1;       // divisores de tensión
const int IN1 = 7, IN2 = 8, ENA = 9;      // driver puente H
const int FIN_E = 2, FIN_O = 3;           // finales de carrera (INPUT_PULLUP)
const int ZONA_MUERTA = 40;               // cuentas ADC
const int UMBRAL_NOCHE = 100;             // luz mínima para seguir
const int VELOCIDAD = 200;                // PWM 0-255
const unsigned long PERIODO_MS = 10000, PULSO_MS = 1500;
 
void setup() {
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT); pinMode(ENA, OUTPUT);
  pinMode(FIN_E, INPUT_PULLUP); pinMode(FIN_O, INPUT_PULLUP);
  detener();
}
