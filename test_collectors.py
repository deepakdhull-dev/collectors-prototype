from collectors.ram import RamCollector
from collectors.disk import DiskCollector
from collectors.cpu import CPUCollector
from collectors.load import LoadCollector
import time

#RAM
ram=RamCollector()
ram_data=ram.collect_safe()
assert "total_mem" in ram_data, f"Missing key:total_mem, got keys:{ram_data.keys()}"
assert "used_mem" in ram_data, f"Missing key:total_mem, got keys:{ram_data.keys()}"
assert "ava_mem" in ram_data, f"Missing key:total_mem, got keys:{ram_data.keys()}"
assert "percent_mem" in ram_data, f"Missing key:total_mem, got keys:{ram_data.keys()}"
assert ram_data["total_mem"]>0, f"total memory should be positive, got {ram_data['total_mb']}"
assert 0<=ram_data['percent_mem']<=100, f"used percentage out of range:{ram_data['percent_mem']}"
assert ram_data['used_mem']+ram_data['ava_mem']==ram_data['total_mem'], f"used memory + available memory should equal toal: {ram_data['used_mem']}+{ram_data['ava_mem']}!={ram_data['total_mem']}"
print(f"RAM : ok - {ram_data['used_mem']}/{ram_data['total_mem']} MB   total {ram_data['percent_mem']} %")


#Load
load=LoadCollector()
load_data=load.collect_safe()
assert "load_1m" in load_data
assert "load_5m" in load_data
assert "load_15m" in load_data
print(f"Load : OK - {load_data['load_1m']} (1m), {load_data['load_5m']} (5m), {load_data['load_15m']} (15m)")

#Disk
disk=DiskCollector()
disk_data=disk.collect_safe()
assert disk_data["total_disk_gb"] > 0
assert 0 <= disk_data["disk_percent_used_gb"] <= 100
assert disk_data["path"] == "/"
print(f"Disk: OK — {disk_data['used_disk_gb']} GB / {disk_data['total_disk_gb']} GB ({disk_data['disk_percent_used_gb']}%)")

#CPU
cpu=CPUCollector()
cpu_data=cpu.collect_safe()
assert cpu_data==0.0, f"first call must return None(no delta yet), got : {cpu_data}"
time.sleep(1)
cpu_data = cpu.collect_safe()
assert cpu_data is not None, "Second call must return a value"
assert 0 <= cpu_data <= 100, f"CPU percent must be 0-100, got: {cpu_data}"
print(f"CPU:  OK — {cpu_data}%")
