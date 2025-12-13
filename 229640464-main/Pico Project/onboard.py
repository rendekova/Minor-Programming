import machine
import time

# --- Global unit time for Morse ---
unit = 0.15

# --- Initialize onboard LED ---
led = machine.Pin("LED", machine.Pin.OUT)

# --- Basic Morse functions ---
def dit():
    led.value(1)
    print(".", end="")
    time.sleep(unit)
    led.value(0)
    time.sleep(unit)

def dah():
    led.value(1)
    print("-", end="")
    time.sleep(3 * unit)
    led.value(0)
    time.sleep(unit)

def letterspace():
    time.sleep(3 * unit)
    print(" ", end="")

def wordspace():
    time.sleep(7 * unit)
    print("   ", end="")

# --- Morse dictionary for "pico pi" ---
MORSE_CODE = {
    "a": [dit, dah],
    "c": [dah, dit, dah, dit],
    "i": [dit, dit],
    "o": [dah, dah, dah],
    "p": [dit, dah, dah, dit],
}

# --- Function to blink Morse message ---
def morse(message):
    print("\nMorse:", end=" ")
    for char in message.lower():
        if char == " ":
            wordspace()
        elif char in MORSE_CODE:
            for func in MORSE_CODE[char]:
                func()
            letterspace()
    print()  # new line after each word

# --- Function to get onboard temperature ---
def temperature():
    sensor = machine.ADC(4)  # internal temperature sensor
    conversion_factor = 3.3 / (65535)
    reading = sensor.read_u16() * conversion_factor
    temp_c = 27 - (reading - 0.706) / 0.001721  # formula from Pico docs
    return round(temp_c, 1)

# --- Function to get RTC time and date ---
def timer():
    rtc = machine.RTC()
    # Set your local timezone manually if needed (example: Netherlands = UTC+1)
    # Adjust this if your board's clock is off:
    # rtc.datetime((2024, 10, 20, 0, 15, 16, 17, 0))
    datetime = rtc.datetime()  # tuple: (year, month, day, weekday, hour, minute, second, subsecond)
    year, month, day, _, hour, minute, second, _ = datetime
    # Format it into sortable YYYY-MM-DD HH:MM:SS
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

# --- Main program ---
def main():
    while True:
        # Get temperature and print it
        temp = temperature()
        print(f"\nPico Pi temperature is {temp:.1f} degrees Celsius.")

        # Check if too hot
        if temp >= 35:
            print(f"TOO HOT: {temp:.1f} degrees Celsius.")
            break

        # Print date and time
        print("Current date-time:", timer())

        # Blink "pico pi" in Morse
        morse("pico pi")

        # Wait 5 seconds before repeating
        time.sleep(5)

# --- Run program ---
main()