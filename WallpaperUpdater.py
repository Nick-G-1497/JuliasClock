## 
#  @package WallpaperUpdater
#  A library for updating your wallpaper via python


import os 
import dbus
import argparse



##
# Class used to update your wallpaper
# @note currently only works with gnome
class WallpaperUpdater:

      def __init__ (self):
            pass

      def set_wallpaper(self, filepath):
            # parser = argparse.ArgumentParser(description='KDE Wallpaper setter')
            # parser.add_argument('file', help='Wallpaper file name')
            # parser.add_argument('--plugin', '-p', help='Wallpaper plugin (default is org.kde.image)', default='org.kde.image')
            # args = parser.parse_args()
            self._kde_set_wallpaper(filepath)
      
      ## 
      # Set your wallpaper to whatever photo is given via the path
      def _kde_set_wallpaper(self, filepath, plugin='org.kde.image'):
            # file = "file:///" + absolute_path 
            # os.system("gsettings set org.gnome.desktop.background picture-uri " + file)
            
            jscript = """
            var allDesktops = desktops();
            print (allDesktops);
            for (i=0;i<allDesktops.length;i++) {
                  d = allDesktops[i];
                  d.wallpaperPlugin = "%s";
                  d.currentConfigGroup = Array("Wallpaper", "%s", "General");
                  d.writeConfig("Image", "file://%s")
            }
            """
            bus = dbus.SessionBus()
            plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
            plasma.evaluateScript(jscript % (plugin, plugin, filepath))
            


if __name__ == '__main__':
      pass