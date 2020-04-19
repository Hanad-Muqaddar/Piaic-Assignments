# # def foo():
# #     try:
# #         return 1
# #     finally:
# #          return 2
# # # foo()
# # print(foo())
#
# import numpy as np
# x = np.arange(-5.0, 5.0, 0.1)
# print(x)

# def a():
#     x =3
# a()
# print(x)

# from PyQt5 import QtWidgets, uic
# import sys
# app = QtWidgets.QApplication([])
#
# win = uic.loadUi("C:\Users\syedh\Desktop\py.ui")  # specify the location of your .ui file
#
# win.show()
#
# sys.exit(app.exec())
import numpy as np
arr = np.ones((10,10))
print(arr)
arr.dtype
arr1 = np.empty((2,3,2))
print(arr1)
print(arr1.dtype)
print(arr1.shape)
print(arr.shape)
