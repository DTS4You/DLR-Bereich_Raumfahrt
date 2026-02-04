DLR-Bereich Raumfahrt
===============================================================================
Funktions-Zuordnung:
-------------------------------------------------------------------------------
01 -> Fairing                           -> LED 1 
02 -> Aerodynamische Steuerelemente     -> LED 2
03 -> Thermalstabile Strikturen         -> LED 3
04 -> Tankstrukturen                    -> LED 4
05 -> Satellitentechnologie             -> LED 5
06 -> Landebeine                        -> LED 6
07 -> Raumfahrtantriebe                 -> Stripe 3
08 -> Fertigungstechnologien            -> Stripe 5
09 -> Reserve oben links                -> Stripe 4
10 -> Reserve oben rechts               -> Stripe 1
11 -> Fertigungstechnologien            -> Stripe 2
...
...
===============================================================================
Hardware:
-------------------------------------------------------------------------------
Leiterplatte    : 24-0003-01-A

U101            -> 5V           -> Step-Down-Modul
JP 301          -> Brücke       -> 5V auf GPIO-Ausgänge
RN304, RN305    -> 120 R        -> Vorwiderstände LEDs
RN301           -> 10 K         -> I2C Input Pull-Down
R202, R203      -> 2K7          -> I2C SCL,SDA Pull-Up
RN302, RN303    -> 1K0          -> I2C Input Port-In
...
...
===============================================================================