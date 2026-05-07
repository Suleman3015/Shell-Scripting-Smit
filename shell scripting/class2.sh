#!/bin/bash


questions=("When was pakistan founded?
A: 1947
B: 1950
C: 1945
D: 1955
" "Who was the founder of pakistan?
A: Muhammad Ali Jinnah
B: Allama Iqbal
C: Liaquat Ali Khan
D: Fatima Jinnah
")
answers=(1947 1923 1923 1922)

echo ${questions[@]} // @ means every element of array
echo ${questions[0]} // 0 means first element of array
echo ${#questions[@]} # to count number of elements in array - length of arrray

#loop

# for question in "${question[@]}"
# do
#     echo "$question"
# done


# for question in "${#questions[@]}"
# do
#     echo "$question"
# done


for (( i=0; i<${#questions[@]}; i++ ))
do
    echo "Q$((i+1)). ${questions[i]}"
    echo -n "your answer: (A/B/C/D): "
    read answer
done


# while loop

i=0
while [ $i -lt ${#questions[@]} ]
do
    echo $i
    ((i++))
done

