import numpy

def kalmanFilter(data, R=.001, Pi=1, Q=1e-5):
	"""
	Pi = inital P guess, default is 1
	R = Rk, estimate o fthe covariance of the observation noise
	Q = Qk, process variance 
	"""
	# allocate space for arrays
	n = len(data) # length of data, size of array
	xhat=numpy.zeros(n)		 # a posteri estimate of x
	P=numpy.zeros(n)		 # a posteri error estimate
	xhatminus=numpy.zeros(n) # a priori estimate of x
	Pminus=numpy.zeros(n)	 # a priori error estimate
	K=numpy.zeros(n)		 # gain or blending factor

	# intial guesses
	xhat[0] = data[0]
	P[0] = Pi #1.0

	for k in range(1,n):
		# time update
		xhatminus[k] = xhat[k-1]
		Pminus[k] = P[k-1]+Q

		# measurement update
		K[k] = Pminus[k]/( Pminus[k]+R )
		xhat[k] = xhatminus[k]+K[k]*(data[k]-xhatminus[k])
		P[k] = (1-K[k])*Pminus[k]
		
	return xhat
