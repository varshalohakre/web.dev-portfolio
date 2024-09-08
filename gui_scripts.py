from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, filedialog, Label
from PIL import Image, ImageTk
import cv2
import webbrowser

# Define paths
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\lohak\Desktop\wallpaper\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_link(url):
    webbrowser.open(url)

# Function to play video
def play_video(file_path):
    cap = cv2.VideoCapture(file_path)
    
    # Function to display video frames
    def show_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = img.resize((600, 350), Image.LANCZOS)  # Resize image for display area
            img_tk = ImageTk.PhotoImage(img)
            canvas.itemconfig(image_1, image=img_tk)
            canvas.image = img_tk  # Keep a reference to avoid garbage collection
            window.after(33, show_frame)  # Continue after 33 ms (~30 frames per second)
        else:
            cap.release()  # Release video capture when video ends

    show_frame()

def upload_file():
    # Allow user to choose an image or video file
    file_path = filedialog.askopenfilename(title="Select an Image or Video File", filetypes=[("Image/Video Files", "*.jpg;*.jpeg;*.png;*.mp4;*.avi")])
    if file_path:
        if file_path.endswith(('.jpg', '.jpeg', '.png')):
            img = Image.open(file_path)
            img = img.resize((600, 350), Image.LANCZOS)  # Use Image.LANCZOS to resize image
            img = ImageTk.PhotoImage(img)
            canvas.itemconfig(image_1, image=img)
            canvas.image = img  # Keep a reference to avoid garbage collection
        elif file_path.endswith(('.mp4', '.avi')):
            play_video(file_path)  # Play video using OpenCV and display in Tkinter

# Initialize the main window
window = Tk()
window.title("Counterfakes")  # Set the title of the window
window.geometry("1280x720")
window.configure(bg="#FFFFFF")

# Create canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Create background rectangles
canvas.create_rectangle(
    50.0,
    197.0,
    655.0,
    548.0,
    fill="#D0D9EC",
    outline=""
)

canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    97.0,
    fill="#3066B7",
    outline=""
)

# Detect Button (YouTube link)
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    window,
    image=button_image_1,
    text="Detect",
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_link("https://www.youtube.com"),  # Link to YouTube
    relief="flat",
    font=("Arial", 14),
    fg="white"  # Set text color to white
)
button_1.place(
    x=877.0,
    y=582.0,
    width=204.0,
    height=52.0
)

button_image_hover_1 = PhotoImage(file=relative_to_assets("button_hover_1.png"))

def button_1_hover(e):
    button_1.config(image=button_image_hover_1, text="", compound="center")  # Hide text on hover

def button_1_leave(e):
    button_1.config(image=button_image_1, text="", compound="center")  # Show text when not hovering

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)

# Upload Button (Upload functionality)
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    window,
    image=button_image_2,
    text="Upload",
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command=upload_file,
    relief="flat",
    font=("Arial", 14),
    fg="white"  # Set text color to white
)
button_2.place(
    x=234.0,
    y=583.0,
    width=238.0,
    height=52.0
)

button_image_hover_2 = PhotoImage(file=relative_to_assets("button_hover_2.png"))

def button_2_hover(e):
    button_2.config(image=button_image_hover_2, text="", compound="center")  # Hide text on hover

def button_2_leave(e):
    button_2.config(image=button_image_2, text="Upload", compound="center")  # Show text when not hovering

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)

# About Us Button (YouTube link)
about_us_button = Button(
    window,
    text="ABOUT US",
    command=lambda: open_link("https://www.youtube.com"),
    font=("Arial", 15),
    bg="#3166B7",
    fg="light grey",
    borderwidth=0,
    relief="flat"
)
about_us_button.place(
    x=34.0,
    y=49.0
)

# Contact Us Button (YouTube link)
contact_us_button = Button(
    window,
    text="CONTACT US",
    command=lambda: open_link("https://www.youtube.com"),
    font=("Arial", 15),
    bg="#3166B7",
    fg="light grey",
    borderwidth=0,
    relief="flat"
)
contact_us_button.place(
    x=162.0,
    y=48.0
)

# Create Images and Text
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    352.0,
    372.0,
    image=image_image_1
)

canvas.create_text(
    337.0,
    32.0,
    anchor="nw",
    text="DEEPFAKE DETECTION",
    fill="#FFFFFF",
    font=("Roboto", 36 * -1)
)

canvas.create_text(
    450.0,
    132.0,
    anchor="nw",
    text="upload image/video",
    fill="#7B5353",
    font=("Roboto", 36 * -1)
)

canvas.create_rectangle(
    712.0,
    202.0,
    1246.0,
    544.0,
    fill="#FAF5F5",
    outline=""
)

canvas.create_text(
    846.0,
    248.0,
    anchor="nw",
    text="ACCURACY PERCENTAGE%",
    fill="#000000",
    font=("RobotoRoman Bold", 24 * -1)
)

canvas.create_rectangle(
    916.0,
    269.0,
    1031.0,
    307.0,
    fill="#D9D9D9",
    outline=""
)

canvas.create_rectangle(
    748.0,
    374.0,
    1200.0,
    515.0,
    fill="#D9D9D9",
    outline=""
)

canvas.create_text(
    821.0,
    397.0,
    anchor="nw",
    text="UPLOADED IMAGE/VIDEO IS ",
    fill="#000000",
    font=("RobotoRoman Bold", 24 * -1)
)

window.resizable(False, False)
window.mainloop()
