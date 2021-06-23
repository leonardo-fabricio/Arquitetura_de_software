echo "Digite Um Valor:"
    read n1
echo "Digite outro valor:"
    read n2

echo "O que deseja fazer? "
echo "1 - Soma"
echo "2 - Subtração"
echo "3 - Multiplicação"
echo "4 - Divisão"
read aux

if [ $aux -eq 1 ]
then
    echo "Resultado: $[n1+n2]"
fi

if [ $aux -eq 2 ] 
then
    echo "Resultado: $[n1-n2]"
fi

if [ $aux -eq 3 ] 
then
    echo "Resultado: $[n1*n2]"
fi

if [ $aux -eq 4 ] 
then
    if [ $n2 != 0 ] 
    then
        echo "Resultado: $[n1/n2]"
    else
        echo "Impossivel Dividir por Zero!"
    fi
fi

