int PIEZOPIN = 5;
int PAUSE = 500;
// One octave of notes between A4 and A5
int note_Bb3 = 233;
int note_B3 = 247;
int note_C4 = 262;
int note_Cs4 = 277; int note_Db4 = note_Cs4;
int note_D4 = 294;
int note_Ds4 = 311; int note_Eb4 = note_Ds4;
int note_E4 = 330;
int note_F4 = 349; int note_Es4 = note_F4;
int note_Fs4 = 370; int note_Gb4 = note_Fs4;
int note_G4 = 392;
int note_Gs4 = 415; int note_Ab4 = note_Gs4;
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;

int note_A5 = note_A4 * 2;
int note_As5 = note_As4 * 2; int note_Bb5 = note_As5;
int note_B5 = note_B4 * 2;

int note_rest = -1;

// note lengths defined here
long whole_note = 1600; // change tempo by changing duration of one measure
long half_note = whole_note / 2;
long quarter_note = whole_note / 4;
long eighth_note = whole_note / 8;
long sixteenth_note = whole_note / 16;
long dotted_quarter_note = quarter_note + eighth_note;
long dotted_eighth_note = eighth_note + sixteenth_note;
long dotted_half_note = half_note + quarter_note;

// WRITE YOUR SONG HERE
long song[39][3]{
  {note_Bb4, eighth_note, 250}, //we’re
  {note_Bb5, dotted_quarter_note, 750}, //soar
  {note_G5, eighth_note, 250}, //in
  {note_rest, half_note, 1000}, //rest
  {note_Bb5, dotted_quarter_note, 750}, //fly
  {note_G5, eighth_note, 250}, //in
  {note_rest, half_note , 1000}, // rest
  {note_G5, eighth_note, 250},//there’s
  {note_Ab5, eighth_note, 250},//not
  {note_G5, eighth_note, 250},//a
  {note_F5, quarter_note, 500},//star
  {note_Eb5, quarter_note, 500},//in
  {note_G5, quarter_note, 500},//heav
  {note_Ab5, eighth_note, 250},//en
  {note_G5, eighth_note, 250},//that
  {note_F5, quarter_note, 500},//we
  {note_Eb5, quarter_note, 500}, //can’t
  {note_G5, dotted_quarter_note, 500}, //reach
  {note_rest, dotted_quarter_note, 750},
  {note_G5, eighth_note, 250},//if
  {note_F5, eighth_note, 250},
  {note_F5, quarter_note, 500},
  {note_G5, eighth_note, 250},
  {note_F5, dotted_quarter_note, 750},
  {note_F5, eighth_note, 250},
  {note_F5,eighth_note, 250},
  {note_F5, eighth_note, 250},
  {note_Eb5, eighth_note, 250},
  {note_Eb5, dotted_quarter_note, 2000}, // free
};

bool staccato = true;
int PAPAUSE = 0;

void setup() {
  Serial.begin(9600);
  pinMode(PIEZOPIN, OUTPUT);
}
void loop() {
  //PLAY YOUR SONG HERE
  for (int i = 0; i < 39; i++){
    tone(PIEZOPIN, song[i][0], song[i][1]);
    delay(song[i][2]);
  }
}
