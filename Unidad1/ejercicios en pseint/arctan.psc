Algoritmo sin_titulo
	n = 1
	iterar = 1
	m = 1
	Escribir 'Ingrese las cifras significativas'
	Leer cifras
	ess = (0.5*(10^(2-cifras)))
	ea = 0
	Escribir 'Ingrese el valor de x'
	Leer x
	aproximacion = 0
	anterior = 0
	Mientras iterar == 1 Hacer
		Si m MOD 2==0 Entonces
			n=((2*n)+1)
			aproximacion = aproximacion-((x^(n))/(n))
			m = m+1
		SiNo 
			aproximacion = aproximacion+((x^(n))/(n))
			m = m+1
		FinSi
		Si n>0 Entonces
			ea = (abs((aproximacion-anterior)/aproximacion)*100)
			Si ea<ess Entonces
				iterar = 2
			FinSi
		FinSi
		anterior = aproximacion
	    n=n+1
		
	FinMientras
	Escribir 'El valor de Arctan(x) es:', aproximacion
	Escribir 'El valor de ea es:', ea
	
FinAlgoritmo
