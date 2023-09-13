import numpy as np
import matplotlib.pyplot as plt
import scipy as spy

y0=np.array([0,0.5,1.5,3,5,5.5,6,6.5,8,9,12,15,16,17,17.5,19,20,25,35,38,40,41,42,43,44,45,48,50,52,58,58.5])
y00=[0,0.5,1.5,3,5,5.5,6,6.5,8,9,12,15,16,17,17.5,19,20,25,35,38,40,41,42,43,44,45,48,50,52,58,58.5]

y001=[]
k=0
for i in y00:
    try:
        y001.append((-y00[k]+y00[k+1])/2)
        k=k+1
    except:
        k=k+1
        continue

x001=[]
ii=0
for y in y001:
    ii=ii+1
    x001.append(ii-1)

y002=[]
kk=0
for iiu in y001:
    try:
        y002.append((-y001[kk]+y001[kk+1])/2)
        kk=kk+1
    except:
        kk=kk+1
        continue

x002=[]
iii=0
for y in y002:
    iii=iii+1
    x002.append(iii-1)


x0=np.array([])
i=0
for y in y0:
    i=i+1
    x0=np.append(x0,i-1)

#minimos cuadrados
grado=6
a = np.polyfit(x0,y0,grado)
r=0
y_ajustado=0
while r<=grado:
    y_ajustado=a[r]*(x0)**(grado-r)+y_ajustado
    r=r+1

#spline cubico
f1 = spy.interpolate.CubicSpline(x0, y0)
f1x=f1.derivative(nu=1)(x0)
f1x2=f1.derivative(nu=2)(x0)

def plotPosSpline(x,y,f):
    plt.plot(x,y,'og')
    plt.plot(x, f(x), 'k')
    plt.xlabel('Tiempo [s]',fontsize=15)
    plt.ylabel('Posición [m]',fontsize=15)
    plt.legend(('Datos experimentales', 'Interpolación spline cubico'), loc="upper left")
    plt.show()

def plotVelSpline(x,x1, y1, f1x):
    plt.plot(x1, y1, 'ob')
    plt.plot(x, f1x, 'k')
    plt.xlabel('Tiempo [s]',fontsize=15)
    plt.ylabel('Velocidad [m/s]',fontsize=15)
    plt.legend(('Datos calculados', 'Primera derivada'), loc="upper left")
    plt.show()

def plotAceSpline(x, x2,y2,f1x2):
    plt.plot(x2, y2, 'ob')
    plt.plot(x, f1x2, 'k')
    plt.xlabel('Tiempo [s]',fontsize=15)
    plt.ylabel('Aceleración [$m^{2}$/s]',fontsize=15)
    plt.legend(('Datos calculados', 'Segunda derivada'), loc="upper left")
    plt.show()

def plotPosMin(x,y,y_ajustado): 
    plt.plot(x,y,'og')
    plt.plot(x, y_ajustado, '')
    plt.xlabel('Tiempo [s]',fontsize=15)
    plt.ylabel('Posición [m]',fontsize=15)
    plt.legend(('Datos experimentales', 'Minimos cuadrados con grado 6.'), loc="upper left")
    plt.show()

#plotPosSpline(x0,y0,f1)
#plotVelSpline(x0,x001, y001, f1x)
#plotAceSpline(x0, x002,y002,f1x2)
#plotPosMin(x0,y0,y_ajustado)
