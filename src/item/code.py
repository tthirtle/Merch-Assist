# Item maintance read
def win_read(event,value):
    from FreeSimpleGUI import WIN_CLOSED
    from _global import current_item
    if event == "update":
        pass
    if event == "Cancel" or event == WIN_CLOSED:
        pass
    
    if current_item == None:
        # New Item
        pass
