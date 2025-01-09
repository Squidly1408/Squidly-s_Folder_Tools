import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from pathlib import Path
import yt_dlp
import threading


class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Title
        title_label = tk.Label(
            root, text="YouTube Downloader", font=("Helvetica", 18, "bold"), fg="blue"
        )
        title_label.pack(pady=10)

        # URL Input
        self.url_frame = tk.Frame(root)
        self.url_frame.pack(pady=5)
        self.url_label = tk.Label(
            self.url_frame, text="YouTube URL:", font=("Helvetica", 12)
        )
        self.url_label.grid(row=0, column=0, sticky="w")
        self.url_var = tk.StringVar()
        self.url_entry = tk.Entry(
            self.url_frame, textvariable=self.url_var, width=50, font=("Helvetica", 10)
        )
        self.url_entry.grid(row=0, column=1, padx=5)

        # Download Type
        self.type_frame = tk.Frame(root)
        self.type_frame.pack(pady=10)
        self.type_label = tk.Label(
            self.type_frame, text="Download Type:", font=("Helvetica", 12)
        )
        self.type_label.grid(row=0, column=0, sticky="w")
        self.download_type = tk.StringVar(value="video")
        self.video_radio = tk.Radiobutton(
            self.type_frame,
            text="Video",
            variable=self.download_type,
            value="video",
            font=("Helvetica", 10),
        )
        self.audio_radio = tk.Radiobutton(
            self.type_frame,
            text="Audio",
            variable=self.download_type,
            value="audio",
            font=("Helvetica", 10),
        )
        self.video_radio.grid(row=0, column=1)
        self.audio_radio.grid(row=0, column=2)

        # Format Selection
        self.format_frame = tk.Frame(root)
        self.format_frame.pack(pady=5)
        self.format_label = tk.Label(
            self.format_frame, text="Select Format:", font=("Helvetica", 12)
        )
        self.format_label.grid(row=0, column=0, sticky="w")
        self.format_var = tk.StringVar(value="mp4")
        self.format_dropdown = ttk.Combobox(
            self.format_frame,
            textvariable=self.format_var,
            values=["mp4", "webm", "mkv", "mp3", "m4a"],
            font=("Helvetica", 10),
            state="readonly",
        )
        self.format_dropdown.grid(row=0, column=1, padx=5)

        # Choose Folder
        self.folder_frame = tk.Frame(root)
        self.folder_frame.pack(pady=10)
        self.folder_label = tk.Label(
            self.folder_frame, text="Save to Folder:", font=("Helvetica", 12)
        )
        self.folder_label.grid(row=0, column=0, sticky="w")
        self.folder_var = tk.StringVar()
        self.folder_entry = tk.Entry(
            self.folder_frame,
            textvariable=self.folder_var,
            width=40,
            font=("Helvetica", 10),
        )
        self.folder_entry.grid(row=0, column=1, padx=5)
        self.browse_button = tk.Button(
            self.folder_frame,
            text="Browse",
            command=self.select_folder,
            font=("Helvetica", 10),
            bg="lightgray",
        )
        self.browse_button.grid(row=0, column=2, padx=5)

        # Progress Bar
        self.progress_label = tk.Label(
            root, text="Download Progress:", font=("Helvetica", 12)
        )
        self.progress_label.pack(pady=5)
        self.progress = ttk.Progressbar(
            root, orient=tk.HORIZONTAL, length=400, mode="determinate"
        )
        self.progress.pack(pady=5)

        # Download Button
        self.download_button = tk.Button(
            root,
            text="Download",
            command=self.start_download_thread,
            font=("Helvetica", 14),
            bg="lightblue",
        )
        self.download_button.pack(pady=20)

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_var.set(folder_selected)

    def start_download_thread(self):
        download_thread = threading.Thread(target=self.start_download)
        download_thread.start()

    def start_download(self):
        url = self.url_var.get().strip()
        download_type = self.download_type.get()
        selected_format = self.format_var.get()
        download_folder = self.folder_var.get().strip()

        if not url:
            messagebox.showerror("Error", "Please enter a valid YouTube URL!")
            return
        if not download_folder:
            messagebox.showerror("Error", "Please select a download folder!")
            return

        # Set up yt-dlp options
        ydl_opts = {
            "format": "bestaudio/best" if download_type == "audio" else "best",
            "outtmpl": str(Path(download_folder) / f"%(title)s.%(ext)s"),
            "progress_hooks": [self.update_progress],
        }

        # Add post-processing for audio-only downloads
        if download_type == "audio":
            ydl_opts["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": selected_format,
                    "preferredquality": "192",
                }
            ]

        self.progress["value"] = 0
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Success", "Download completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download: {e}")

    def update_progress(self, d):
        if d["status"] == "downloading":
            downloaded = d.get("downloaded_bytes", 0)
            total = d.get("total_bytes", 1)
            percent = (downloaded / total) * 100
            self.progress["value"] = percent
            self.root.update_idletasks()
        elif d["status"] == "finished":
            self.progress["value"] = 100
            self.root.update_idletasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
