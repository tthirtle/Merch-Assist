def loc_read(event,value:dict):
    match event[0]:
        case "table":
            table_input(event[2],value.get("desc"))

def table_input(selection,item_name:str):
    print(selection)
    if selection[0] or selection[1] == None:
        print("None")
        return
    if selection[0] or selection[1] == -1:
        print("-1")
        return
    from ui import table
    from FreeSimpleGUI import popup_get_text
    current_table = table.Values
    row = selection[0]
    col = selection[1]
    match col:
        case 0:
            entry_type = "Gondola"
        case 1:
            entry_type = "Shelf"
        case 2:
            entry_type = "Slot"
    entry_text = f"Please enter {entry_type} for {item_name}"
    entry = popup_get_text(entry_text,"Enter location info")
    current_table[row][col] = entry
    print(current_table)
    table.update(current_table)