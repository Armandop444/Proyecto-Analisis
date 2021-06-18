Algoritmo problema4
	n=1
	iterar=1
	aproximacion=0
	anterior=0
	factorial=1
	m=1
	Escribir "Ingrese el numero de cifras significativas: "
	Leer cifras
	ess=(0.5*(10^(2-cifras)))
	ea=0
	Escribir 'ingrese un valor para X'
	Leer x
	anterior=x
	Mientras iterar==1 Hacer
		n=((2*n)+1)
		Para contador<-1 Hasta n Con Paso 1 Hacer
			factorial=factorial*contador
		FinPara
		aproximacion=aproximacion+((-1^m)/factorial)*(x^n)
		m=m+1
		Si n>0 Entonces
			ea=(abs((aproximacion-anterior)/aproximacion))*100
			Si ea<ess Entonces
				iterar=2
			Fin Si
		FinSi
		anterior=aproximacion
	FinMientras
	Escribir aproximacion
	Escribir ea
	Escribir n
FinAlgoritmo