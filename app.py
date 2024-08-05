import tkinter as tk
from tkinter import filedialog, ttk
from reportlab.pdfgen import canvas
from PIL import Image
import os

class ImageToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []   # All images will be saved in this
        self.output_pdf_name = tk.StringVar()

        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("Image To PDF Converter")
        self.root.geometry("500x700")
        self.root.config(bg="#f0f0f0")

        title_frame = tk.Frame(self.root, bg="#4a7abc")
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text="Image To PDF Converter", font=("Helvetica", 20, "bold"), bg="#4a7abc", fg="white")
        title_label.pack(pady=10)

        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        select_image_button = ttk.Button(main_frame, text="Select Images", command=self.select_images)
        select_image_button.pack(pady=(0, 10))

        self.selected_images_list = tk.Listbox(main_frame, selectmode=tk.MULTIPLE, height=10, bg="#e0e0e0", relief=tk.FLAT)
        self.selected_images_list.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

        label = tk.Label(main_frame, text="Enter the PDF Name: ", bg="#f0f0f0")
        label.pack()

        pdf_name_entry = ttk.Entry(main_frame, textvariable=self.output_pdf_name, width=40, justify='center')
        pdf_name_entry.pack()

        convert_button = ttk.Button(main_frame, text="Convert to PDF", command=self.convert_images_to_pdf)
        convert_button.pack(pady=(20, 40))

        self.progress = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress.pack(pady=(0, 20), fill=tk.X)

    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        self.update_selected_images_listbox()

    def update_selected_images_listbox(self):
        self.selected_images_list.delete(0, tk.END)

        for image_path in self.image_paths:
            _, image_name = os.path.split(image_path)
            self.selected_images_list.insert(tk.END, image_name)

    def convert_images_to_pdf(self):
        if not self.image_paths:
            return

        output_pdf_path = self.output_pdf_name.get() + ".pdf" if self.output_pdf_name.get() else "output.pdf"

        pdf = canvas.Canvas(output_pdf_path, pagesize=(612, 792))

        # to put images in the center
        self.progress["maximum"] = len(self.image_paths)
        self.progress["value"] = 0

        for idx, image_path in enumerate(self.image_paths):
            img = Image.open(image_path)
            available_width = 540
            available_height = 720
            scale_factor = min(available_width / img.width, available_height / img.height)
            new_width = img.width * scale_factor
            new_height = img.height * scale_factor
            x_centered = (612 - new_width) / 2
            y_centered = (792 - new_height) / 2

            pdf.setFillColorRGB(1, 1, 1)
            pdf.rect(0, 0, 612, 792, fill=1)
            pdf.drawImage(image_path, x_centered, y_centered, width=new_width, height=new_height)
            pdf.showPage()

            self.progress["value"] = idx + 1
            self.root.update_idletasks()

        pdf.save()

        tk.messagebox.showinfo("Success", f"PDF saved as {output_pdf_path}")

def main():
    root = tk.Tk()
    converter = ImageToPdfConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
