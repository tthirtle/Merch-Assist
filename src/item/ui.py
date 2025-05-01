import FreeSimpleGUI as sg

# Hard coded varibles - Testing only

statuses = [
    "Active",
    "Inactive",
    "Discontinued",
    "Replaced"
]

brands = ["Auto"]

img_file_types = (
    ("Windows Bitmap (*.bmp)","*.bmp"),
    ("Joint Photographic Experts Group Image (*.jpg)","*.jpg"),
    ("Graphics Interchange Format (*.gif)","*.gif"),
    ("Portable Network Graphics (*.png)","*.png"),
    sg.FILE_TYPES_ALL_FILES[0]
)

# UI
# Global Item Maintance Window

# Needed Fields
# UPC,SKU,Description,Status

upc_label = sg.Text("UPC")
upc_textbox = sg.Input(key="upc")
sku_label = sg.Text("SKU")
sku_textbox = sg.Input(key="sku")
brand_label = sg.Text("Brand")
brand_combo = sg.Combo(brands,brands[0],key='brand')
descrip_label = sg.Text("Description")
descrip_textbox = sg.Input(key="descr")
image_label = sg.Text("Image")
image_textbox = sg.Input(key="img")
image_button = sg.FileBrowse(file_types=img_file_types)

maint_layout = [
    [upc_label,upc_textbox],
    [sku_label,sku_textbox],
    [brand_label,brand_combo],
    [descrip_label,descrip_textbox],
    [image_label,image_textbox,image_button],
    [sg.Ok(),sg.Cancel()]
]

maint_window = sg.Window(title="Item Maintance",layout=maint_layout)

# Location Window

sku_loc_label = sg.Text("SKU")
sku_loc_textbox = sg.Input(disabled=True)
upc_loc_label = sg.Text("UPC")
upc_loc_textbox = sg.Input(disabled=True)
desc_loc_label = sg.Text("Description")
desc_loc_textbox = sg.Input(disabled=True,key="desc")

table = sg.Table(values=
                 [
                      ['','',''],
                      ['','',''],
                      ['','',''],
                      ['','',''],
                      ['','','']
     ],headings=["Gondola","Shelf","Slot"],select_mode=sg.TABLE_SELECT_MODE_EXTENDED,enable_click_events=True,key="table")

loc_layout = [
    [upc_loc_label,upc_loc_textbox],
    [sku_loc_label,sku_loc_textbox],
    [desc_loc_label,desc_loc_textbox],
    [table]
]

loc_window = sg.Window("Location Select",loc_layout)


# TEST CODE
loc_window.finalize()
desc_loc_textbox.update("Sample")
from code_o import loc_read
while True:
     (event, value) = loc_window.read()
     if event  == sg.WIN_CLOSED:
          break
     print(event)
     print(value)
     loc_read(event,value)