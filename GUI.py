import pystray
from PIL import Image as PILImage
import os
from subprocess import Popen
import sys
import app
def icon_run():
    def iconstop():
        icon.stop()
    def hi():
        sys.exit('F off')
    Image = PILImage.open(os.path.join(os.path.dirname(__file__), "icon.png"))
    icon = pystray.Icon("Kanon", Image, menu =pystray.Menu(
                pystray.MenuItem('Test', iconstop), 
                pystray.MenuItem('Show', hi)))
    icon.run_detached()





