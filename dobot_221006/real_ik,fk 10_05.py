import math
import numpy as np
import matplotlib.pyplot as plt

def FK(J1,J2,J3):

    L1 = 142
    L2 = 160
    L3 = 46 + 150 # 탁구채

    th1 = math.radians(J1)
    th2 = math.radians(J2)
    th3 = math.radians(J3)

    x = math.cos(th1)*(L1*math.sin(th2) + L2*math.cos(th3) + L3)
    y = math.sin(th1)*(L1*math.sin(th2) + L2*math.cos(th3) + L3)
    z = L1*math.cos(th2) - L2*math.sin(th3) - 40 #탁구채 부착

    x1 = L1*math.sin(th2)*math.cos(th1)
    y1 = L1*math.sin(th2)*math.sin(th1)
    z1 = L1*math.cos(th2)

    x2 = L2*math.cos(th3)*math.cos(th1) + x1
    y2 = L2*math.cos(th3)*math.sin(th1) + y1
    z2 = z1 - L2*math.sin(th3)

    return x,y,z,x1,y1,z1,x2,y2,z2

def IK(x,y,z):

    L1 = 142
    L2 = 160
    L3 = 46 + 150 # 탁구채

    z += 40

    r = math.sqrt(x**2+y**2)
    p = math.sqrt((r-L3)**2 + z**2)
    alpha = math.degrees(math.acos((L1**2+p**2-L2**2)/(2*L1*p)))
    beta = math.degrees(math.atan(z/(r-L3)))
    gama = math.degrees(math.acos((L1**2+L2**2-p**2)/(2*L1*L2)))

    J1 = math.degrees(math.atan(y/x))
    J2 = 90 - alpha - beta
    J3 = 90 + J2 - gama

    return J1,J2,J3

def main():

    while(1):
        '''
        x = float(input("x: "))
        y = float(input("y: "))
        z = float(input("z: "))

        J1 = float(input("J1: "))
        J2 = float(input("J2: "))
        J3 = float(input("J3: "))
        '''
        x = 196.9095
        y = 166.4020
        z = 19.6686
        J1 = 40.2001
        J2 = 36.7352
        J3 = 37.0267
    
        fk_x,fk_y,fk_z,x1,y1,z1,x2,y2,z2 = FK(J1,J2,J3)
        ik_j1,ikj_j2,ik_j3 = IK(x,y,z)

        print("x,y,z: %f,%f,%f" %(fk_x,fk_y,fk_z))
        print("J1,J2,J3: %f,%f,%f"%(ik_j1,ikj_j2,ik_j3))

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        fontlabel = {"fontsize":"large", "color":"gray", "fontweight":"bold"}
        ax.set_xlabel("X", fontdict=fontlabel)
        ax.set_ylabel("Y", fontdict=fontlabel)
        ax.set_title("Z", fontdict=fontlabel)
        #plt.xlim([0,670])
        #plt.ylim([0,1500])
        


        x01,y01,z01 = [0,x1],[0,y1],[0,z1]
        x12,y12,z12 = [x1,x2],[y1,y2],[z1,z2]
        x23,y23,z23 = [x2,fk_x],[y2,fk_y],[z2,fk_z]

        ax.plot(x01,y01,z01, color = 'b')
        ax.plot([x1,x2],[y1,y2],[z1,z2], color = 'y')
        ax.plot([x2,x],[y2,y],[z2,z], color = 'r')
        ax.scatter(x,y,z, color = 'r')

        plt.show()
        

main()
