while True:
    st = input("enter the something \n")
    c1 = ''
    c2 = ''
    c3 = ''
    for i in st:
        if(i.isdigit()):
            # print(i)
            c1=str(c1)+str(i)
            # print("this is digit = ",c1)
        elif (c1 is not c3) and i==" ":
            c2 = c1
            c1 = ''
    if "add" in st.lower() or "plus" in st.lower() or "sum" in st.lower() or "+" in st.lower() or "addition" in st.lower():
        try:
            print("total addition = ",int(c2)+int(c1))
        except ValueError:
            print("please a space starting and ending tha digits.....Like anythig 12 anything 22")

    elif "multiply" in st.lower() or "multiplication" in st.lower() or "*" in st.lower() or "mul" in st.lower():
        try:
            print("total addition = ", int(c2) * int(c1))
        except ValueError:
            print("please a space starting and ending tha digits.....Like anythig 12 anything 22")

    elif "divide" in st.lower() or "division" in st.lower() or "/" in st.lower() or "div" in st.lower():
        try:
            print("total addition = ", int(c2) / int(c1))
        except ValueError:
            print("please a space starting and ending tha digits.....Like anythig 12 anything 22")

    elif "subtract" in st.lower() or "subtraction" in st.lower() or "-" in st.lower() or "min" in st.lower():
        try:
            print("total addition = ", int(c2) - int(c1))
        except ValueError:
            print("please a space starting and ending tha digits.....Like anythig 12 anything 22")
    else:
        print("please enter mathematical word or symbols for any operation")

# import pyqrcode
# from pyqrcode import QRCode
# qr=pyqrcode.create("facebook.com")
# qr.png("my3.png",scale=20)
