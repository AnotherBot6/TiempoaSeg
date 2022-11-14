def segundos(h, m, s):
    horas=h*3600
    minutos=m*60
    s +=minutos + horas
    return s
def main():
    h=int(input('Dame las horas '))
    m=int(input('Dame los minutos '))
    s=int(input('Dame los segundos '))
    h_2=int(input('Dame las horas '))
    m_2=int(input('Dame los minutos '))
    s_2=int(input('Dame los segundos '))
    res_1=(segundos(h,m, s))
    res_2=(segundos(h_2, m_2, s_2))
    print('Proceso 1: ' +str(res_1))
    print('Proceso 2: ' +str(res_2))
    
main()
