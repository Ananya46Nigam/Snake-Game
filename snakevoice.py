import pyaudio
import struct
import pyautogui  # to press a button to play the game

# below are the four wake word's path that you have generated earlier
key1 = 'go_down_windows.ppn'
key2 = 'snake_up_windows.ppn'
key3 = 'go_right_windows.ppn'
key4 = 'go_left_windows.ppn'

# this is the library path that you can fnd inside Porcupine -> lib -> system(windows or linux or mac) -> os type( 64 or 32 bit)
library_path = r'C:\Users\anany\porcupine'

# this is model file path can be find inside Porcupine -> lib -> common
model_file_path = r'C:\Users\anany\porcupine_params.pv'
keyword_file_paths = [key1, key2, key3, key4]
sensitivities = [0.5,0.5,0.5,0.5]
handle = porcupine(library_path, model_file_path, keyword_paths=[key1,key2,key3,key4],sensitivities=[0.5,0.5,0.5,0.5])

def get_next_audio_frame():
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(rate=handle.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=handle.frame_length,input_device_index=None)
    pcm = audio_stream.read(handle.frame_length)
    pcm = struct.unpack_from("h" * handle.frame_length, pcm)
    return pcm

while True:
    pcm = get_next_audio_frame()
    keyword_index = handle.process(pcm)
    if keyword_index==1:
        print(keyword_index)
        pyautogui.press('up')
    if keyword_index==3:
        print(keyword_index)
        pyautogui.press('left')
    if keyword_index==2:
        print(keyword_index)
        pyautogui.press('right')
    if keyword_index==0:
        print(keyword_index)
        pyautogui.press('down')
