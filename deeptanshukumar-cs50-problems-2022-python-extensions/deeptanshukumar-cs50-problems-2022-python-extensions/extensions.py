def main():
    extension = input("File name: ").lower().strip().split(".")[-1]
    match extension:
        case "pdf"|"zip":
            media_type(f"application/{extension}")
        case "txt":
            media_type("text/plain")
        case "png" |"gif":
            media_type(f"image/{extension}")
        case "jpg" |"jpeg":
            media_type(f"image/jpeg")
        case _:
            media_type("application/octet-stream")

def media_type(media_extension):
    print(media_extension)


main()
