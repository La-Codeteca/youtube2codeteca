from datetime import date

def generate_name(extension = '.txt'):
    fecha = date.today()
    FILE_NAME = f"{fecha}.{extension}"
    return FILE_NAME