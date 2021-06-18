Algoritmo ejercicio1
	n = 0
	salida=0
	iterar=0
	nuevo=0
	anterior=0
	e=2.71828182845905
	Repetir
		Escribir 'Ingrese valor inicial de x (tome en cuenta que x >= -e (2.71828182845905)).'
		Leer x
		Si (x<=-e)
			Escribir 'El numero ingresado es invalido.'
		FinSi
		
	Hasta Que x>-e
	Repetir
		Escribir 'Ingrese numero de cifras significativas.(tome en cuenta cifras significativas > 0).'
		Leer cifrassignificativas
		Si (cifrassignificativas<=0)
			Escribir 'El numero ingresado es invalido.'
		FinSi
		
	Hasta Que cifrassignificativas>0
	ess=0.5*(10^(2-cifrassignificativas))
	Escribir "Su error verdadero tiene que ser de ess=",ess
	
	Repetir
		Si n==0
			nuevo = 1
		SiNo
			Si n%2 == 0
				nuevo = nuevo - (x^n)/(n*(e^n))
			SiNo	
				nuevo = nuevo + (x^n)/(n*(e^n))
			FinSi
		FinSi
		Si n<>0
			ea = (abs(nuevo-anterior)/nuevo)*100
		FinSi
		Escribir 'El valor en la iteracion ', n+1, ' es de ', nuevo
		Escribir 'Su error aproximado es de ', ea
		Escribir '------------------------------------------'
		anterior=nuevo
		n = n+1
		
	Hasta Que ea<ess y ea<>0
	
	
FinAlgoritmo
