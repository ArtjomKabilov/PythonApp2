import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Формирование данных и построение диаграммы
#fail=open("dannie.txt","r")
#mas1=[]
#mas2=[]
#for line in fail:
    #n=line.find(",")
   # mas1.append(line[0:n].strip())
   # mas2.append(int(line[n+1:len(line)].strip()))
#fail.close()
#title = "Данные о ИТ безопасности"
#plt.grid(True)
#color_rectangle = np.random.rand(7, 3)
#plt.barh(mas1, mas2, color=color_rectangle)
#plt.show()

x1 = np.arange(-12,13)
y1 =(-1/18)*(x1**2)+12
plt.plot(x1,y1,color='black',linestyle='-',marker='')
x2 = np.arange(-4,5)
y2=(-1/8)*(x2**2)+6
plt.plot(x2,y2,color='black',linestyle='-',marker='')
x3 = np.arange(-12,-4)
y3=(-1/8)*(x3+8)**2+6
plt.plot(x3,y3,color='black',linestyle='-',marker='')
x4 = np.arange(4,13)
y4=(-1/8)*(x4-8)**2+6
plt.plot(x4,y4,color='black',linestyle='-',marker='')
x5 = np.arange(-4,-0.2,0.1)
y5=2*(x5+3)**2-9
plt.plot(x5,y5,color='black',linestyle='-',marker='')
x6 = np.arange(-4,0.1,0.2)
y6=1.5*(x6+3)**2-10
x7 =np.array([5,5])
y7=np.array([15,13])
plt.plot(x7,y7,color='blue',linestyle='-',marker='s')
x8 =np.array([-5,-5])
y8=np.array([-15,-13])
plt.plot(x8,y8,color='blue',linestyle='-',marker='s')
x9 =np.array([4,4])
y9=np.array([10,12])
plt.plot(x9,y9,color='blue',linestyle='-',marker='s')
x10 =np.array([4,4])
y10=np.array([10,12])
plt.plot(x10,y10z,color='blue',linestyle='-',marker='s')
plt.title("Зонтик")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(axis="y",c="black",alpha=.4,lw=5,ls="-")
plt.xticks(np.arange(-15,16,5))
plt.yticks(np.arange(-15,16,5))
plt.grid(True)


plt.savefig("my_image.png") 
plt.show()  
