empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}
def empleados_con_salario_mayor(empleados, salario_minimo):
    empleados_filtrados = {}

    for id_empleado, datos_empleado in empleados.items():
        nombre, edad, salario = datos_empleado
        if salario > salario_minimo:
            empleados_filtrados[id_empleado] = datos_empleado
    return empleados_filtrados
resultado = empleados_con_salario_mayor(empleados, 2800)
print(resultado)