import docx2pdf
from PyPDF2 import PdfFileReader
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5 import uic
import pdf2docx
import os
import fitz
import pdfplumber

def get_pages(file):
    pdfFileReader = PdfFileReader(file)
    numPages = pdfFileReader.getNumPages()
    print(numPages)
    return numPages

def pdf2img(input_path, output_path, zoom_x=3, zoom_y=3, rotate_angle=0):
    files = os.listdir(input_path)
    for file in files:
        # 过滤临时文件
        if '~$' in file:
            continue
        # 过滤非pdf格式文件
        if file.split('.')[-1] != 'pdf':
            continue
        pdf_file = os.path.join(input_path, file)

        num_page = get_pages(pdf_file)
        for i in range(num_page):
            pdf = fitz.open(pdf_file)
            page = pdf[i]
            # 设置缩放和旋转系数
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate_angle)
            pix = page.get_pixmap(matrix=trans, alpha=False)
            save_roi_name = os.path.join(output_path, file[:-4] + 'page{}.png'.format(i))
            print(save_roi_name)
            pix.save(save_roi_name)
            pdf.close()
''''''
def filter_file(path, filetype):
    files = []
    for file in os.listdir(path):
        if file.endswith(filetype):
            temp_path = os.path.join(path, file)
            files.append(temp_path)
    # print(files)
    return files

# 可以试着重写用上面的filter_file()
def pdf_docx(file_dir, output_dir):
    files = os.listdir(file_dir)
    # print(files)
    for file in files:
        # 过滤临时文件
        if '~$' in file:
            continue
        # 过滤非pdf格式文件
        if file.split('.')[-1] != 'pdf':
            continue
        # print(file)
        pages = get_pages(os.path.join(file_dir, file))
        # print(pages)
        # 获取文件名称
        file_name = file.split('.')[0]
        # docx文件名称
        docx_name = file_name + '.docx'
        # 加载pdf文档
        cv = pdf2docx.Converter(os.path.join(file_dir, file))
        docx_path = os.path.join(output_dir, docx_name)
        cv.convert(docx_path, start=0, end=pages)
        # cv.convert(docx_name, pages=[0, 2, 3])
        cv.close()


class Stats:
    def __init__(self):
        self.ui = uic.loadUi("文件工具助手.ui")
        # word转pdf
        self.ui.btn1_1_1.clicked.connect(self.choose_dir_1_1)
        self.ui.btn1_1_2.clicked.connect(self.save_dir_1_1)
        self.ui.btn1_1_3.clicked.connect(self.word2pdf)
        # pdf转word
        self.ui.btn2_1_1.clicked.connect(self.choose_dir_2_1)
        self.ui.btn2_1_2.clicked.connect(self.save_dir_2_1)
        self.ui.btn2_1_3.clicked.connect(self.pdf2word)
        # pdf转img
        self.ui.btn2_2_1.clicked.connect(self.choose_dir_2_2)
        self.ui.btn2_2_2.clicked.connect(self.save_dir_2_2)
        self.ui.btn2_2_3.clicked.connect(self.start_convert_img)
        # pdf提取文字
        self.ui.btn2_3_1.clicked.connect(self.choose_dir_2_3)
        # self.ui.btn2_3_2.clicked.connect(self.save_dir_2_3)
        self.ui.btn2_3_3.clicked.connect(self.start_extract_text)


    # word转pdf--选择路径
    def choose_dir_1_1(self):
        '''可能需要开发打开文件的'''
        # self.vDir,_ = QFileDialog.getOpenFileName(None, '选择文件夹')
        # self.vDir,_ = QFileDialog.getOpenFileNames(None, '选择文件夹')
        self.vDir = QFileDialog.getExistingDirectory(None, '选择文件夹')
        self.ui.textBrowser1_1_1.clear()
        self.ui.textBrowser1_1_1.append(self.vDir)
    def save_dir_1_1(self):
        # word转pdf--保存路径
        self.vDir = QFileDialog.getExistingDirectory(None, '选择文件夹')
        self.ui.textBrowser1_1_2.clear()
        self.ui.textBrowser1_1_2.append(self.vDir)
    # pdf转word
    def choose_dir_2_1(self):
        self.vDir = QFileDialog.getExistingDirectory(None, '选择文件夹')
        self.ui.textBrowser2_1_1.clear()
        self.ui.textBrowser2_1_1.append(self.vDir)
    def save_dir_2_1(self):
        self.vDir = QFileDialog.getExistingDirectory(None, '选择文件夹')
        self.ui.textBrowser2_1_2.clear()
        self.ui.textBrowser2_1_2.append(self.vDir)
    # pdf转img
    def choose_dir_2_2(self):
        self.vDir = QFileDialog.getExistingDirectory(None, '选择文件夹')
        self.ui.textBrowser2_2_1.clear()
        self.ui.textBrowser2_2_1.append(self.vDir)
    def save_dir_2_2(self):
        self.vDir = QFileDialog.getExistingDirectory(None, '选择文件夹')
        self.ui.textBrowser2_2_2.clear()
        self.ui.textBrowser2_2_2.append(self.vDir)
    # pdf提取文字
    def choose_dir_2_3(self):
        self.vDir3, ok = QFileDialog.getOpenFileName(None, '选择文件')
        self.ui.textBrowser2_3_1.clear()
        self.ui.textBrowser2_3_1.append(self.vDir3)
    def save_dir_2_3(self):
        self.vDir = QFileDialog.getExistingDirectory(None, '选择文件夹')
        self.ui.textBrowser2_3_2.clear()
        self.ui.textBrowser2_3_2.append(self.vDir)

    '''1-1 word转pdf'''
    def word2pdf(self):
        input_dir = self.ui.textBrowser1_1_1.toPlainText()
        output_dir = self.ui.textBrowser1_1_2.toPlainText()
        self.ui.textBrowser1_1_3.setText('开始转化')
        docx2pdf.convert(input_dir, output_dir)
        self.ui.textBrowser1_1_3.append('转换成功')

    def pdf2word(self):
        input_dir = self.ui.textBrowser2_1_1.toPlainText()
        output_dir = self.ui.textBrowser2_1_2.toPlainText()
        self.ui.textBrowser2_1_3.setText('开始转化')
        pdf_docx(input_dir, output_dir)
        self.ui.textBrowser2_1_3.append('转换成功')

    def start_convert_img(self):
        input_dir = self.ui.textBrowser2_2_1.toPlainText()
        output_dir = self.ui.textBrowser2_2_2.toPlainText()
        print(input_dir)
        print(output_dir)
        self.ui.textBrowser2_2_3.setText('开始转化')
        pdf2img(input_dir, output_dir)
        self.ui.textBrowser2_2_3.append('转换成功')

    def start_extract_text(self):
        input_dir = self.ui.textBrowser2_3_1.toPlainText()
        le = self.ui.lineEdit2_3_1.text()
        pdf_pages = get_pages(input_dir)
        # self.ui.textBrowser2_3_4.setText(pdf_pages)
        pdf = pdfplumber.open(input_dir)
        # if le != "":
        if le:
            page = int(self.ui.lineEdit2_3_1.text())

            if page > pdf_pages or page < 1:
                print("页码不存在")
                self.ui.plainTextEdit2_3_1.setPlainText("页码不存在")
            else:
                one_page = pdf.pages[page - 1]
                text = one_page.extract_text()
                print(text)
                self.ui.plainTextEdit2_3_1.setPlainText(text)
        else:
            one_page = pdf.pages[0]
            text = one_page.extract_text()
            print(text)
            self.ui.plainTextEdit2_3_1.setPlainText(text)
        pdf.close()


if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()

