from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
import numpy as np

Window.size = (432, 960)
Window.clearcolor = (0.51, 0.69, 0.71, 1)


matrix = []
matrix_second=[]
matr = []
matr_second=[]

class MatrixApp(App):
    def on_enter_second(self,value):
        print(value.text)
        matrix_second.append(value.text)
        print(matrix_second)
        for a in matrix_second:
            if a =='':
                matr_second.clear()
        if len(matrix_second) == self.val:
            matr_second.append([a for a in matrix_second])
            matrix_second.clear()
            print(matr_second)

    def oper(self):
        if self.vali=="det":
            matrixx = np.array(matr, dtype=np.float32)
            print(matrixx)
            det = np.linalg.det(matrixx)
            lbdet=Label(text='[size=30][color=000000]det=%s[/color][/size]'%(det),markup=True)
            self.als.add_widget(lbdet)
            matr.clear()
            matr_second.clear()
        if self.vali=='T':
            matrixx = np.array(matr, dtype=np.float32)
            print(matrixx)
            trans=np.transpose(matrixx)
            lbdet = Label(text='[size=30][color=000000]T=\n%s[/color][/size]' % (trans),markup=True)
            self.als.add_widget(lbdet)
            matr.clear()
            matr_second.clear()
        if self.vali=='A-¹':
            matrixx = np.array(matr, dtype=np.float32)
            print(matrixx)
            if np.linalg.det(matrixx)==0:
                lbdet = Label(text='        [size=30][color=000000]Определитель равен нулю!(матрица вырожденная)[/color][/size]',halign= 'center',markup=True)
            if np.linalg.det(matrixx)!=0:
                revers = np.linalg.inv(matrixx)
                lbdet = Label(text='[size=30][color=000000]A-¹=\n%s[/color][/size]' % (revers),markup=True)
            self.als.add_widget(lbdet)
            matr.clear()
            matr_second.clear()
        if self.vali=='+':
            matrixx = np.array(matr, dtype=np.float32)
            matrixx_second = np.array(matr_second, dtype=np.float32)
            answer=matrixx+matrixx_second
            lbdet = Label(text='[size=30][color=000000]C=\n%s[/color][/size]' % (answer),markup=True)
            self.als.add_widget(lbdet)
            matr.clear()
            matr_second.clear()
        if self.vali == '-':
            matrixx = np.array(matr, dtype=np.float32)
            matrixx_second = np.array(matr_second, dtype=np.float32)
            answer = matrixx - matrixx_second
            lbdet = Label(text='[size=30][color=000000]C=\n%s[/color][/size]' % (answer),markup=True)
            self.als.add_widget(lbdet)
            matr.clear()
            matr_second.clear()
        if self.vali == 'X':
            matrixx = np.array(matr, dtype=np.float32)
            matrixx_second = np.array(matr_second, dtype=np.float32)
            answer = matrixx * matrixx_second
            lbdet = Label(text='[size=30][color=000000]C=\n%s[/color][/size]' % (answer),markup=True)
            self.als.add_widget(lbdet)
            matr.clear()
            matr_second.clear()
        if self.vali == '÷':
            matrixx = np.array(matr, dtype=np.float32)
            matrixx_second = np.array(matr_second, dtype=np.float32)
            answer = matrixx / matrixx_second
            lbdet = Label(text='[size=30][color=000000]C=\n%s[/color][/size]' % (answer),markup=True)
            self.als.add_widget(lbdet)
            matr.clear()
            matr_second.clear()

    def btn_pressed_operation(self, value):
        self.als.clear_widgets()
        self.vali = str(value.text)
        self.oper()


    def on_enter(self, value):
        print(value.text)
        matrix.append(value.text)
        print(matrix)
        for a in matrix:
            if a=="":
                matrix.clear()
        if len(matrix) == self.val:
            matr.append([a for a in matrix])
            matrix.clear()
            print(matr)

    def change_lb(self):
        self.gl1.clear_widgets()
        self.gls.clear_widgets()
        self.gl1.cols = self.val
        self.gl1.rows = self.val
        self.gls.cols = self.val
        self.gls.rows = self.val
        for i in range((self.val) ** 2):
            ti = TextInput(multiline=False)
            ti.bind(on_text_validate=self.on_enter)
            self.gl1.add_widget(ti)
        for i in range((self.val) ** 2):
            ti = TextInput(multiline=False)
            ti.bind(on_text_validate=self.on_enter_second)
            self.gls.add_widget(ti)

    def btn_pressed(self, value):
        matrix.clear()
        matrix_second.clear()
        matr.clear()
        matr_second.clear()
        self.val = 0
        self.val += int(value.text)
        self.change_lb()

    def build(self):

        self.BOX = BoxLayout(orientation='vertical',padding=20)
        bl1 = BoxLayout(size_hint=[0.9, 0.1],pos_hint={'right':0.95,},spacing=5)

        self.gl1 = GridLayout(cols=0, rows=0,padding=20,spacing=5,size_hint=[0.9, 0.6],pos_hint={'right':0.95,})
        bl2 = BoxLayout(size_hint=[0.9, 0.1],pos_hint={'right':0.95,},spacing=5 )

        self.bls = BoxLayout(orientation="vertical",padding=20)
        self.gls=GridLayout(cols=0, rows=0,padding=20,spacing=5,size_hint=[1,1 ])
        self.als=AnchorLayout(size_hint=[0.9, 0.6])

        btn1 = Button(text='2',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn1.bind(on_press=self.btn_pressed)
        bl1.add_widget(btn1)
        btn2 = Button(text='3',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn2.bind(on_press=self.btn_pressed)
        bl1.add_widget(btn2)
        btn3 = Button(text='4',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn3.bind(on_press=self.btn_pressed)
        bl1.add_widget(btn3)
        btn4 = Button(text='5',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn4.bind(on_press=self.btn_pressed)
        bl1.add_widget(btn4)
        btn5 = Button(text='6',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn5.bind(on_press=self.btn_pressed)
        bl1.add_widget(btn5)

        btn6 = Button(text='det',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn6.bind(on_press=self.btn_pressed_operation)
        bl2.add_widget(btn6)
        btn6 = Button(text='T',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn6.bind(on_press=self.btn_pressed_operation)
        bl2.add_widget(btn6)
        btn6 = Button(text='A-¹',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn6.bind(on_press=self.btn_pressed_operation)
        bl2.add_widget(btn6)
        btn6 = Button(text='+',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn6.bind(on_press=self.btn_pressed_operation)
        bl2.add_widget(btn6)
        btn7 = Button(text='-',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn7.bind(on_press=self.btn_pressed_operation)
        bl2.add_widget(btn7)
        btn8 = Button(text='X',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn8.bind(on_press=self.btn_pressed_operation)
        bl2.add_widget(btn8)
        btn9 = Button(text='÷',background_color=[0.18, 0.20, 0.20, 1],background_normal="")
        btn9.bind(on_press=self.btn_pressed_operation)
        bl2.add_widget(btn9)


        self.BOX.add_widget(bl1)
        self.BOX.add_widget(self.gl1)
        self.BOX.add_widget(bl2)
        self.bls.add_widget(self.gls)
        self.bls.add_widget(self.als)
        self.BOX.add_widget(self.bls)
        return self.BOX


if __name__ == '__main__':
    app = MatrixApp()
    app.run()