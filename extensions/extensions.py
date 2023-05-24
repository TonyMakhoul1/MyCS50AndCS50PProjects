message = input("File name: ")
if ".jpg" or ".jpeg" in message:
    print("image/jpeg")
elif ".gif" in message:
    print("image/gif")
elif ".pdf" in message:
    print("application/pdf")
else:
    print("application/octet-stream")

