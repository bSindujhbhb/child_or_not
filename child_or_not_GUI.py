import tkinter as tk
import tensorflow as tf
from tkinter import filedialog 
from tkinter import * 
from PIL import Image, ImageTk 
import numpy as np

#Loading the Model 
from keras.models import load_model 
model=load_model('Age_Sex_Detection.h5')

# Initializing the GUI

top=tk.Tk()
top.geometry('800x600')
top.title('Child or not detector')
top.configure(background="#CDCDCD")

# Initializing the Labels (1 for age and 1 for Sex)
label1=Label(top, background="#CDCDCD", font=("arial", 15, "bold"))
label2=Label(top, background="#CDCDCD", font=('arial', 15, 'bold'))
sign_image=Label (top)

def Detect(file_path):
    global Label_packed
    image = Image.open(file_path)
    image = image.resize((48, 48), resample=Image.BICUBIC)  # Choose a resampling method, e.g., BICUBIC
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    image = np.delete(image, 0, 1)
    image = np.resize(image, (48, 48, 3))
    print(image.shape)
    image = np.array([image]) / 255
    pred = model.predict(image)
    age = int(np.round(pred[1][0]))
    if age <= 12:
        result_text = f"Predicted Age is {age}\nChild"
        label1.configure(foreground="#811638", text=result_text)
    else:
        result_text = f"Predicted Age is {age}\nNot a Child"
        label1.configure(foreground="#811638", text=result_text)
        
def show_Detect_button(file_path):
    Detect_b=Button(top, text="Detect Image", command=lambda: Detect(file_path),padx=10,pady=5) 
    Detect_b.configure(background="#364156", foreground='white', font=('arial', 10, 'bold')) 
    Detect_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        show_Detect_button(file_path)
    except:
        pass

upload=Button(top, text="Upload an Image", command=upload_image,padx=10,pady=5) 
upload.configure(background="#364156", foreground='white', font=('arial', 10, 'bold')) 
upload.pack(side="bottom",pady=50)
sign_image.pack(side='bottom', expand=True)
label1.pack(side="bottom",pady=50)
label2.pack(side="bottom",pady=50)
heading=Label(top, text="Child or not detector", pady=20, font=("arial", 20, "bold"))
heading.configure(background="#CDCDCD", foreground="#364156")
heading.pack()
top.mainloop()