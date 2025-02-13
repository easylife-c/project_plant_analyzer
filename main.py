import pigpio
import config
import time

# Connect to the pigpio daemon
pi = pigpio.pi()
if not pi.connected:
    print("Error: Can't connect to pigpio daemon! Please run 'sudo pigpiod'")
    exit()

# Set up the GPIO pin (using BCM numbering)
PUMP_PIN = config.GPIO_PUMP_PIN
pi.set_mode(PUMP_PIN, pigpio.OUTPUT)

def pump_on():
    """Activates the pump."""
    print("Turning on pump...")
    pi.write(PUMP_PIN, 1)

def pump_off():
    """Deactivates the pump."""
    print("Turning off pump...")
    pi.write(PUMP_PIN, 0)

# For standalone testing of pump control:
if __name__ == "__main__":
    pump_on()
    time.sleep(100)  # Keep the pump on for 5 seconds
    pump_off()
