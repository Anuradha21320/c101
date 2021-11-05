import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token="sl.A7aMTvUWCiFPgNEOMupf2GC0yEpO9e1dV5tPSUQ60hJKF5S3Sho6dLwCSrM5aiYupuudWCdwvYooBN4nKsKzfGyP5oYek2fVrDTeW6oE_Q2cyghEsxJ21TBDzUA5MnMAdOECNqk"
    TransferData1=TransferData(access_token)
    file_from=input("enter the file path to transfer ")
    file_to=input("enter the full path to the dropbox ")
    TransferData1.upload_file(file_from, file_to)
    print("file has been moved")

main()
      