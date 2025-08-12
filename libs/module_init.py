# #############################################################################
# ### MyGlobal
# ### Bereich Raumfahrt V1.00
# #############################################################################

class Global_Module:
    
    inc_ws2812          = False
    inc_decoder         = False
    inc_serial          = False
    inc_i2c             = False


class Global_WS2812:

    numpix_1            = 16            # Anz. LEDs im 1. Stripe -> Boden 1
    numpix_2            = 16            # Anz. LEDs im 2. Stripe -> Boden 2
    numpix_3            = 16            # Anz. LEDs im 3. Stripe -> Boden 3
    numpix_4            = 16            # Anz. LEDs im 4. Stripe -> Boden 4
    numpix_5            = 16            # Anz. LEDs im 5. Stripe -> Boden 5
    # Gesamtzahl ermitteln !!!
    # Spiegel   = 68 + 241 = 309
    # Spiegel   = 241               ohne Rand !!!
    # Laser     = 23
    # Empfänger = 16
    # Summe     : 280 LEDs
    numpix_6            = 320           # Anz. LEDs im 6. Stripe -> Spiegel, Laser, Empfänger
    #numpix_1           = 256           # Anz. LEDs im 1. Stripe -> Test !!!

    #--------------------------------------------------------------------------
    # Strip -> LED Stripe -> Value - 1

    seg_1_01    = ( 1 ,            #  1. Line -> 1. Seg -> Teil 1.1
                    0 , 
                    8 )

    seg_1_02    = ( 1 ,            #  1. Line -> 2. Seg -> Teil 1.2
                    seg_1_01[1] - 1 , 
                    8 )

    seg_1_03    = ( 1 ,            #  1. Line -> 3. Seg -> Teil 1.3
                    seg_1_02[1] - 1 ,
                    8 )

    #--------------------------------------------------------------------------

    
# -----------------------------------------------------------------------------

    color_def           = (  0,  0,  2)
    color_off           = (  0,  0,  0)
    color_on            = (255, 10, 10)
    color_dot           = (110,  2,  2)
    color_half          = (110,  2,  2)
    color_blink_on      = (255, 20, 20)
    color_blink_off     = (  0,  0,  5)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz

#==============================================================================

def main():

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.seg_1_01[0], mg.seg_1_01[1], mg.seg_1_01[2])
    #print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------