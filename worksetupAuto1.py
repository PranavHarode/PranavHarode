import webbrowser as wb

def workauto():
    Chrome_path= 'C:\Users\prana\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe %s'
    URLs=("youtube.com","gmail.com","google.map/maps","github.com/PranavHarode/PROJECTS-PY")


    for url in URLs:
        wb.get(Chrome_path).open(url)

workauto()

