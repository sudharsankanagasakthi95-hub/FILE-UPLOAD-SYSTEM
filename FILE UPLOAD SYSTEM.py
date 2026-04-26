import os
import shutil

folder = "files"
os.makedirs(folder, exist_ok=True)

while True:
    print("\n--- File Upload & Download System ---")
    print("1. Upload File")
    print("2. View Files")
    print("3. Download File")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        source = input("Enter file path to upload: ")

        if os.path.exists(source):
            filename = os.path.basename(source)
            destination = os.path.join(folder, filename)
            shutil.copy(source, destination)
            print("File Uploaded Successfully!")
        else:
            print("File not found!")

    elif choice == "2":
        files = os.listdir(folder)

        if files:
            print("\nUploaded Files:")
            for file in files:
                print(file)
        else:
            print("No files available.")

    elif choice == "3":
        filename = input("Enter file name to download: ")
        source = os.path.join(folder, filename)

        if os.path.exists(source):
            destination = input("Enter destination path: ")
            shutil.copy(source, destination)
            print("File Downloaded Successfully!")
        else:
            print("File not found!")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")