# Proyecto Integrador de Competencias NetDevOps

## 1. Descripción del Proyecto
Sistema distribuido de automatización y operaciones de red (NetDevOps) diseñado para integrar la extracción de información mediante modelos YANG y APIs, monitoreo continuo de telemetría de red, aprovisionamiento automatizado de infraestructura con Ansible y mitigación proactiva ante ataques de denegación de servicio (DoS).

## 2. Topología y Arquitectura del Entorno
El entorno de laboratorio simula una red corporativa distribuida compuesta por:
- **Switch Cisco IOS-XE Principal:** `172.23.18.224` (Soporte NETCONF / RESTCONF habilitado)
- **Switch Cisco IOS-XE Secundario:** `172.23.18.223` (Soporte NETCONF / RESTCONF habilitado)
- **Firewall FortiGate (FortiOS):** `172.23.18.225` (API REST e interfaz `wan1` configurada)
- **Servidores Linux (Ubuntu Server):** 
  - Servidor 1: Servicio Web (NGINX) con página personalizada.
  - Servidor 2: Servidor FTP seguro (`vsftpd`).
  - Servidor 3: Servidor de Correo (Postfix / Dovecot).
  - Servidor 4: DNS Empresarial (`BIND9`) para resolución de nombres centralizada.

## 3. Requisitos Previos e Instalación
Para configurar el entorno de ejecución en la estación de automatización, asegúrate de tener Python 3 y pip instalados, luego instala las dependencias de red y automatización:
## 4. Manual de Usuario y Ejecución
1. **Monitoreo y Telemetría:** Ejecuta el script principal para iniciar el dashboard interactivo y la supervisión de enlaces:
2. **Mitigación Automática de DoS:** El script evalúa en tiempo real si el tráfico de las interfaces supera el umbral del 70% de ocupación, ejecutando un apagado defensivo (`shutdown`) automático de la interfaz afectada y registrando la estampa de tiempo (`timestamp`) en los logs del sistema.
3. **Aprovisionamiento con Ansible:** Despliega y configura los servicios de los servidores Linux utilizando los playbooks estructurados ubicados en la carpeta `ansible/`.

## 5. Metodología GitOps y Colaboración
El desarrollo del proyecto se estructuró bajo el flujo de trabajo de ramas (*Feature Branch Workflow*), asegurando revisiones de código (*Code Reviews*) e historial de commits controlados antes de la integración a la rama principal `main`.
