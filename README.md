# Recipe Menu
This project aims for better understanding for Python-Tkinter, Pillow and requests module<br>

## Installation and Setup
One is reqired to install certain Python modules for the programme to execute properly.<br>
The same can be done by the following block of codes/
```bash
  import subprocess
  import sys
  def import_or_install(module_name):
      try:
          __import__(module_name)
          pass
      except ImportError:
          print(f"The module '{module_name}' is not installed. Installing now...")
          subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
          pr int(f"'{module_name}' has been installed successfully.")
  import_or_install('tkinter')
```
The modules to be installed are: -
* tkinter
* mysql.connector
* requests
* Pillow

## Setting Up Database
The program first check whether the database is created in the system or not. If not, then it starts creating the database
```bash
conn = sql.connect(host='localhost', user='root', password='family123')
cr = conn.cursor()
cr.execute("SHOW DATABASES LIKE 'projectworksans'")
result = cr.fetchone()
if not result:
    cr.execute("create database projectworksans")
    cr.execute("use projectworksans")
...
```
## Importing images from browser
The images are imported using requests module
```bash
 if image_url:
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                image_data = response.content
                img = Image.open(io.BytesIO(image_data))
                photo = ImageTk.PhotoImage(img)
                image_label = tk.Label(rframe, image=photo)
                image_label.image = photo  # Keep a reference to avoid garbage collection
                image_label.pack()
                image_label.pack(side=tk.RIGHT, anchor='ne')
                image_label.pack(side=tk.TOP, anchor='ne')
            except requests.exceptions.RequestException as e:
                print(f"Error fetching image: {e}")
```

## Loading Image URL

Retrieve the image URL using Pillow, io and requests module
1. Pillow (PIL) module is used for image processing. It opens, loads and saves the images
2. The io module enables working with data streams held in memory, such as StringIO for text data and BytesIO for binary data.
3. requests modules allow sending different types of HTTP requests, such as GET, POST, PUT, DELETE, PATCH, and HEAD, which are essential for interacting with web servers and APIs.

## Future Expectations
* Enabling Adding and Removing options for more recipes and cuisines

## Import points to Remember
* This project requires a good internet connection as it retrieves the image's URL from Google.com.
* This project may take time to load and display the image and information.
* If any changes are made in the database, ensure that the previous version of your database is removed from your laptop.

## Find a bug?
If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above.
