from machine import Pin import time

LED_PIN = 15 BUTTON_PIN = 14

led = Pin(LED_PIN, Pin.OUT) led.value(0)

blink_on = False

def button_irq(pin):
    global blink_on # Debounce-Logik rudimentär: kurze Pause verhindern mehrfache Trigger 
    if pin.value() == 0: # Taster gedrückt (LOW)
        blink_on = True # LED sofort kurz einschalten, um Reaktion zu zeigen
        led.value(1)
    else:
        pass

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

button.irq(trigger=Pin.IRQ_FALLING, handler=button_irq)


try:
    while True:
        if blink_on: # LED blinken lassen
            led.value(1)
            time.sleep(0.2)
            led.value(0)
            time.sleep(0.2) # Nach dem ersten Blinken wieder ausschalten, Flag zurücksetzen
            blink_on = False
        else: # Minimales Idle time.sleep(0.05)
except KeyboardInterrupt: # Saubere Beendigung
    led.value(0)
