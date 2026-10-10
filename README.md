# 🚀 Proyecto Integrador de Competencias: NetDevOps

Sistema distribuido para la automatización de redes, extracción de telemetría mediante modelos YANG/APIs, orquestación de servidores Linux y mitigación automatizada de ataques de denegación de servicio (DoS).

---

## 📋 Tabla de Contenidos
1. [Descripción del Proyecto](#-descripción-del-proyecto)
2. [Topología e Infraestructura](#-topología-e-infraestructura)
3. [Requerimientos Técnicos Implementados](#-requerimientos-técnicos-implementados)
4. [Instalación y Ejecución](#-instalación-y-ejecución)
5. [Estructura del Repositorio](#-estructura-del-repositorio)

---

## 🎯 Descripción del Proyecto
Este proyecto integra desarrollo en Python, administración de sistemas Linux mediante Ansible y control de infraestructura de red (Cisco IOS-XE y FortiGate). El sistema monitorea de forma continua el ancho de banda y aplica políticas de mitigación defensiva automática (`administrative down`) al superar el umbral del 70% de tráfico ante posibles ataques DoS.

---

## 🌐 Topología e Infraestructura
* **Switch Cisco IOS-XE (NETCONF/RESTCONF):** `172.23.18.224` / `172.23.18.223`
* **Firewall FortiGate (API REST):** `172.23.18.225` (Interfaz `wan1`)
* **Servidor Web (NGINX):** `192.168.91.144`
* **Servidor FTP (vsftpd):** `192.168.91.143`
* **Servidor Mail (Postfix):** `192.168.91.146`
* **Servidor DNS (BIND9):** `192.168.91.145`

---

## ⚙️ Requerimientos Técnicos Implementados
1. **Extracción de Modelos YANG y APIs:** Extracción automatizada de estado operativo y métricas de red.
2. **Monitoreo de Telemetría:** Cálculo de ocupación de banda en tiempo real.
3. **Orquestación con Ansible:** Despliegue automatizado de los 4 servicios de red esenciales.
4. **Mitigación DoS (Umbral 70%):** Apagado automático de interfaces ante saturación de tráfico.
5. **Recuperación (No Shutdown):** Función interactiva para restablecer enlaces con estampa de tiempo y registros de auditoría (*logs*).
6. **Interfaz Interactiva (CLI Avanzada con Rich):** Panel visual en consola para supervisión y administración.
7. **GitOps y Control de Versiones:** Historial estructurado y buenas prácticas de desarrollo colaborativo.

---

## ⚙️ Instalación y Ejecución

1. Clonar el repositorio y acceder a la carpeta:
   ```bash
   cd ~/proyecto-netdevops
