import tkinter as tk
from PIL import ImageTk, Image

BUTTON_BG_COLOR = "#136DC7"
BUTTON_FG_COLOR = "#FFFFFF"
BUTTON_ACTIVE_BG_COLOR = "#61677A"
BUTTON_HOVER_BG_COLOR = "#A0A0A0" 
INFO_BG_COLOR = "#D8D9DA"
INFO_FG_COLOR = "#000000"
INFO_FONT = ("Times New Roman", 20, "bold")

ics_info = {
   "LM741": {
        "range": "Single Operational Amplifier",
        "application": "Amplification and Signal Conditioning",
        "advantages": "Simple and widely used",
        "disadvantages": "Low bandwidth, not suitable for high-frequency applications",
        "working_conditions": "Supply Voltage: ±5V to ±22V\nTemperature: -55°C to +125°C",
        "image" : 'C:\\Users\\user\\Desktop\\ic images\LM741.png'

    },
    "NE555": {
        "range": "Timer",
        "application": "Pulse generation, oscillation, and time delay",
        "advantages": "Versatile and widely used for timing applications",
        "disadvantages": "Limited maximum operating frequency",
        "working_conditions": "Supply Voltage: 4.5V to 15V\nTemperature: 0°C to +70°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\NE555.jpeg'
    },
    "ATmega328P": {
        "range": "Microcontroller",
        "application": "Embedded Systems, IoT, Robotics",
        "advantages": "Highly versatile, large community support",
        "disadvantages": "Limited processing power compared to higher-end microcontrollers",
        "working_conditions": "Supply Voltage: 1.8V to 5.5V\nTemperature: -40°C to +85°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\ATmega328P.jpg'
    },
    "LM7805": {
        "range": "Voltage Regulator",
        "application": "Voltage regulation in electronic circuits",
        "advantages": "Stable and reliable output voltage",
        "disadvantages": "Requires heat sink for high current applications",
        "working_conditions": "Input Voltage: 7V to 25V\nTemperature: 0°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM7805.png'
    },
    "CD4017": {
        "range": "Decade Counter",
        "application": "Frequency dividers, LED chasers, and sequential controllers",
        "advantages": "Easy to use, simple implementation",
        "disadvantages": "Limited maximum clock frequency",
        "working_conditions": "Supply Voltage: 3V to 15V\nTemperature: -55°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\CD4017.jpeg'
    },
    "CD4011": {
        "range": "Quad 2-input NAND Gate",
        "application": "Logic gates, digital circuits",
        "advantages": "Multiple NAND gates in a single package",
        "disadvantages": "Higher propagation delay compared to single gates",
        "working_conditions": "Supply Voltage: 3V to 18V\nTemperature: -55°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\CD4011.png'
    },
    "LM386": {
        "range": "Low Voltage Audio Power Amplifier",
        "application": "Audio amplification for small speakers",
        "advantages": "Low power consumption, suitable for battery-powered devices",
        "disadvantages": "Limited output power for large speakers",
        "working_conditions": "Supply Voltage: 4V to 12V\nTemperature: -40°C to +85°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM386.jpg'
    },
    "LM317": {
        "range": "Adjustable Voltage Regulator",
        "application": "Precise voltage regulation in electronic circuits",
        "advantages": "Adjustable output voltage, easy to use",
        "disadvantages": "Requires external components for proper operation",
        "working_conditions": "Input Voltage: 3V to 40V\nTemperature: 0°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM317.png'
    },
    "74HC595": {
        "range": "8-Bit Shift Register",
        "application": "Serial-to-parallel data conversion, LED displays",
        "advantages": "Easy expansion of output pins",
        "disadvantages": "Limited current sourcing capability",
        "working_conditions": "Supply Voltage: 2V to 6V\nTemperature: -40°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\HC595.jpg'
    },
    "SN74LS04": {
        "range": "Hex Inverter",
        "application": "Logic gates, digital circuits",
        "advantages": "High-speed operation, low propagation delay",
        "disadvantages": "Not suitable for high-current applications",
        "working_conditions": "Supply Voltage: 4.75V to 5.25V\nTemperature: 0°C to +70°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\SN74LS04.png'
    },
    "LM324": {
        "range": "Quad Operational Amplifier",
        "application": "Signal conditioning, audio applications",
        "advantages": "Low cost and widely available",
        "disadvantages": "Lower bandwidth and slew rate compared to some other op-amps",
        "working_conditions": "Supply Voltage: 3V to 32V\nTemperature: 0°C to +70°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM324.png'
    },
    "LM555": {
        "range": "Timer",
        "application": "Pulse generation, oscillation, and time delay",
        "advantages": "Wide supply voltage range, simple design",
        "disadvantages": "Limited maximum operating frequency",
        "working_conditions": "Supply Voltage: 4.5V to 15V\nTemperature: 0°C to +70°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM555.png'
    },
    "CD4060": {
        "range": "14-Stage Binary Ripple Counter",
        "application": "Frequency dividers, timers, and clock generation",
        "advantages": "Wide supply voltage range, easy-to-use ripple counter",
        "disadvantages": "Limited maximum clock frequency",
        "working_conditions": "Supply Voltage: 3V to 15V\nTemperature: -55°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\CD4060.png'
    },
    "ATmega2560": {
        "range": "Microcontroller",
        "application": "Advanced embedded systems, robotics, 3D printers",
        "advantages": "High memory and I/O capabilities",
        "disadvantages": "Higher power consumption compared to lower-end microcontrollers",
        "working_conditions": "Supply Voltage: 1.8V to 5.5V\nTemperature: -40°C to +85°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\ATmega2560.png'
    },
    "LM317T": {
        "range": "Adjustable Voltage Regulator",
        "application": "Precise voltage regulation in electronic circuits",
        "advantages": "Adjustable output voltage, easy to use",
        "disadvantages": "Requires heat sink for high current applications",
        "working_conditions": "Input Voltage: 3V to 40V\nTemperature: 0°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM317T.jpeg'
    },
    "LM431": {
        "range": "Adjustable Precision Zener Shunt Regulator",
        "application": "Voltage reference and regulation",
        "advantages": "High precision and low temperature coefficient",
        "disadvantages": "Limited current sourcing capability",
        "working_conditions": "Supply Voltage: 2.5V to 36V\nTemperature: -40°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM431.png'
    },

    "LM7812": {
        "range": "Voltage Regulator",
        "application": "Positive voltage regulation in electronic circuits",
        "advantages": "Stable and reliable output voltage",
        "disadvantages": "Requires heat sink for high current applications",
        "working_conditions": "Input Voltage: 14.5V to 35V\nTemperature: 0°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM7812.png'
    },
    "CD4046": {
        "range": "Phase-Locked Loop (PLL)",
        "application": "Frequency synthesis, frequency demodulation",
        "advantages": "Wide frequency range, versatile PLL functions",
        "disadvantages": "Requires external components for proper operation",
        "working_conditions": "Supply Voltage: 3V to 18V\nTemperature: -55°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\CD4046.jpeg'
    },
    "LM386N": {
        "range": "Low Voltage Audio Power Amplifier",
        "application": "Audio amplification for small speakers",
        "advantages": "Low power consumption, suitable for battery-powered devices",
        "disadvantages": "Limited output power for large speakers",
        "working_conditions": "Supply Voltage: 4V to 12V\nTemperature: -40°C to +85°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM386N.png'
    },
    "74LS138": {
        "range": "3-to-8 Line Decoder/Demultiplexer",
        "application": "Address decoding, memory selection",
        "advantages": "Multiple decoders in a single package",
        "disadvantages": "Limited fan-out and current sourcing capability",
        "working_conditions": "Supply Voltage: 4.75V to 5.25V\nTemperature: 0°C to +70°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LS138.png'

    },
    "CD4013": {
        "range": "Dual D-type Flip-Flop",
        "application": "Memory elements, data storage",
        "advantages": "Simple and easy-to-use flip-flop",
        "disadvantages": "Limited clock frequency and propagation delay",
        "working_conditions": "Supply Voltage: 3V to 18V\nTemperature: -55°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\CD4013.png'
    },
    "LM339": {
        "range": "Quad Comparator",
        "application": "Voltage level detection, signal conditioning",
        "advantages": "Multiple comparators in a single package",
        "disadvantages": "Limited speed and output current",
        "working_conditions": "Supply Voltage: 2V to 36V\nTemperature: 0°C to +70°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM339.png'
    },
    "LM324N": {
        "range": "Quad Operational Amplifier",
        "application": "Signal conditioning, audio applications",
        "advantages": "Low cost and widely available",
        "disadvantages": "Lower bandwidth and slew rate compared to some other op-amps",
        "working_conditions": "Supply Voltage: 3V to 32V\nTemperature: 0°C to +70°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\LM339.png'
    },
    "CD4026": {
        "range": "Decade Counter with 7-Segment Decoder/Driver",
        "application": "Frequency dividers, 7-segment display driver",
        "advantages": "Integrated 7-segment display driver",
        "disadvantages": "Limited maximum clock frequency",
        "working_conditions": "Supply Voltage: 3V to 15V\nTemperature: -55°C to +125°C",
"image" : 'C:\\Users\\user\\Desktop\\ic images\\CD4026.png'
    },
}

def show_info(ic_name):
    info_window = tk.Toplevel(root)
    info_window.title(ic_name + " Information")
    info_window.configure(bg=INFO_BG_COLOR)

    Range = "Name : " + ics_info[ic_name]["range"]
    Working = "Working conditions : " + ics_info[ic_name]["working_conditions"]
    Application = "Applications : " + ics_info[ic_name]["application"]
    Advantages = "Advantages :  " + ics_info[ic_name]["advantages"]
    Disadvantages = "Disadvantages : " + ics_info[ic_name]["disadvantages"]

    info_label = tk.Label(info_window, text=Range + "\n" + Working + "\n" + Application + "\n" + Advantages + "\n" + Disadvantages,
                          bg=INFO_BG_COLOR, fg=INFO_FG_COLOR, font=INFO_FONT, anchor="w")
    info_label.grid(row=0, column=0, padx=10, pady=5)

    image_path = ics_info[ic_name]["image"]
    img = Image.open(image_path)
    img = img.resize((300, 300))  # Resize image for display
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(info_window, image=photo, bg=INFO_BG_COLOR)
    image_label.image = photo
    image_label.grid(row=0, column=1, padx=10, pady=5)

    # Adding the back button
    back_button = tk.Button(info_window, text="Back", command=info_window.destroy, bg=BUTTON_BG_COLOR,
                            fg=BUTTON_FG_COLOR, activebackground=BUTTON_ACTIVE_BG_COLOR,
                            font=("Times New Roman", 16, "bold"))
    back_button.grid(row=1, column=0, columnspan=2, pady=10)

def on_enter(event):
    event.widget['background'] = BUTTON_HOVER_BG_COLOR

def on_leave(event):
    event.widget['background'] = BUTTON_BG_COLOR

def create_buttons():
    frame = tk.Frame(root, bg=INFO_BG_COLOR)
    frame.pack(expand=True, padx=20, pady=20)

    row = 0
    column = 0

    for ic_name in ics_info.keys():
        button = tk.Button(frame, text=ic_name, command=lambda name=ic_name: show_info(name), bg=BUTTON_BG_COLOR,
                           fg=BUTTON_FG_COLOR, activebackground=BUTTON_ACTIVE_BG_COLOR, relief=tk.RIDGE, bd=2,
                           font=("Times New Roman", 11, "bold"))

        # Bind the hover functions to the button
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

        button.grid(row=row, column=column, padx=10, pady=5)

        column += 1
        if column > 1:
            column = 0
            row += 1

    frame.update_idletasks()
    x_offset = (root.winfo_width() - frame.winfo_width()) // 2
    y_offset = (root.winfo_height() - frame.winfo_height()) // 2
    root.geometry(f"+{x_offset}+{y_offset}")

root = tk.Tk()
root.title("IC Information Viewer")
root.configure(bg=INFO_BG_COLOR)

info_label = tk.Label(root, text="Select an IC to view information.", bg=INFO_BG_COLOR, fg=INFO_FG_COLOR,
                      font=INFO_FONT, anchor="w")
info_label.pack(pady=10)

create_buttons()

root.geometry("750x350")
root.mainloop()