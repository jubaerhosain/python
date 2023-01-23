try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        print("closed")
        f.close()
except:
  print("Something went wrong when opening the file")

else:
    print("else block if no error in try")
