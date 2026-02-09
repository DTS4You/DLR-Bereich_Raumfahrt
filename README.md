DLR-Bereich Raumfahrt
===============================================================================
Funktions-Zuordnung:
-------------------------------------------------------------------------------
01 -> Fairing                           -> LED 6    -> Bit 5
02 -> Aerodynamische Steuerelemente     -> LED 3    -> Bit 2
03 -> Thermalstabile Strikturen         -> LED 5    -> Bit 4
04 -> Tankstrukturen                    -> LED 2    -> Bit 1
05 -> Satellitentechnologie             -> LED 4    -> Bit 3
06 -> Landebeine                        -> LED 1    -> Bit 0
07 -> Raumfahrtantriebe                 -> Stripe 3 -> Obj. 2
08 -> Fertigungstechnologien            -> Stripe 5 -> Obj. 4
09 -> Reserve oben links                -> Stripe 4 -> Obj. 3
10 -> Reserve oben rechts               -> Stripe 1 -> Obj. 0
11 -> Fertigungstechnologien            -> Stripe 2 -> Obj. 1
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

ToDo

Menü -> Trägerrakete
-> 25 -> Aero, Fairing, Lanfebeine, Tank


Back Link -> Deutsch -> Menü Trägerrakete springt auf Eng.


Menübaum nicht von der Home-seite ansteuerbar


