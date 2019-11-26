#include <Arduino.h>


// Needed due to preprocessor issues.
#ifdef PLUGIN_SET_GENERIC_ESP32
  #ifndef ESP32
    #define ESP32
  #endif
#endif

void setup() {

  #ifdef USES_P001
  #warning "USES_P001 defined"
  #else
    #warning "USES_P001 NOT defined"
  #endif

}

void loop() {

}
