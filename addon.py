import subprocess
import xbmcaddon

my_addon = xbmcaddon.Addon()
res = my_addon.getSetting('res')
fps = my_addon.getSetting('fps')
ip = my_addon.getSetting('ip')
app = my_addon.getSetting('app')

moonlight = "moonlight stream -" + res + " -fps " + fps + " -app " + app + " " + ip

process = subprocess.Popen(moonlight, stdout=subprocess.PIPE)
output, error = process = process.communicate()