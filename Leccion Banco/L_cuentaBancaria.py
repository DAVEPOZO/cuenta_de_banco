
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import random

# Lista de cuentas
cuentas = []
historial_transacciones = []

# Función para generar un número de cuenta
def generar_numero_cuenta():
    return random.randint(100000, 999999)

# Función para registrar una nueva cuenta
def registrar_cuenta():
    def guardar_cuenta():
        cedula = entrada_cedula.get()
        nombre = entrada_nombre.get()
        contrasena = entrada_contrasena.get()
        saldo = entrada_saldo.get()
        tipo_cuenta = combo_tipo.get()
        genero = genero_var.get()

        if not (cedula and nombre and contrasena and saldo and tipo_cuenta):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if not saldo.isdigit() or int(saldo) < 0:
            messagebox.showerror("Error", "El saldo debe ser un número positivo")
            return

        numero_cuenta = generar_numero_cuenta()
        cuentas.append({
            "cedula": cedula,
            "nombre": nombre,
            "contrasena": contrasena,
            "saldo": int(saldo),
            "tipo_cuenta": tipo_cuenta,
            "genero": genero,
            "numero_cuenta": numero_cuenta
        })

        messagebox.showinfo("Éxito", f"Cuenta registrada correctamente. Número de cuenta: {numero_cuenta}")
        ventana_registro.destroy()

    ventana_registro = tk.Toplevel(ventana_principal)
    ventana_registro.title("Registrar Cuenta")

    tk.Label(ventana_registro, text="Número de cédula:").grid(row=0, column=0, padx=10, pady=5)
    entrada_cedula = tk.Entry(ventana_registro)
    entrada_cedula.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
    entrada_nombre = tk.Entry(ventana_registro)
    entrada_nombre.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Contraseña:").grid(row=2, column=0, padx=10, pady=5)
    entrada_contrasena = tk.Entry(ventana_registro, show="*")
    entrada_contrasena.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Saldo inicial:").grid(row=3, column=0, padx=10, pady=5)
    entrada_saldo = tk.Entry(ventana_registro)
    entrada_saldo.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Tipo de cuenta:").grid(row=4, column=0, padx=10, pady=5)
    combo_tipo = ttk.Combobox(ventana_registro, values=["Ahorro", "Corriente"], state="readonly")
    combo_tipo.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(ventana_registro, text="Género:").grid(row=5, column=0, padx=10, pady=5)

    # Variables para almacenar las imágenes
    hombre_img = Image.open("imagenes\\avatar_masculino.png")  # Ruta de la imagen de Hombre
    mujer_img = Image.open("imagenes\\avatar_femenino.png")  # Ruta de la imagen de Mujer
    hombre_img = hombre_img.resize((50, 50))  # Ajuste de tamaño
    mujer_img = mujer_img.resize((50, 50))  # Ajuste de tamaño
    hombre_tk = ImageTk.PhotoImage(hombre_img)
    mujer_tk = ImageTk.PhotoImage(mujer_img)

    # Etiquetas para mostrar las imágenes de "Hombre" y "Mujer"
    imagen_hombre = tk.Label(ventana_registro, image=hombre_tk)
    imagen_hombre.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    imagen_mujer = tk.Label(ventana_registro, image=mujer_tk)
    imagen_mujer.grid(row=6, column=1, columnspan=2, padx=100, pady=5)

    # Radiobutton para seleccionar el género
    genero_var = tk.StringVar(value="Hombre")
    tk.Radiobutton(ventana_registro, text="Hombre", variable=genero_var, value="Hombre").grid(row=5, column=1, sticky="w")
    tk.Radiobutton(ventana_registro, text="Mujer", variable=genero_var, value="Mujer").grid(row=5, column=1,columnspan=2)

    tk.Button(ventana_registro, text="Registrar", command=guardar_cuenta).grid(row=7, column=0, columnspan=2, pady=10)

# Función para iniciar sesión
def iniciar_sesion():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()

    for cuenta in cuentas:
        if cuenta["cedula"] == usuario and cuenta["contrasena"] == contrasena:
            mostrar_dashboard(cuenta)  # Llama a la función para mostrar el dashboard
            return

    messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para mostrar el dashboard después de iniciar sesión
def mostrar_dashboard(cuenta):
    ventana_dashboard = tk.Toplevel(ventana_principal)
    ventana_dashboard.title(f"Dashboard de {cuenta['nombre']}")
    
    # Botón para consultar saldo
    def consultar_saldo():
        messagebox.showinfo("Saldo", f"Tu saldo actual es: ${cuenta['saldo']}")

    # Mostrar avatar
    avatar_img = Image.open("imagenes\\avatar_masculino.png" if cuenta["genero"] == "Hombre" else "imagenes\\avatar_femenino.png")
    avatar_img = avatar_img.resize((100, 100))  # Ajuste de tamaño
    avatar_tk = ImageTk.PhotoImage(avatar_img)
    tk.Label(ventana_dashboard, image=avatar_tk).grid(row=0, column=0, padx=20, pady=20)

    # Mostrar información
    tk.Label(ventana_dashboard, text=f"Nombre: {cuenta['nombre']}").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(ventana_dashboard, text=f"Cédula: {cuenta['cedula']}").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(ventana_dashboard, text=f"Saldo: $ ?").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(ventana_dashboard, text=f"Tipo de cuenta: {cuenta['tipo_cuenta']}").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(ventana_dashboard, text=f"N° Cuenta: {cuenta['numero_cuenta']}").grid(row=5, column=0, padx=10, pady=5)
    
    # Botones de acción
    tk.Button(ventana_dashboard, text="Consultar saldo", command=consultar_saldo).grid(row=6, column=0, padx=10, pady=5)
    # Mantener la referencia de la imagen
    ventana_dashboard.avatar_tk = avatar_tk
    
        # Botón para depositar dinero
    def depositar_dinero():
        def realizar_deposito():
            monto = deposito_entry.get()
            if not monto.isdigit() or int(monto) <= 0:
                messagebox.showerror("Error", "Monto inválido")
                return
            cuenta['saldo'] += int(monto)
            messagebox.showinfo("Éxito", f"Depósito realizado. Nuevo saldo: ${cuenta['saldo']}")
            deposito_ventana.destroy()

        deposito_ventana = tk.Toplevel(ventana_dashboard)
        deposito_ventana.title("Depositar Dinero")
        
        tk.Label(deposito_ventana, text="Monto a depositar:").grid(row=0, column=0, padx=10, pady=5)
        deposito_entry = tk.Entry(deposito_ventana)
        deposito_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(deposito_ventana, text="Depositar", command=realizar_deposito).grid(row=1, column=0, columnspan=2, pady=10)

    # Botones de acción
    def logout():
        ventana_dashboard.destroy()  # Cierra la ventana del dashboard
        ventana_principal.deiconify() 
    
    
    
    # Retirar dinero
    def retirar_dinero():
        def realizar_retiro():
            monto = retiro_entry.get()
            if not monto.isdigit() or int(monto) <= 0:
                messagebox.showerror("Error", "Monto inválido")
                return
            if cuenta['saldo'] >= int(monto):
                cuenta['saldo'] -= int(monto)
                messagebox.showinfo("Éxito", f"Retiro realizado. Nuevo saldo: ${cuenta['saldo']}")
                historial_transacciones.append(f"Retiro: ${monto}")
                retiro_ventana.destroy()
            else:
                messagebox.showerror("Error", "Saldo insuficiente")

        retiro_ventana = tk.Toplevel(ventana_dashboard)
        retiro_ventana.title("Retirar Dinero")
        
        tk.Label(retiro_ventana, text="Monto a retirar:").grid(row=0, column=0, padx=10, pady=5)
        retiro_entry = tk.Entry(retiro_ventana)
        retiro_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(retiro_ventana, text="Retirar", command=realizar_retiro).grid(row=1, column=0, columnspan=2, pady=10)
    
    # Transferencia entre cuentas
    def transferencia():
        def realizar_transferencia():
            monto = transferencia_entry.get()
            numero_cuenta_destino = transferencia_cuenta_entry.get()

            if not monto.isdigit() or int(monto) <= 0:
                messagebox.showerror("Error", "Monto inválido")
                return
            
            if cuenta['saldo'] < int(monto):
                messagebox.showerror("Error", "Saldo insuficiente")
                return
            
            # Buscar la cuenta destino
            cuenta_destino = next((c for c in cuentas if c['numero_cuenta'] == int(numero_cuenta_destino)), None)
            if cuenta_destino is None:
                messagebox.showerror("Error", "Cuenta destino no encontrada")
                return

            # Realizar la transferencia
            cuenta['saldo'] -= int(monto)
            cuenta_destino['saldo'] += int(monto)
            historial_transacciones.append(f"Transferencia de ${monto} a cuenta {numero_cuenta_destino}")
            
            messagebox.showinfo("Éxito", f"Transferencia realizada. Nuevo saldo: ${cuenta['saldo']}")
            transferencia_ventana.destroy()

        transferencia_ventana = tk.Toplevel(ventana_dashboard)
        transferencia_ventana.title("Transferir Dinero")
        
        tk.Label(transferencia_ventana, text="Monto a transferir:").grid(row=0, column=0, padx=10, pady=5)
        transferencia_entry = tk.Entry(transferencia_ventana)
        transferencia_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(transferencia_ventana, text="Número de cuenta destino:").grid(row=1, column=0, padx=10, pady=5)
        transferencia_cuenta_entry = tk.Entry(transferencia_ventana)
        transferencia_cuenta_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(transferencia_ventana, text="Transferir", command=realizar_transferencia).grid(row=2, column=0, columnspan=2, pady=10)

    # Historial de transacciones
    def mostrar_historial():
        historial_ventana = tk.Toplevel(ventana_dashboard)
        historial_ventana.title("Historial de Transacciones")

        if not historial_transacciones:
            tk.Label(historial_ventana, text="No hay transacciones registradas.").grid(row=0, column=0, padx=10, pady=10)
        else:
            for idx, transaccion in enumerate(historial_transacciones):
                tk.Label(historial_ventana, text=transaccion).grid(row=idx, column=0, padx=10, pady=5)

        tk.Button(historial_ventana, text="Cerrar", command=historial_ventana.destroy).grid(row=len(historial_transacciones)+1, column=0, pady=10)

    # Botones para acciones
    tk.Button(ventana_dashboard, text="Depositar dinero", command=depositar_dinero).grid(row=7, column=0, padx=10, pady=10)
    tk.Button(ventana_dashboard, text="Retirar dinero", command=retirar_dinero).grid(row=8, column=0, padx=10, pady=5)
    tk.Button(ventana_dashboard, text="Transferir dinero", command=transferencia).grid(row=9, column=0, padx=10, pady=5)
    tk.Button(ventana_dashboard, text="Historial de transacciones", command=mostrar_historial).grid(row=10, column=0, padx=10, pady=5)
    tk.Button(ventana_dashboard, text="Cerrar sesión", command=logout).grid(row=11, column=0, padx=10, pady=20)

# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Sistema Bancario")

# Widgets de la ventana principal
tk.Label(ventana_principal, text="Usuario (Cédula):").grid(row=0, column=0, padx=10, pady=5)
entrada_usuario = tk.Entry(ventana_principal)
entrada_usuario.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana_principal, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
entrada_contrasena = tk.Entry(ventana_principal, show="*")
entrada_contrasena.grid(row=1, column=1, padx=10, pady=5)

tk.Button(ventana_principal, text="Iniciar Sesión", command=iniciar_sesion).grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(ventana_principal, text="Registrar", command=registrar_cuenta).grid(row=3, column=0, columnspan=2, pady=10)

ventana_principal.mainloop()