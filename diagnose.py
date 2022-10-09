from inky import Inky7Colour as Inky

display = Inky()

print(f"Found: {display.eeprom().get_variant()}")
print(display)
