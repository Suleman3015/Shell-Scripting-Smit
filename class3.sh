#!/bin/bash

#functions

# name="suleman"
# Captalize(){
#     echo $name
# }
# Captalize


# bc (basic calculator)

add(){
    echo "$1 + $2" | bc
}

add 5 10

multiply(){
    echo "$1 * $2" | bc
}

subtract(){
    echo "$1 - $2" | bc
}

divide(){
    if [ $2 -eq 0 ]; then
        echo "Error: Division by zero is not allowed."
        exit 1
    fi
    echo "scale=2; $1 / $2" | bc
}


read -p "Enter first number: " num1

while true; do
    read -p "Enter an operator (+, -, *, /): " op
     if [-z  $op ]; then
        echo "Operator cannot be empty. Please enter a valid operator."
        continue
    fi
    read -p "Enter second number: " num2

   # id numbers is not equal to number then show error
    # if ! [[ $num1 =~ ^-?[0-9]+$ ]] || ! [[ $num2 =~ ^-?[0-9]+$ ]]; then
    #     echo "Error: Please enter valid numbers."
    #     continue
    # fi
    case $op in
        "+")
            result=$(add $num1 $num2)
            echo "Result: $result"
            ;;
        "-")
            result=$(subtract $num1 $num2)
            echo "Result: $result"
            ;;
        "*")
            result=$(multiply $num1 $num2)
            echo "Result: $result"
            ;;
        "/")
            result=$(divide $num1 $num2)
            echo "Result: $result"
            ;;
        *)
            echo "Invalid operator. Please enter +, -, *, or /."
            continue
            ;;
    esac

    

    # echo $num1
    # echo $op
    # echo $num2
done