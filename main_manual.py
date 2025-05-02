from manual_organizer import organize_folder

if __name__ == "__main__":
    folder_to_organize = input("Enter the folder path to manually organize: ")
    organize_folder(folder_to_organize)
    print("✅ Done organizing manually!")
