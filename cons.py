import os
class cons:
    def __init__(self):
        self.render = None
        self.file_error = "Hata yok"
    def add(self, code):
        self.file_error = False
        self.render = self.render + "\n" + code
    def add_file(self, file):
        try:
            with open(file, "r") as file:
                lines = file.read()
                self.render = self.render = lines
        except FileNotFoundError:
            self.file_error = True
            print(f"{file} dosyası {os.getcwd()} konumunda bulunamdı")
    def run(self):
        if self.file_error is True:
            raise FileNotFoundError("Dosya bulunamdı")
        else:
            pass
        if self.render is None:
            print("Lütfen bir kod ekleyin")
            pass
        else:
            exec(self.render)            
