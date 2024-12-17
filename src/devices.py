# devices.py

from typing import List, Tuple
from pyaudio import PyAudio

class AudioDevices:
  
    @classmethod
    def list_audio_devices(
        cls, pyaudio: PyAudio
    ) -> Tuple[List[Tuple[int, str]], List[Tuple[int, str]]]:
        
        # Get host API info and number of devices
        info = pyaudio.get_host_api_info_by_index(0)
        n_devices = info.get("deviceCount")

        input_devices = []
        output_devices = []

        # Iterate through all devices and classify them as input or output devices
        for i in range(n_devices):
            device = pyaudio.get_device_info_by_host_api_device_index(0, i)
            if device.get("maxInputChannels") > 0:
                input_devices.append(
                    (i, device.get("name"), int(device.get("defaultSampleRate")))
                )
            if device.get("maxOutputChannels") > 0:
                output_devices.append((i, device.get("name"), device))
                
        return input_devices, output_devices

    @classmethod
    def choose_device(cls, devices, device_type="input"):
        
        if not devices:
            print(f"No {device_type} devices found.")
            return None

        # Display available devices
        print(f"Available {device_type} devices:")
        for _, (device_index, name, sample_rate) in enumerate(devices):
            print(f"{device_index}: {name}")

        # Prompt the user to select a device by index
        while True:
            try:
                choice = int(input(f"Select {device_type} device by index: "))
                if choice in [d[0] for d in devices]:
                    if device_type == "input":
                        return choice, sample_rate
                    else:
                        return choice
                else:
                    print(
                        f"Invalid selection. Please choose a valid {device_type} device index."
                    )
            except ValueError:
                print("Please enter a numerical index.")
