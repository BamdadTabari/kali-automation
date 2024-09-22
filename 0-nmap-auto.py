import subprocess
import os

def get_ip_address():
    # Prompt the user to enter an IP address
    ip = input("Please enter an IP address: ")
    return ip

def run_nmap(ip):
    # Construct the command to run Nmap
    nmap_command = f"nmap -sV {ip}"
    
    try:
        # Run the Nmap command using subprocess
        result = subprocess.run(nmap_command, shell=True, check=True, capture_output=True)
        
        # Get the exit status of the process
        exit_status = result.returncode
        
        if exit_status == 0:
            # If successful, save the output to a file
            filename = f"{ip}_scan.txt"
            with open(filename, "w") as file:
                # Write the output to the file
                a = result.stdout
                file.write(result.stdout.decode('utf-8'))
            
            print(f"Nmap scan completed successfully. Results saved to {filename}")
        else:
            print("Nmap scan failed.")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during Nmap execution: {e}")

def main():
    ip = get_ip_address()
    run_nmap(ip)

if __name__ == "__main__":
    main()
