class file:
    def __init__(self,files):
          self.files=files
    def search(self):
     try: 
        with open(self.files,'r') as a:
            content=a.read()
            print(content)
     except FileNotFoundError:
            print("error:file not found")
file1=file(r'C:/Users/hari prasad e/Documents/softronics/assingments/hari.txt')
file1.search()


