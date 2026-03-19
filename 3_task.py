import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO


def get_url():
    url = ("https://nekos.best/api/v2/neko")
    response = requests.get(url)
    return response.json()['results'][0]['url']

def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((300, 500), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

def next_img():
    url = get_url()
    photo = load_image_from_url(url)
    label.configure(image=photo)
    label.image = photo


root = tk.Tk()
root.title("Изображение из интернета")


url = get_url()
photo = load_image_from_url(url)

label = tk.Label(root, image=photo)
label.pack(pady=10)

button = tk.Button(root, text='Следующая картинка', command=next_img)
button.pack()
    
root.mainloop()