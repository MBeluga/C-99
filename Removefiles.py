import shutil, time
path = "Randomfiles"
days = 10
seconds = time.time() - (days*24*60*60)
def remove_file(path):
    if not shutil.rmtree(path):
        print (path + "is removed succesfully!")
    else:
        print ("Unable to delete " + path)