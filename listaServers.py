with open ("lista_servers.txt", "r") as lServer:
	for line in lServer:
		server = line
		server2 = line



		#print ("%s%s" %(server,server2))
		a = ("<protocol>RDP</protocol>\n<port>3389</port>\n<serverName>%s</serverName>\n<url>rdp://%s:3389/</url>\n<name>NT-DCSSA02</name>\n<credential>ADM.Gustavoas</credential>\n<domainName>mercurio</domainName>\n<userName>adm.gustavoas</userName>\n<password>w@x8i3nbk</password>\n<notes />\n<desktopSize>AutoScale</desktopSize>\n<desktopSizeHeight>600</desktopSizeHeight>\n<desktopSizeWidth>800</desktopSizeWidth>\n<colors>Bit16</colors>\n<sounds>DontPlay</sounds>\n<redirectClipboard>True</redirectClipboard>\n<enableTLSAuthentication>True</enableTLSAuthentication>\n<enableNLAAuthentication>True</enableNLAAuthentication>\n<idleTimeout>240</idleTimeout>\n<overallTimeout>600</overallTimeout>\n<connectionTimeout>600</connectionTimeout>\n<shutdownTimeout>10</shutdownTimeout>\n<tags />\n<newWindow>False</newWindow>\n<toolBarIcon />\n<bitmapPeristence>RDP</bitmapPeristence>\n</favorite>" %(server,server2))
		print (a)

		with open ("return.txt", "a") as  returnFile:
			returnFile.write(a)
		