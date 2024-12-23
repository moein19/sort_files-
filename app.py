import shutil,os

class Sort_files:
    def __init__(self, s):
        self.s = s

    @property
    def sort_json(self):
        data = os.listdir(self.s)
        if "json files" in data:
            for i in data:
                if i.endswith(".json"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"json files")
                    print(f"file {i} moved to json files")
        elif "json files" not in data:
            os.mkdir(self.s+os.sep+"json files")
        try:
            for i in data:
                if i.endswith(".json"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"json files")
                    print(f"file {i} moved to json files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_python(self):
        data = os.listdir(self.s)
        if "python files" in data:
            for i in data:
                if i.endswith(".py"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"python files")
                    print(f"file {i} moved to python files")
        elif "python files" not in data:
            os.mkdir(self.s+os.sep+"python files")
        try:
            for i in data:
                if i.endswith(".py"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"python files")
                    print(f"file {i} moved to python files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_txt(self):
        data = os.listdir(self.s)
        if "txt files" in data:
            for i in data:
                if i.endswith(".txt"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"txt files")
                    print(f"file {i} moved to txt files")
        elif "txt files" not in data:
            os.mkdir(self.s+os.sep+"txt files")
        try:
            for i in data:
                if i.endswith(".txt"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"txt files")
                    print(f"file {i} moved to txt files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_pickle(self):
        data = os.listdir(self.s)
        if "pickle files" in data:
            for i in data:
                if i.endswith(".pickle"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"pickle files")
                    print(f"file {i} moved to pickle files")
        elif "pickle files" not in data:
            os.mkdir(self.s+os.sep+"pickle files")
        try:
            for i in data:
                if i.endswith(".pickle"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"pickle files")
                    print(f"file {i} moved to pickle files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_csv(self):
        data = os.listdir(self.s)
        if "csv files" in data:
            for i in data:
                if i.endswith(".csv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"csv files")
                    print(f"file {i} moved to csv files")
        elif "csv files" not in data:
            os.mkdir(self.s+os.sep+"csv files")
        try:
            for i in data:
                if i.endswith(".csv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"csv files")
                    print(f"file {i} moved to csv files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_html(self):
        data = os.listdir(self.s)
        if "html files" in data:
            for i in data:
                if i.endswith((".html",".htm")):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"html files")
                    print(f"file {i} moved to html files")
        elif "html files" not in data:
            os.mkdir(self.s+os.sep+"html files")
        try:
            for i in data:
                if i.endswith((".html",".htm")):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"html files")
                    print(f"file {i} moved to html files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_xlsx(self):
        data = os.listdir(self.s)
        if "excel files" in data:
            for i in data:
                if i.endswith((".xlsx",".xls")):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"excel files")
                    print(f"file {i} moved to excel files")
        elif "excel files" not in data:
            os.mkdir(self.s+os.sep+"excel files")
        try:
            for i in data:
                if i.endswith((".xlsx",".xls")):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"excel files")
                    print(f"file {i} moved to excel files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_docx(self):
        data = os.listdir(self.s)
        if "word files" in data:
            for i in data:
                if i.endswith(".docx"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"word files")
                    print(f"file {i} moved to word files")
        elif "word files" not in data:
            os.mkdir(self.s+os.sep+"word files")
        try:
            for i in data:
                if i.endswith(".docx"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"word files")
                    print(f"file {i} moved to word files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_pdf(self):
        data = os.listdir(self.s)
        if "pdf files" in data:
            for i in data:
                if i.endswith(".pdf"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"pdf files")
                    print(f"file {i} moved to pdf files")
        elif "pdf files" not in data:
            os.mkdir(self.s+os.sep+"pdf files")
        try:
            for i in data:
                if i.endswith(".pdf"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"pdf files")
                    print(f"file {i} moved to pdf files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_powerPoint(self):
        data = os.listdir(self.s)
        if "powerpoint files" in data:
            for i in data:
                if i.endswith(".pptx"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"powerpoint files")
                    print(f"file {i} moved to powerpoint files")
        elif "powerpoint files" not in data:
            os.mkdir(self.s+os.sep+"powerpoint files")
        try:
            for i in data:
                if i.endswith(".pptx"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"powerpoint files")
                    print(f"file {i} moved to powerpoint files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_photo(self):
        #".jfif",".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".svg", ".ico", ".heic", ".heif", ".raw"
        data = os.listdir(self.s)
        if "photo files" in data:
            for i in data:
                if i.endswith("jfif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jfif files",exist_ok=True)
                if i.endswith("jpg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jpg files",exist_ok=True)
                if i.endswith("jpeg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jpeg files",exist_ok=True)
                if i.endswith("png"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"png files",exist_ok=True)
                if i.endswith("gif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"gif files",exist_ok=True)
                if i.endswith("bmp"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"bmp files",exist_ok=True)
                if i.endswith("tiff"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"tiff files",exist_ok=True)
                if i.endswith("tif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"tif files",exist_ok=True)
                if i.endswith("webp"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"webp files",exist_ok=True)
                if i.endswith("svg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"svg files",exist_ok=True)
                if i.endswith("ico"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"ico files",exist_ok=True)
                if i.endswith("heic"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"heic files",exist_ok=True)
                if i.endswith("heif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"heif files",exist_ok=True)
                if i.endswith("raw"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"raw files",exist_ok=True)
            for i in data:
                if i.endswith("jfif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jfif files")
                if i.endswith("jpg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jpg files")
                if i.endswith("jpeg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jpeg files")
                if i.endswith("png"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"png files")
                if i.endswith("gif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"gif files")
                if i.endswith("bmp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"bmp files")
                if i.endswith("tiff"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"tiff files")
                if i.endswith("tif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"tif files")
                if i.endswith("webp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"webp files")
                if i.endswith("svg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"svg files")
                if i.endswith("ico"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"ico files")
                if i.endswith("heic"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"heic files")
                if i.endswith("heif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"heif files")
                if i.endswith("raw"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"raw files")
        elif "photo files" not in data:
            os.mkdir(self.s+os.sep+"photo files")
        try:
            for i in data:
                if i.endswith("jfif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jfif files",exist_ok=True)
                if i.endswith("jpg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jpg files",exist_ok=True)
                if i.endswith("jpeg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"jpeg files",exist_ok=True)
                if i.endswith("png"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"png files",exist_ok=True)
                if i.endswith("gif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"gif files",exist_ok=True)
                if i.endswith("bmp"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"bmp files",exist_ok=True)
                if i.endswith("tiff"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"tiff files",exist_ok=True)
                if i.endswith("tif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"tif files",exist_ok=True)
                if i.endswith("webp"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"webp files",exist_ok=True)
                if i.endswith("svg"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"svg files",exist_ok=True)
                if i.endswith("ico"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"ico files",exist_ok=True)
                if i.endswith("heic"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"heic files",exist_ok=True)
                if i.endswith("heif"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"heif files",exist_ok=True)
                if i.endswith("raw"):
                    os.makedirs(self.s+os.sep+"photo files"+os.sep+"raw files",exist_ok=True)
            for i in data:
                if i.endswith("jfif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jfif files")
                if i.endswith("jpg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jpg files")
                if i.endswith("jpeg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"jpeg files")
                if i.endswith("png"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"png files")
                if i.endswith("gif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"gif files")
                if i.endswith("bmp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"bmp files")
                if i.endswith("tiff"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"tiff files")
                if i.endswith("tif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"tif files")
                if i.endswith("webp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"webp files")
                if i.endswith("svg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"svg files")
                if i.endswith("ico"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"ico files")
                if i.endswith("heic"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"heic files")
                if i.endswith("heif"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"heif files")
                if i.endswith("raw"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"photo files"+os.sep+"raw files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_video(self):
        #".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm", ".3gp", ".m4v", ".mpg", ".mpeg", ".ogv", ".ts", ".f4v"
        data = os.listdir(self.s)
        if "video files" in data:
            for i in data:
                if i.endswith("mp4"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mp4 files",exist_ok=True)
                if i.endswith("mkv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mkv files",exist_ok=True)
                if i.endswith("mov"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mov files",exist_ok=True)
                if i.endswith("avi"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"avi files",exist_ok=True)
                if i.endswith("flv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"flv files",exist_ok=True)
                if i.endswith("wmv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"wmv files",exist_ok=True)
                if i.endswith("webm"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"webm files",exist_ok=True)
                if i.endswith("3gp"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"3gp files",exist_ok=True)
                if i.endswith("m4v"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"m4v files",exist_ok=True)
                if i.endswith("mpg"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mpg files",exist_ok=True)
                if i.endswith("mpeg"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mpeg files",exist_ok=True)
                if i.endswith("ogv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"ogv files",exist_ok=True)
                if i.endswith("ts"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"ts files",exist_ok=True)
                if i.endswith("f4v"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"f4v files",exist_ok=True)
            for i in data:
                if i.endswith("mp4"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mp4 files")
                if i.endswith("mkv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mkv files")
                if i.endswith("mov"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mov files")
                if i.endswith("avi"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"avi files")
                if i.endswith("flv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"flv files")
                if i.endswith("wmv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"wmv files")
                if i.endswith("webm"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"webm files")
                if i.endswith("3gp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"3gp files")
                if i.endswith("m4v"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"m4v files")
                if i.endswith("mpg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mpg files")
                if i.endswith("mpeg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mpeg files")
                if i.endswith("ovg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"ovg files")
                if i.endswith("ts"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"ts files")
                if i.endswith("f4v"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"f4v files")
        elif "video files" not in data:
            os.mkdir(self.s+os.sep+"video files")
        try:
            for i in data:
                if i.endswith("mp4"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mp4 files",exist_ok=True)
                if i.endswith("mkv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mkv files",exist_ok=True)
                if i.endswith("mov"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mov files",exist_ok=True)
                if i.endswith("avi"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"avi files",exist_ok=True)
                if i.endswith("flv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"flv files",exist_ok=True)
                if i.endswith("wmv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"wmv files",exist_ok=True)
                if i.endswith("webm"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"webm files",exist_ok=True)
                if i.endswith("3gp"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"3gp files",exist_ok=True)
                if i.endswith("m4v"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"m4v files",exist_ok=True)
                if i.endswith("mpg"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mpg files",exist_ok=True)
                if i.endswith("mpeg"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"mpeg files",exist_ok=True)
                if i.endswith("ogv"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"ogv files",exist_ok=True)
                if i.endswith("ts"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"ts files",exist_ok=True)
                if i.endswith("f4v"):
                    os.makedirs(self.s+os.sep+"video files"+os.sep+"f4v files",exist_ok=True)
            for i in data:
                if i.endswith("mp4"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mp4 files")
                if i.endswith("mkv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mkv files")
                if i.endswith("mov"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mov files")
                if i.endswith("avi"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"avi files")
                if i.endswith("flv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"flv files")
                if i.endswith("wmv"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"wmv files")
                if i.endswith("webm"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"webm files")
                if i.endswith("3gp"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"3gp files")
                if i.endswith("m4v"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"m4v files")
                if i.endswith("mpg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mpg files")
                if i.endswith("mpeg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"mpeg files")
                if i.endswith("ovg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"ovg files")
                if i.endswith("ts"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"ts files")
                if i.endswith("f4v"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"video files"+os.sep+"f4v files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_music(self):
        #".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".alac", ".aiff", ".amr", ".opus"
        data = os.listdir(self.s)
        if "music files" in data:
            for i in data:
                if i.endswith("mp3"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"mp3 files",exist_ok=True)
                if i.endswith("wav"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"wav files",exist_ok=True)
                if i.endswith("aac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"aac files",exist_ok=True)
                if i.endswith("flac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"flac files",exist_ok=True)
                if i.endswith("ogg"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"ogg files",exist_ok=True)
                if i.endswith("wma"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"wma files",exist_ok=True)
                if i.endswith("m4a"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"m4a files",exist_ok=True)
                if i.endswith("alac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"alac files",exist_ok=True)
                if i.endswith("aiff"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"aiff files",exist_ok=True)
                if i.endswith("amr"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"amr files",exist_ok=True)
                if i.endswith("opus"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"opus files",exist_ok=True)
            for i in data:
                if i.endswith("mp3"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"mp3 files")
                if i.endswith("wav"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"wav files")
                if i.endswith("aac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"aac files")
                if i.endswith("flac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"flac files")
                if i.endswith("ogg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"ogg files")
                if i.endswith("wma"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"wma files")
                if i.endswith("m4a"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"m4a files")
                if i.endswith("alac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"alac files")
                if i.endswith("aiff"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"aiff files")
                if i.endswith("amr"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"amr files")
                if i.endswith("opus"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"opus files")
        elif "music files" not in data:
            os.mkdir(self.s+os.sep+"music files")
        try:

            for i in data:
                if i.endswith("mp3"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"mp3 files",exist_ok=True)
                if i.endswith("wav"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"wav files",exist_ok=True)
                if i.endswith("aac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"aac files",exist_ok=True)
                if i.endswith("flac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"flac files",exist_ok=True)
                if i.endswith("ogg"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"ogg files",exist_ok=True)
                if i.endswith("wma"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"wma files",exist_ok=True)
                if i.endswith("m4a"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"m4a files",exist_ok=True)
                if i.endswith("alac"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"alac files",exist_ok=True)
                if i.endswith("aiff"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"aiff files",exist_ok=True)
                if i.endswith("amr"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"amr files",exist_ok=True)
                if i.endswith("opus"):
                    os.makedirs(self.s+os.sep+"music files"+os.sep+"opus files",exist_ok=True)
            for i in data:
                if i.endswith("mp3"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"mp3 files")
                if i.endswith("wav"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"wav files")
                if i.endswith("aac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"aac files")
                if i.endswith("flac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"flac files")
                if i.endswith("ogg"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"ogg files")
                if i.endswith("wma"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"wma files")
                if i.endswith("m4a"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"m4a files")
                if i.endswith("alac"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"alac files")
                if i.endswith("aiff"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"aiff files")
                if i.endswith("amr"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"amr files")
                if i.endswith("opus"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"music files"+os.sep+"opus files")

        except:
            print("operation wasn`t ok")

    @property
    def sort_exe(self):
        data = os.listdir(self.s)
        if "exe files" in data:
            for i in data:
                if i.endswith(".exe"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"exe files")
                    print(f"file {i} moved to exe files")
        elif "exe files" not in data:
            os.mkdir(self.s+os.sep+"exe files")
        try:
            for i in data:
                if i.endswith(".exe"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"exe files")
                    print(f"file {i} moved to exe files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_rar(self):
        data = os.listdir(self.s)
        if "rar files" in data:
            for i in data:
                if i.endswith(".rar"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"rar files")
                    print(f"file {i} moved to rar files")
        elif "rar files" not in data:
            os.mkdir(self.s+os.sep+"rar files")
        try:
            for i in data:
                if i.endswith(".rar"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"rar files")
                    print(f"file {i} moved to rar files")
        except:
            print("operation wasn`t ok")


    @property
    def sort_apk(self):
        data = os.listdir(self.s)
        if "apk files" in data:
            for i in data:
                if i.endswith(".apk"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"apk files")
                    print(f"file {i} moved to apk files")
        elif "apk files" not in data:
            os.mkdir(self.s+os.sep+"apk files")
        try:
            for i in data:
                if i.endswith(".apk"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"apk files")
                    print(f"file {i} moved to apk files")
        except:
            print("operation wasn`t ok")
    @property
    def sort_zip(self):
        data = os.listdir(self.s)
        if "zip files" in data:
            for i in data:
                if i.endswith(".zip"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"zip files")
                    print(f"file {i} moved to zip files")
        elif "zip files" not in data:
            os.mkdir(self.s+os.sep+"zip files")
        try:
            for i in data:
                if i.endswith(".zip"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"zip files")
                    print(f"file {i} moved to zip files")
        except:
            print("operation wasn`t ok")

    @property
    def sort_access(self):
        data = os.listdir(self.s)
        if "access files" in data:
            for i in data:
                if i.endswith(".accdb"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"access files")
                    print(f"file {i} moved to access files")
        elif "access files" not in data:
            os.mkdir(self.s+os.sep+"access files")
        try:
            for i in data:
                if i.endswith(".accdb"):
                    shutil.move(self.s+os.sep+i,self.s+os.sep+"access files")
                    print(f"file {i} moved to access files")
        except:
            print("operation wasn`t ok")

