#include <NTPClient.h>
// change next line to use with another board/shield
#include <ESP8266WiFi.h>
//#include <WiFi.h> // for WiFi shield
//#include <WiFi101.h> // for WiFi 101 shield or MKR1000
#include <WiFiUdp.h>

int buzzerPin = 14;//4;
const char *ssid     = "ziroom441";
const char *password = "4001001111";

WiFiUDP ntpUDP;

// You can specify the time server pool and the offset (in seconds, can be
// changed later with setTimeOffset() ). Additionaly you can specify the
// update interval (in milliseconds, can be changed using setUpdateInterval() ).
NTPClient timeClient(ntpUDP, "europe.pool.ntp.org", 3600, 60000);

void setup() {
  Serial.begin(115200);

  pinMode(buzzerPin, OUTPUT);
  //  digitalWrite(buzzerPin, LOW);


  WiFi.begin(ssid, password);
  Serial.println("connected WIFI");
  digitalWrite(buzzerPin, LOW);

  while ( WiFi.status() != WL_CONNECTED ) {
    delay ( 500 );
    Serial.print ( "." );
  }

  timeClient.begin();
  timeClient.setTimeOffset(28800);
}

void loop() {
//  digitalWrite(buzzerPin, LOW);
  timeClient.update();
  int hour = timeClient.getHours();
  int minute = timeClient.getMinutes();
  int Seconds = timeClient.getSeconds();
  Serial.print(hour);
  Serial.print(":");
  Serial.print(minute);
  Serial.print(":");
  Serial.println(Seconds);
  //  minute=Seconds;

  Serial.println(timeClient.getFormattedTime());
  for (int i = 0; i <= 15; i++) {//22-7
    if (hour == i) {
      //
      if (minute == 0) {
        Serial.println("minute == 0");
        for (int i = 0; i < 1; i++) {
          digitalWrite(buzzerPin, HIGH);
          Serial.println("HIGH");
          delay(500);
          digitalWrite(buzzerPin, LOW);
          Serial.println("LOW");
          delay(500);
        }
      }
      if (minute == 15) {
        Serial.println("minute == 15");
        for (int i = 0; i < 2; i++) {
          digitalWrite(buzzerPin, HIGH);
          Serial.println("HIGH");
          delay(500);
          digitalWrite(buzzerPin, LOW);
          Serial.println("LOW");
          delay(500);
        }
      }
      if (minute == 30) {
        Serial.println("minute == 30");
        for (int i = 0; i < 3; i++ ) {
          digitalWrite(buzzerPin, HIGH);
          Serial.println("HIGH");
          delay(500);
          digitalWrite(buzzerPin, LOW);
          Serial.println("LOW");
          delay(500);
        }
      }
      if (minute == 45) {
        Serial.println("minute == 45");
        for (int i = 0; i < 4; i++) {
          digitalWrite(buzzerPin, HIGH);
          Serial.println("HIGH");
          delay(500);
          digitalWrite(buzzerPin, LOW);
          Serial.println("LOW");
          delay(500);
        }
      }
    }
  }

  delay(60000);
}
