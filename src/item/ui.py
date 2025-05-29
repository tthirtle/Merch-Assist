# Item Maintance Window
import FreeSimpleGUI as sg

brands = ["Auto"]

status = [
    "Active",
    "Inactive",
    "Discontinued",
    "Replaced"
]

img_file_types = (
    ("All image File types","*.jpg *.jpeg *.bmp *.png *.gif"),
    ("Jpeg file","*.jpg *.jpeg"),
    ("Bitmap file","*.bmp"),
    ("PNG file","*.png"),
    sg.FILE_TYPES_ALL_FILES[0]
)

upc_label = sg.Text("UPC")
upc_textbox = sg.Input(key='upc')
sku_label = sg.Text("SKU")
sku_textbox = sg.Input(key="sku")
brand_label = sg.Text("Brand")
brand_combo = sg.InputCombo(values=brands,key="brand")
desc_label = sg.Text("Description")
desc_textbox = sg.Input(key='desc')
status_label = sg.Text("Status")
status_text = sg.Combo(values=status,key="status",readonly=True)
pack_label = sg.Text("Pack size")
pack_text = sg.Input(key="pack",tooltip="Number of items in a pack(1 on order)")
unit_label = sg.Text("Unit size")
unit_text = sg.Input(key='unit',tooltip="The size of the product example: 1 ea, 2 dozen, 16 capsulles, 20 fl oz")

img_label = sg.Text("Image")
img_text = sg.Input(key='img')
img_button = sg.FileBrowse(file_types=img_file_types)

update_button = sg.Button("Update",key="update")


layout = [
    [upc_label,upc_textbox],
    [sku_label,sku_textbox],
    [brand_label,brand_combo],
    [desc_label,desc_textbox],
    [status_label,status_text],
    [pack_label,pack_text],
    [unit_label,unit_text],
    [img_label,img_text,img_button],
    [update_button,sg.Cancel()]
]

window = sg.Window("Item Maintance",layout=layout)

window.read()