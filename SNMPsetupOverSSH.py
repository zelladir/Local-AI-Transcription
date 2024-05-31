import paramiko
import sys

def setup_snmp(host, ssh_user, ssh_password, snmp_user, snmp_password):
    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=ssh_user, password=ssh_password)

        # Commands to install and configure SNMP
        commands = [
            "sudo apt update",
            "sudo apt install snmpd -y",
            f"echo 'createUser {snmp_user} SHA \"{snmp_password}\" AES' | sudo tee -a /var/lib/snmp/snmpd.conf",
            "sudo systemctl restart snmpd"
        ]

        # Execute commands
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
            stdin.write(ssh_password + "\n")  # Provide sudo password
            stdin.flush()
            exit_status = stdout.channel.recv_exit_status()  # Block until command is executed
            if exit_status == 0:
                print(f"Executed command '{command}' on {host} successfully.")
            else:
                print(f"Error in executing command '{command}' on {host}", file=sys.stderr)

        # Close SSH connection
        ssh.close()

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

# Example usage
hosts = ["10.0.0.34"]  # List of VM IPs
ssh_user = "mmadmin"
ssh_password = "4thelulz!"
snmp_user = "asquared"
snmp_password = "N0rmandy!"

for host in hosts:
    setup_snmp(host, ssh_user, ssh_password, snmp_user, snmp_password)
