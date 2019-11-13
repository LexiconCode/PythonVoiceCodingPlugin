import os
import subprocess
import json

from yapsy.IPlugin import IPlugin


def python_voice_coding_plugin_aenea_send_sublime(c,data):
    x =  json.dumps(data).replace('"','\\"')
    y = "subl --command \"" + c + "  " + x + "\""
    subprocess.call(y, shell = True)
    subprocess.call("subl", shell = True)

class PythonVoiceCodingPluginAenea(IPlugin):
	"""docstring for PythonVoiceCodingPluginAena"""
	def register_rpcs(self,server):
		server.register_function(python_voice_coding_plugin_aenea_send_sublime)
		








