import subprocess

def configure_apache():
	#creation fichier de configuration
	subprocess.run(["echo", "<Configuration Apache>", "|", "tee", "/etc/apache2/sites-available/000-default.conf"])

def restart_apache():
	subprocess.run(["sudo", "systemctl", "restart", "apache2"])
 # pour restart un service on utilise systemctl

if __name__ == "__main__":
	configure_apache()
	restart_apache()


