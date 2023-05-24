message = input("File name: ")
'''
if ".jpg" or ".jpeg" in message:
    print("image/jpeg")
elif ".gif" in message:
    print("image/gif")
elif ".pdf" in message:
    print("application/pdf")
else:
    print("application/octet-stream")
'''
match name:
    case ".jpeg":
        print("image/jpeg")
    case ".jpg":
        print("image/jpeg")
    case ".gif":
        print("image/gif")
    case ".pdf":
        print("application/pdf")
    case _:
        print("application/octet-stream")
