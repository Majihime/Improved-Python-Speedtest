# Imports using sp for simplicity
import speedtest as sp
print("Testing connection speeds, please wait warmly.")
# Fetches the optimal server for the user
server = sp.Speedtest()
server.get_best_server()
# Calculates download and upload speed in megabytes & gigabytes
print("Calculating download speed...")
downloadspeed0 = server.download()
downloadspeed1 = downloadspeed0 / 1000000
downloadspeed2 = downloadspeed0 / 1000000000
print("Calculating upload speed...")
uploadspeed0 = server.upload()
uploadspeed1 = uploadspeed0 / 1000000
uploadspeed2 = uploadspeed0 / 1000000000
# Displays download and upload speeds in megabytes & gigabytes
print(f"Download speed = {downloadspeed1:.6g} Mbps / {downloadspeed2:.4g} Gbps")
print(f"Upload speed = {uploadspeed1:.6g} Mbps / {uploadspeed2:.4g} Gbps")
# Displays the user's ping from the selected server
pingresults = server.results.ping
print(f"Ping = {pingresults:.4g} miliseconds")