def main():
    e = input("File name: ")
    e = e.split(".")
    b = len(e)
    match e[b - 1]:
        case "gif":
            print ("image/gif")
        case "png":
            print ("image/png")
        case "jpg" | "jpeg":
            print ("image/jpeg")
        case "pdf":
            print ("application/pdf")
        case "txt":
            print ("text/plan")
        case "zip":
            print ("application/zip")
        case _:
            print ("application/octet-stream")
main()