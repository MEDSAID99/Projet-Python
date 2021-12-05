#Vérification de l'état des machines
import subprocess
import os

print("Donner l'état des adresses IP:\n")
with open(os.devnull, "wb") as limbo:
        for n in range(50, 55):
                ip="192.168.1.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print (ip, ": inactive")
                else:
                        print (ip, ": active")
