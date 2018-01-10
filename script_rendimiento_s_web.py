#-*- coding: utf-8 -*-

import os
import time
import commands

# Configuración
CONN =[1,10,25,50,75,100,200,500,1000]
TITULO="modulo"
DURATION="10"
IP="localhost"
URLS=["index.html","image.jpg","contenido.zip"]
SERVERS=["apache2"]

##############################################################################################################
resultados=[]
for con in CONN:
        time.sleep(2)
        for server in SERVERS:
                print "Reiniciando %s..." % server
                os.system("systemctl restart %s" % server)
        lcon=[]
        print("Conexiones concurrentes %d"%con)
        for url in URLS:
                print("URL: http://%s/%s"%(IP,url))
                res=commands.getoutput('ab -t %s -k -c %s http://%s/%s | grep "Requests per second:"|awk \'{print $4}\''%(DURATION,con,IP,url))
                try:
                        lcon.append(float(res.split("\n")[-1]))
                        print res.split("\n")[-1]+" #/seg"
                except:
                        pass
        resultados.append(lcon)
        
cad=TITULO+"\t"
for lista in resultados:
        cad+='"'+str(sum(lista)/len(lista)).replace(".",",")+'"\t'
print cad[:-1]
