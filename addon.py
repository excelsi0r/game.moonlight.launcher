import subprocess
import xbmcaddon

my_addon = xbmcaddon.Addon()
# res = my_addon.getSetting('res')
# fps = my_addon.getSetting('fps')
# ip = my_addon.getSetting('ip')
# bitrate = my_addon.getSetting('bitrate')

# moonlight = "moonlight stream -" + res + " -fps " + fps + " -bitrate " + bitrate + "000 " + ip

moonlight = "steamlink"

process = subprocess.Popen(moonlight, stdout=subprocess.PIPE)
output, error = process = process.communicate()