import tkinter as tk
from gpiozero import LED

# Setup LEDs connected to GPIO pins
led_a = LED(17)
led_b = LED(2)
led_c = LED(3)

# Ensure all LEDs are initially off
def all_off():
    led_a.off()
    led_b.off()
    led_c.off()

# Turn off all LEDs when the script starts
all_off()

# Function to control which LED is turned on
def control_led(selected_led):
    all_off()  # Make sure all other LEDs are off before turning one on
    if selected_led == 1:
        led_a.on()
    elif selected_led == 2:
        led_b.on()
    elif selected_led == 3:
        led_c.on()

# Triggered when a radio button is selected
def update_led():
    led_to_activate = chosen_led.get()
    control_led(led_to_activate)

# Close the application and turn off all LEDs
def exit_program():
    all_off()
    main_window.quit()

# Create main window for the application
main_window = tk.Tk()
main_window.title("LED Control")

# Integer variable to store the selected LED
chosen_led = tk.IntVar()

# Display title label
label_heading = tk.Label(main_window, text="Select an LED to Turn On", font=("Times New Roman", 18))
label_heading.pack(pady=15)

# Create radio buttons for each LED control
radio_led1 = tk.Radiobutton(main_window, text="LED A", variable=chosen_led, value=1, command=update_led)
radio_led2 = tk.Radiobutton(main_window, text="LED B", variable=chosen_led, value=2, command=update_led)
radio_led3 = tk.Radiobutton(main_window, text="LED C", variable=chosen_led, value=3, command=update_led)

# Pack the radio buttons into the window
radio_led1.pack(anchor=tk.W, padx=30)
radio_led2.pack(anchor=tk.W, padx=30)
radio_led3.pack(anchor=tk.W, padx=30)

button_reset = tk.Button(main_window, text="Turn Off All LEDs", command=all_off)
button_reset.pack(pady=10)

button_exit = tk.Button(main_window, text="Close Program", command=exit_program)
button_exit.pack(pady=10)

main_window.mainloop()