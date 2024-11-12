import tkinter as tk
from gpiozero import LED

# Setup LEDs connected to GPIO pins
led_a = LED(17)
led_b = LED(27)
led_c = LED(22)

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

# Create main window for the application with a larger size
main_window = tk.Tk()
main_window.title("LED Control")
main_window.geometry("500x500")  # Set the window size to 400x400

# Integer variable to store the selected LED
chosen_led = tk.IntVar()

# Display title label with larger font
label_heading = tk.Label(main_window, text="Select an LED to Turn On", font=("Times New Roman", 24))
label_heading.pack(pady=20)

# Create radio buttons for each LED control with larger font and padding
radio_led1 = tk.Radiobutton(main_window, text="LED A", variable=chosen_led, value=1, command=update_led, bg="red", font=("Arial", 18), indicatoron=0, padx=20, pady=10)
radio_led2 = tk.Radiobutton(main_window, text="LED B", variable=chosen_led, value=2, command=update_led, bg="white", font=("Arial", 18), indicatoron=0, padx=20, pady=10)
radio_led3 = tk.Radiobutton(main_window, text="LED C", variable=chosen_led, value=3, command=update_led, bg="yellow", font=("Arial", 18), indicatoron=0, padx=20, pady=10)

# Pack the radio buttons into the window with additional padding
radio_led1.pack(anchor=tk.W, padx=50, pady=10)
radio_led2.pack(anchor=tk.W, padx=50, pady=10)
radio_led3.pack(anchor=tk.W, padx=50, pady=10)

# Larger reset and exit buttons with increased padding and font
button_reset = tk.Button(main_window, text="Turn Off All LEDs", command=all_off, bg="gray", font=("Arial", 16), padx=20, pady=10)
button_reset.pack(pady=15)

button_exit = tk.Button(main_window, text="Close Program", command=exit_program, bg="gray", font=("Arial", 16), padx=20, pady=10)
button_exit.pack(pady=15)

main_window.mainloop()
