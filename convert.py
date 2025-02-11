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
        hapus_file = input("Apakah Anda ingin menghapus file " + input_file + "? (y/n) ")
        if hapus_file.lower() == "y":
            os.remove(input_file)
            print(f"File dihapus: {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan: {e}")

def get_filenames(folder_path=None):
    if folder_path is None:
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # folder_path = os.path.join(script_dir, "source")
        folder_path = os.path.join(os.getcwd(), "source") 
    try:
        return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        # return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    except FileNotFoundError:
        print(f"Folder '{folder_path}' tidak ditemukan.")
        return []
    except PermissionError:
        print(f"Tidak memiliki izin untuk mengakses folder '{folder_path}'.")
        return []


if __name__ == "__main__":
    
    result_folder = os.path.join(os.getcwd(), "result")
    source_folder = os.path.join(os.getcwd(), "source")
    list_file = get_filenames()
    if len(list_file) > 0:
        for file_name in list_file:
            print(file_name)
            print("ini " + os.path.splitext(file_name)[0])
            format_hasil = input("Masukkan format tujuan (contoh: mp4, ts, avi): ")
            output_mp4 = os.path.join(result_folder, os.path.splitext(file_name)[0] + "." + format_hasil)
            print(output_mp4)
            convert_ts_to_mp4(os.path.join(source_folder,file_name), output_mp4)
    else:
        print("Tidak ada file di folder " + source_folder)
