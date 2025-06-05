import webbrowser

answer = input("Are you sure you wanna execute this file? (Y/N): ").strip().upper()

if answer == "Y":
    url = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
    webbrowser.open(url)
elif answer == "N":
    input("Press any button to close...")
