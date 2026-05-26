
import customtkinter as ctk
import requests
import speech_recognition as sr

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

root.geometry("700x500")

root.title("AI Email Assistant")


title = ctk.CTkLabel(
    root,
    text="AI Email Assistant",
    font=("Arial",30,"bold")
)

title.pack(pady=20)

label = ctk.CTkLabel(
    root,
    text="Enter Email Prompt:",
    font=("Arial",18)
)

label.pack(pady=10)

text_entry = ctk.CTkEntry(
    root,
    width=500,
    height=40,
    font=("Arial",16)
)

text_entry.pack(pady=10)

def generate():

    text = text_entry.get()

    response = requests.get(
        "http://127.0.0.1:5000",
        params={
            "text": text
        }
    )

    result = response.text

    result_box.delete("1.0", "end")

    result_box.insert("end", result)

button = ctk.CTkButton(
    root,
    text="Generate",
    command=generate,
    fg_color="#2563eb",
    hover_color="#1d4ed8"
)
button.pack(pady=20)





result_box = ctk.CTkTextbox(
    root,
    width=600,
    height=150,
    font=("Arial",16)
)

result_box.pack(pady=20)
def voice_input():

    r = sr.Recognizer()

    with sr.Microphone() as source:
         r.adjust_for_ambient_noise(source)

         audio = r.listen(source,timeout=8)

    text = r.recognize_google(audio)

    text_entry.delete(0, "end")

    text_entry.insert(0, text)
    
voice_button = ctk.CTkButton(
    root,
    text="Voice Input",
    command=voice_input
)
voice_button.pack(pady=10)

root.mainloop()