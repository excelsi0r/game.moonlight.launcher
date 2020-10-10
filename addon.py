import subprocess
import xbmcaddon

my_addon = xbmcaddon.Addon()
res = my_addon.getSetting('res')
fps = my_addon.getSetting('fps')
ipaddress = my_addon.getSetting('ipaddress')
bitrate = my_addon.getSetting('bitrate')

moonlight = "moonlight stream -" + res + " -fps " + fps + " -bitrate " + bitrate + "000 " + ipaddress

process = subprocess.Popen(moonlight, stdout=subprocess.PIPE)
output, error = process = process.communicate()