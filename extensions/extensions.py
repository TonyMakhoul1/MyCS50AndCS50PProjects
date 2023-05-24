message = input("File name: ")
if ".jpg" in message:
    print("image/jpeg")
elif ".jpeg" in message:
    print("image/jpeg")
elif ".png" in message:
    print("image/png")
elif ".gif" in message:
    print("image/gif")
elif ".pdf" in message:
    print("application/pdf")
elif ".txt" in message:
    print("text/plain")
elif ".zip" in message:
    print("application.zip")
elif ".PDF" in message:
    print("application/pdf")
else:
    print("application/octet-stream")

