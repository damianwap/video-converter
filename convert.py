import os
import subprocess

def convert_ts_to_mp4(input_file, output_file):
    """Mengonversi file .ts menjadi .mp4 menggunakan ffmpeg"""
    try:
        command = [
            "ffmpeg", "-i", input_file,
            "-c:v", "copy", "-c:a", "aac", "-strict", "experimental",
            output_file
        ]
        
        subprocess.run(command, check=True)
        print(f"Konversi berhasil: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    print("Contoh format nama folder: C:/Users/NamaPengguna/Videos atau /home/user/videos")
    input_directory = input("Masukkan lokasi folder sumber: ")
    output_directory = input("Masukkan lokasi folder hasil: ")
    input_ts = input("Masukkan nama file (contoh: video.mp4): ")
    format_hasil = input("Masukkan format tujuan (contoh: mp4, ts, avi): ")

    
    input_path = os.path.join(input_directory, input_ts)
    output_mp4 = os.path.join(output_directory, os.path.splitext(input_ts)[0] + "." + format_hasil)
    
    convert_ts_to_mp4(input_path, output_mp4)
