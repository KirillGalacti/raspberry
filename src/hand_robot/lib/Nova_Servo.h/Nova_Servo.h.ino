/*
Servo.h - Библиотека сервоприводов с управлением прерываниями для Arduino, использующая 16-битные таймеры - Версия 2
 Авторское право (c) 2009 Майкл Марголис. Все права защищены.
 Эта библиотека является свободным программным обеспечением; вы можете распространять ее и/или изменять в соответствии с условиями GNU Lesser General Public
 Лицензия, опубликованная Фондом свободного программного обеспечения; 
 либо версия 2.1 Лицензии, либо (по вашему выбору) любая более поздняя версия.
 Эта библиотека распространяется в надежде, что она будет полезна,
 но БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ; даже без подразумеваемых гарантий ТОВАРНОЙ ПРИГОДНОСТИ или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННОЙ ЦЕЛИ. См. GNU
 Меньшая общая публичная лицензия для получения более подробной информации.
 Вы должны были получить копию GNU для широкой публики
 Лицензируйте вместе с этой библиотекой; если нет, запишите в Свободное программное обеспечение
 Foundation, Inc., 51 Franklin St, Пятый этаж, Бостон, Массачусетс 02110-1301 США
*/

/* 
 Сервопривод активируется путем создания экземпляра класса Servo, передающего нужный pin-код методу attach().
 Обратите внимание, что аналоговая запись ШИМ на выводах, связанных с таймером, отключается при подключении первого сервопривода.
 Таймеры захватываются по мере необходимости группами по 12 сервоприводов - 24 сервопривода используют два таймера, 48 сервоприводов будут использовать четыре.
 Последовательность, используемая для захвата таймеров, определена в timers.h
 Методы следующие:
 Servo - класс для управления серводвигателями, подключенными к выводам Arduino.
 attach (pin ) - присоединяет серводвигатель к контакту ввода-вывода.
 attach(pin, min, max) - присоединяется к pin, устанавливая минимальные и максимальные значения в микросекундах по умолчанию min равно 544, max равно 2400 
 
 write() - задает угол наклона сервопривода в градусах. (недопустимый угол, который действителен как импульс в микросекундах, обрабатывается как микросекунды)
 writeMicroseconds() - Устанавливает ширину сервоимпульса в микросекундах
 read() - Получает последнюю записанную ширину сервоимпульса в виде угла от 0 до 180. 
 readMicroseconds() - Получает последнюю записанную длительность сервоимпульса в микросекундах. (был read_us() в первом выпуске)
 attached() - Возвращает
 detach() - Останавливает пульсирование подключенного сервопривода на выводе ввода-вывода. 
 */

#ifndef Servo_h
#define Servo_h

#include <inttypes.h>

/* 
 * Определяет 16-битные таймеры, используемые с сервобиблиотекой 
 *
 * Если определено значение _useTimerX, то TimerX - это 16-разрядный таймер на текущей плате.
 * timer16_Sequence_t перечисляет последовательность, в которой должны быть выделены таймеры
 * _Nbr_16timers указывает, сколько 16-разрядных таймеров доступно.
*/

// Architecture specific include
#if defined(ARDUINO_ARCH_AVR)
#include "avr/ServoTimers.h"
#elif defined(ARDUINO_ARCH_SAM)
#include "sam/ServoTimers.h"
#elif defined(ARDUINO_ARCH_SAMD)
#include "samd/ServoTimers.h"
#elif defined(ARDUINO_ARCH_STM32F4)
#include "stm32f4/ServoTimers.h"
#elif defined(ARDUINO_ARCH_NRF52)
#include "nrf52/ServoTimers.h"
#elif defined(ARDUINO_ARCH_MEGAAVR)
#include "megaavr/ServoTimers.h"
#elif defined(ARDUINO_ARCH_MBED)
#include "mbed/ServoTimers.h"
#else
#error "This library only supports boards with an AVR, SAM, SAMD, NRF52 or STM32F4 processor."
#endif

#define Servo_VERSION           2     // software version of this library

#define MIN_PULSE_WIDTH       544     // the shortest pulse sent to a servo  
#define MAX_PULSE_WIDTH      2400     // the longest pulse sent to a servo 
#define DEFAULT_PULSE_WIDTH  1500     // default pulse width when servo is attached
#define REFRESH_INTERVAL    20000     // minimum time to refresh servos in microseconds 

#define SERVOS_PER_TIMER       12     // the maximum number of servos controlled by one timer 
#define MAX_SERVOS   (_Nbr_16timers  * SERVOS_PER_TIMER)

#define INVALID_SERVO         255     // flag indicating an invalid servo index

#if !defined(ARDUINO_ARCH_STM32F4)

typedef struct  {
  uint8_t nbr        :6 ;             // a pin number from 0 to 63
  uint8_t isActive   :1 ;             // true if this channel is enabled, pin not pulsed if false 
} ServoPin_t   ;  

typedef struct {
  ServoPin_t Pin;
  volatile unsigned int ticks;
} servo_t;

struct name{
  float Servo_1;
  float Servo_2;
  float Servo_3;
  }

class Servo
{
public:
  Servo();
  uint8_t attach(int name);           // attach the given pin to the next free channel, sets pinMode, returns channel number or INVALID_SERVO if failure
  uint8_t attach(int name, int min, int max); // as above but also sets min and max values for writes. 
  void detach();
  void write(int value);             // if value is < 200 its treated as an angle, otherwise as pulse width in microseconds 
  void writeMicroseconds(int value); // Write pulse width in microseconds 
  int read();                        // returns current pulse width as an angle between 0 and 180 degrees
  int readMicroseconds();            // returns current pulse width in microseconds for this servo (was read_us() in first release)
  bool attached();                   // return true if this servo is attached, otherwise false 
private:
   uint8_t servoIndex;               // index into the channel data for this servo
   int8_t min;                       // minimum is this value times 4 added to MIN_PULSE_WIDTH    
   int8_t max;                       // maximum is this value times 4 added to MAX_PULSE_WIDTH   
};

#endif
#endif
