# #############################################################################
# ### GPIO
# ### V 1.00
# #############################################################################
from machine import Pin, I2C # type: ignore
import libs.mcp23017_raw as mcp23017
from time import sleep # type: ignore


class GPIO:

    def __init__(self):
        self.i2c        = I2C(0, scl=Pin(21), sda=Pin(20))
        self.mcp        = mcp23017.MCP23017(self.i2c, 0x20)
        self.inputs     = 0x00
        self.outputs    = 0x00
        self.blink      = True

    def get_input_byte(self):
        self.inputs = int.from_bytes(self.mcp._read(0x13, 1), 'big')
        return self.inputs

    def get_input_bit(self, bit):
        self.inputs = int.from_bytes(self.mcp._read(0x13, 1), 'big')
        return self.inputs & ( 1 << bit)
    
    def get_value_bit(self, bit):
        return self.inputs & ( 1 << bit)

    def set_output_byte(self, value=None):
        if not value == None:
            self.outputs = value
        self.mcp._write([0x12, self.outputs])
        return self.outputs
    
    def set_output_bit(self, bit, value):
        if value == "On":
            self.outputs = self.outputs | ( 1 << bit)
        else:
            self.outputs = self.outputs & ~( 1 << bit)
        self.mcp._write([0x12, self.outputs])
        return self.outputs

    def do_blink(self):
        if self.blink:
            self.mcp._write([0x12, self.outputs])
            self.blink = False
        else:
            self.mcp._write([0x12, 0x00])
            self.blink = True
        return self.blink


# -----------------------------------------------------------------------------
def main():

    print("=== Start Main -> Module_GPIO ===")
    LOOP_DELAY = 0.3

    try:
        print("Start")

        gpio = GPIO()
        gpio.set_output_byte(0xAA)

        while(True):

            gpio.do_blink()
            sleep(LOOP_DELAY)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")
        gpio.set_output_byte(0x00)
        
    print("=== End Main ===")

# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
