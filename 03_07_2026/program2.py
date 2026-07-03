try:
    fb = open(r"C:\Users\Akash\Desktop\Core-Classes\Python-9am\03_07_2026\student.txt","r")
    print(fb.readline())
except FileNotFoundError as e:
    print(e)