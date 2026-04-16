#!/bin/bash
# revising

# 1- variables
# read, argument, flex


# Flag Argument For Variable
name=""
gender=("A) Male" "B) Female")
while getopts "n:" opt; do
  case $opt in
    n) name=$OPTARG;;
    *) echo "Invalid option/flag";;
  esac
done

greet() {
    echo "Welcome $1"
}

if [ -z "$name" ]; then
    echo "Please rerun thes script with -n flag followed by your name. Example: ./class9.sh -n John"
    exit 1
    else
        greet "$name"

fi



echo "Welcome $name"
echo ""
echo "Please Select Your Gender"


# Flag Argument For Array

for ((i=0; i<${#gender[@]};i++)); 
do
  echo "${gender[i]}"
done
  
while $true; do
read gndr
    gndr=${gndr^^} # Convert input to uppercase
    if [[ "$gndr" =~ ^[AB]$ ]]; then
        case $gndr in
            A) gndr="Male";;
            B) gndr="Female";;
            esac
            echo "Your selected $gndr"

        break
    else
        echo "Invalid option. Please enter A or B."
        
    fi
done

# echo "Your selected $gndr"
