// Controlador de cinco fases: demostracion para jugador 1 vs jugador 2.
// Los botones representan eventos del juego; este montaje no calcula puntajes.
// LED Q0..Q4: pines 12, 11, 10, 9, 8, cada uno con resistencia de 1 kohm.
// Botones a GND: A0 inicio, A1 otra ronda, A2 ganador, A3 reinicio.

enum Estado { ESPERA, INICIO, PREPARACION, EVALUACION, FIN };
const byte LEDS[] = {12, 11, 10, 9, 8};
const byte BOTONES[] = {A0, A1, A2, A3};
const unsigned long TIEMPO_INICIO = 1500;
const unsigned long TIEMPO_PREPARACION = 2000;
const unsigned long ANTIRREBOTE = 30;

Estado estado = ESPERA;
unsigned long entradaEstado = 0;
bool lecturaAnterior[4] = {HIGH, HIGH, HIGH, HIGH};
bool estable[4] = {HIGH, HIGH, HIGH, HIGH};
unsigned long ultimoCambio[4] = {0, 0, 0, 0};

void mostrarEstado() {
  for (byte i = 0; i < 5; i++) digitalWrite(LEDS[i], i == estado ? HIGH : LOW);
  Serial.print("Q");
  Serial.print((int)estado);
  Serial.print(" - ");
  switch (estado) {
    case ESPERA: Serial.println("ESPERA: pulsa INICIAR"); break;
    case INICIO: Serial.println("INICIO: inicializando (1,5 s)"); break;
    case PREPARACION: Serial.println("PREPARACION de ronda (2 s)"); break;
    case EVALUACION: Serial.println("EVALUACION: pulsa OTRA RONDA o GANADOR"); break;
    case FIN: Serial.println("FIN: pulsa REINICIAR para volver a Q0"); break;
  }
}

void cambiarEstado(byte siguiente) {
  estado = (Estado)siguiente;
  entradaEstado = millis();
  mostrarEstado();
}

bool pulsado(byte i) {
  bool lectura = digitalRead(BOTONES[i]);
  if (lectura != lecturaAnterior[i]) ultimoCambio[i] = millis();
  lecturaAnterior[i] = lectura;
  if (millis() - ultimoCambio[i] >= ANTIRREBOTE && lectura != estable[i]) {
    estable[i] = lectura;
    return estable[i] == LOW;
  }
  return false;
}

void evento(char orden) {
  if (orden == 'r' || orden == 'R') {
    cambiarEstado(ESPERA);
  } else if ((orden == 'i' || orden == 'I') && estado == ESPERA) {
    cambiarEstado(INICIO);
  } else if (estado == EVALUACION) {
    // GANADOR representa ronda resuelta CON ganador (F=1, V=1).
    if (orden == 'g' || orden == 'G') cambiarEstado(FIN);
    // OTRA RONDA representa ronda resuelta SIN ganador (F=1, V=0).
    else if (orden == 'n' || orden == 'N') cambiarEstado(PREPARACION);
  }
}

void setup() {
  Serial.begin(9600);
  for (byte i = 0; i < 5; i++) pinMode(LEDS[i], OUTPUT);
  for (byte i = 0; i < 4; i++) pinMode(BOTONES[i], INPUT_PULLUP);
  Serial.println("JUDGE - CONTROLADOR DE CINCO FASES");
  Serial.println("Botones o monitor serie: I=iniciar, N=otra ronda, G=ganador, R=reiniciar");
  cambiarEstado(ESPERA); // Arranque definido: Q0 encendido sin tocar nada.
}

void loop() {
  bool inicio = pulsado(0);
  bool ronda = pulsado(1);
  bool ganador = pulsado(2);
  bool reinicio = pulsado(3);
  if (reinicio) evento('R'); // Reinicio tiene prioridad.
  else if (ganador) evento('G');
  else if (ronda) evento('N');
  else if (inicio) evento('I');

  while (Serial.available()) evento(Serial.read());

  unsigned long transcurrido = millis() - entradaEstado;
  if (estado == INICIO && transcurrido >= TIEMPO_INICIO) cambiarEstado(PREPARACION);
  else if (estado == PREPARACION && transcurrido >= TIEMPO_PREPARACION) cambiarEstado(EVALUACION);
}
