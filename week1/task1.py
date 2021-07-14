import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):

        t=1
        while t <n+1:
            self.x = self.x + v*(np.cos(self.theta))*self.dt
            self.y = self.y + v*(np.sin(self.theta))*self.dt
            self.theta = self.theta + w*self.dt

            self.x_points.append(self.x)
            self.y_points.append(self.y)
            t+=1

    def plot(self, v: float, w: float, n: int):
        self.step(v,w,n) 
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        #plt.show()
        s="unicycle_"+str(v)+"_"+str(w)+".png"
        plt.savefig(s)

if __name__ == "__main__":
    print("Unicycle Model Assignment")

    robot = Unicycle(0,0,0.77,0.05)
    robot.plot(5,4,50)
    # make an object of the robot and plot various trajectories