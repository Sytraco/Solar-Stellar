import numpy as np

class MethodNum:
    def __init__(self, x, dt) -> None:
        self.x = x
        self.Ts = dt

    def _set_initial_type(self, initial_condition):

        """
        Forces the initial condition type as np.ndarray.

        Parameter :
        -----------
        initial_condition : int, float, list, tuple, ndarray

        Return :
        -----------
        init : ndarray

        """
    
        if not isinstance(initial_condition, np.ndarray):

            if isinstance(initial_condition, list):
                init = np.array(initial_condition)
            else:
                init = np.array([initial_condition])
        else:
            init = initial_condition
        
        return init
    
    def init_compute(self, y0, stop_point):

        # number of points in the time axis
        self.N = self.x.size

        # set the initial condition as np.ndarray
        y0 = self._set_initial_type(initial_condition=y0)

        # get the spatial dimension of the problem, for example : 2D with (x0, y0) --> order = 2
        order = y0.shape[0]

        # set the stopping parameter of the computation loop
        loop = self.N-1 if stop_point is None else (stop_point - 1 if stop_point <= self.N - 1 else print(f"Expected size is out of bounds for index {self.x.size}"))

        # initial axis for the estimated solution
        y = np.zeros((order, self.N)) if stop_point is None else np.zeros((order, loop + 1))

        # applying the initial conditions
        y[:, 0] = y0

        return y, y0, loop, order

class RungeKutta(MethodNum):
    
    def __init__(self, x, dt, order):
        super().__init__(x, dt)
        self.q = order
        
        if order == 4:
            self.A = np.roll(np.diag([0, 1/2, 1/2, 1]), -1)
            self.B = np.array([1/6, 1/3, 1/3, 1/6])
            self.C = np.array([0, 1/2, 1/2, 1])

    # RK4 scheme solution from TP corrections
    def rk2D(self, EDO, y0, nb_point=None):

        y, y0, loop, _ = self.init_compute(y0=y0, stop_point=nb_point)

        x = np.copy(self.x)
        
        for i in range(loop):
            K1 = EDO(x_axis=x[i]     ,  ydy=y[:,i])
            K2 = EDO(t=x[i]+self.Ts/2,  ydy=y[:,i]+self.Ts/2*K1)
            K3 = EDO(t=x[i]+self.Ts/2,  ydy=y[:,i]+self.Ts/2*K2)
            K4 = EDO(t=x[i]+self.Ts  ,  ydy=y[:,i]+self.Ts*K3)
            y[:,i+1] = y[:,i] + self.Ts/6*(K1 + 2*K2 + 2*K3 + K4)
            x[i+1] = x[i] + self.Ts

        return y
            
    # General scheme for RK order q
    def compute(self, EDO, y0, excitation=False, nb_point=None):
        
        y_rk, y0, loop, order = self.init_compute(y0=y0, stop_point=nb_point)
        
        for xi, xn in zip(range(loop), self.x):
            
            K = np.zeros((order, self.q+1))

            for i in range(1, self.q+1):
                
                K[:, i] = EDO(
                    ydy = y_rk[:, xi] + self.Ts * (self.A[i-1, i-2] * K[:, i-1]),
                    x_axis  = xn + self.C[i-1] * self.Ts
                    )

            K = [np.delete(arr=K, obj=0) if K.size == K.shape[0] else np.delete(arr=K, obj=0, axis=1)][0]

            y_rk[:, xi+1] = y_rk[:, xi] + self.Ts * np.sum(self.B * K, axis=1)
        
        return y_rk