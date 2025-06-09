import webbrowser
import time

confirm = input("Are you sure you want to execute this script? (yes/no): ").strip().lower()
if confirm == 'yes':
    while True:
        url = "https://www.youtube.com/watch?v=IxX_QHay02M"  # Change the url here
        webbrowser.open(url)
        time.sleep(3)  # I won't recomend to remove this line because it will start opening the url very fast, only remove it if you are testing in your machine or if you got permission and the person that gave you permission knows what this script does, this script won't come with any type of warranty for any damage!!!
else:
    print("Execution cancelled.")
