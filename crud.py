from PyQt5 import QtWidgets, uic 
from PyQt5.QtWidgets import *
import sys
import conexion

def validarCampos():
    if ventana.txtNombre.text()=="" or ventana.txtCorreo.text()=="" :
        alerta=QMessageBox()
        alerta.setText('Debes llenar los campos')
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()
        return True

def agregar():
    if validarCampos():
        return False
    print("Hola, soy la acción de agregar")
    nombre= ventana.txtNombre.text()
    correo= ventana.txtCorreo.text()
    print(nombre,correo)

    objContactos=conexion.contactos()
    contactos=objContactos.crearContacto((nombre,correo))
    consultar()

def eliminar():
    print("Hola, soy la acción de agregar")
    id= ventana.txtID.text()
    objContactos=conexion.contactos()
    contactos=objContactos.borrarContacto(id)
    consultar()
    
def modificar():
    if validarCampos():
        return False
    print("Hola, soy la acción de modificar")
    id= ventana.txtID.text()
    nombre= ventana.txtNombre.text()
    correo= ventana.txtCorreo.text()
    print(nombre,correo)

    objContactos=conexion.contactos()
    contactos=objContactos.modificarContacto((nombre,correo,id))
    consultar()

def cancelar():
    print("Hola, soy la acción de agregar")
    consultar()
    
def consultar():
    ventana.tblContactos.setRowCount(0)
    indiceControl=0
   
    objContactos=conexion.contactos()
    contactos=objContactos.leerContactos()
    for contacto in contactos:
        ventana.tblContactos.setRowCount(indiceControl+1)
        ventana.tblContactos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        indiceControl+=1

    ventana.txtID.setText("")
    ventana.txtCorreo.setText("")
    ventana.txtNombre.setText("")

    ventana.btnAgregar.setEnabled(True)
    ventana.btnModificar.setEnabled(False)
    ventana.btnEliminar.setEnabled(False)
    ventana.btnCancelar.setEnabled(False)

def seleccionar():
    id=ventana.tblContactos.selectedIndexes()[0].data()
    nombre=ventana.tblContactos.selectedIndexes()[1].data()
    correo=ventana.tblContactos.selectedIndexes()[2].data()
    print(id,nombre,correo)
    ventana.txtID.setText(id)
    ventana.txtNombre.setText(nombre)
    ventana.txtCorreo.setText(correo)

    ventana.btnAgregar.setEnabled(False)
    ventana.btnModificar.setEnabled(True)
    ventana.btnEliminar.setEnabled(True)
    ventana.btnCancelar.setEnabled(True)

aplicacion = QtWidgets.QApplication([])
ventana = uic.loadUi("ventana.ui")
ventana.show()
consultar()
ventana.tblContactos.setHorizontalHeaderLabels(['ID','Nombre','Correo'])
ventana.tblContactos.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tblContactos.setSelectionBehavior(QTableWidget.SelectRows)

ventana.tblContactos.cellClicked.connect(seleccionar)

ventana.btnAgregar.clicked.connect(agregar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())