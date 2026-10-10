import time
import sys

# Lista de servidores a monitorear con sus respectivas IPs y roles
SERVERS = [
    {"name": "Web Server", "ip": "192.168.91.144", "role": "NGINX"},
    {"name": "FTP Server", "ip": "192.168.91.143", "role": "vsftpd"},
    {"name": "Mail Server", "ip": "192.168.91.146", "role": "Postfix"},
    {"name": "DNS Server", "ip": "192.168.91.145", "role": "BIND9"}
]

# Umbral de conexiones simulado para detección de DoS (porcentaje o cantidad de paquetes)
DOS_THRESHOLD = 70.0 

def extract_telemetry():
    """Simula la extracción de telemetría de red y estado de los servidores"""
    print("[*] Iniciando extracción de telemetría de infraestructura...")
    metrics = []
    
    # Aquí puedes integrar llamadas RESTCONF/NETCONF hacia tus dispositivos de red o servidores
    for srv in SERVERS:
        # Simulamos una carga de tráfico aleatoria o métrica de uso de CPU/Conexiones
        import random
        cpu_usage = round(random.uniform(15.0, 85.0), 2)
        
        metrics.append({
            "name": srv["name"],
            "ip": srv["ip"],
            "role": srv["role"],
            "cpu_load": cpu_usage
        })
    return metrics

def check_dos_mitigation(metrics):
    """Evalúa si alguna métrica supera el umbral del 70% para aplicar mitigación"""
    print("\n[*] Evaluando umbrales de seguridad y mitigación DoS...")
    for m in metrics:
        print(f" -> Verificando {m['name']} ({m['ip']}) | Carga actual: {m['cpu_load']}%")
        if m['cpu_load'] > DOS_THRESHOLD:
            print(f" [!] ¡ALERTA! Posible DoS detectado en {m['name']} ({m['ip']}). Carga: {m['cpu_load']}% > Umbral: {DOS_THRESHOLD}%")
            print(f" [x] ACCIÓN DE MITIGACIÓN: Aplicando reglas de bloqueo temporal / Rate limiting para {m['ip']}...")
        else:
            print(f" [OK] Estado normal en {m['name']}.")

if __name__ == "__main__":
    print("==========================================")
    print("   MONITOR DE RED Y MITIGACIÓN DoS v1.0   ")
    print("==========================================")
    
    # Ejecución de prueba del ciclo de telemetría
    telemetry_data = extract_telemetry()
    check_dos_mitigation(telemetry_data)
    print("\n[*] Ciclo de monitoreo completado con éxito.")
