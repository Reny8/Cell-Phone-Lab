from cell_phone import Cell_Phone
cell = Cell_Phone("Samsung")
for contact in cell.contacts:
    print(cell.contacts)
cell.message("Tay: Call me when you get the change")
cell.message("2678794333: It is Bryan. Got a new phone number. Save my number")
cell.send_a_text("Tay")
cell.vibrate()
print(cell.phone_on_vibrate)