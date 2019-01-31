#include <Servo.h>
Servo obj;
int Pin=6;
int place =0;
int user=0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
obj.attach(Pin);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Enter num");
  while(Serial.available()==0){}
  user=Serial.parseInt();
  for(place=5;place<=175;place++){
  obj.write(place);
  if(user==place)
  {
    delay(4000);
    }
 delay(18);
  }
  

  for(place=175;place>=5;place--)
  {
    obj.write(place);
    delay(18);
    
  }

}
