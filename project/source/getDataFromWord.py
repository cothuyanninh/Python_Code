try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile
import os , cv2, sys, shutil


"""
Module that extract text from MS XML Word document (.docx).
(Inspired by python-docx <https://github.com/mikemaccana/python-docx>)
"""

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'


def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)

    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text
                 for node in paragraph.getiterator(TEXT)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))

    return '\n\n'.join(paragraphs)


def get_picture_form_word(path):

    z = zipfile.ZipFile(path)
# z = zipfile.ZipFile("../data/input/word/congphuong.docx")

#print all files in zip archive
    all_files = z.namelist()

    listPicture =[]
#get all files in word/media/ directory
    for i in range(len(all_files)):
        if all_files[i].endswith('.png'):
            listPicture.append(all_files[i])


#open an image and save it
    if len(listPicture) == 0:
        return 0
    else:
        for i in range(len(listPicture)):
            namefile = listPicture[i]
            image = z.open(namefile).read()
            f = open('../data/temp/'+ namefile.split('word/media/')[1], 'wb')
            f.write(image)
            f.close()


def check_Face_in_picture(_path):
    get_picture_form_word(_path)
    faceCascade = cv2.CascadeClassifier('../lib/haarcascade_frontalface_default.xml')
    filePicture = '../data/temp/'
    listPictureinfilePicture = os.listdir(filePicture)
    for i in range(len(listPictureinfilePicture)):
        if listPictureinfilePicture[i].endswith('.png'):
            image = cv2.imread('../data/temp/'+listPictureinfilePicture[i])
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
            grayImage,
            scaleFactor  = 1.1,
            minNeighbors = 5,
            )
            if len(faces) == 0 :
                os.unlink('../data/temp/'+listPictureinfilePicture[i])
            if len(faces) == 1:
                os.rename(filePicture+listPictureinfilePicture[i], filePicture+'/'+ os.path.basename(_path)[:-5]+'.jpg')
            # print(os.path.basename(_path)[:-5])
            # shutil.move('../data/temp/'+listPictureinfilePicture[i], os.path.basename(_path)[:-5])





    # image = cv2.imread("images/2.jpg")
    # grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # faces = faceCascade.detectMultiScale(
    # grayImage,
    # scaleFactor  = 1.1,
    # minNeighbors = 5,
    # )
    # print("Tim duoc {0} mat!".format(len(faces)))
    # print(str(faces))
    # if len(faces) != 0 :
    #     minh = open('dbFace.txt', 'r')
    #     listdb = minh.readlines()
    #     if len(listdb) != 0:
    #         for i in range(len(listdb)):
    #             if str(faces) == listdb[i].split('\n')[0]:
    #                 print("Da co trong DB va ten la:")
    #                 print(name)
    #             else :
    #                 print("Chua co trong DB")
    #                 minh.close()
    #                 minh2= open('dbFace.txt', 'a')
    #                 minh2.write(str(faces))
    #                 minh2.write('\n')
    #                 minh2.close()
                
    #     else :
    #         minh1 = open('dbFace.txt', 'a')
    #         print("chua co trong DB")
    #         minh1.write(str(faces))
    #         minh1.write('\n')
    #         minh1.close()

# get_picture_form_word("../data/input/word/congphuong.docx")

#print(get_docx_text('C:\\Users\\vanquangcz\\Desktop\\python\\project\\data\\input\\3.docx'))