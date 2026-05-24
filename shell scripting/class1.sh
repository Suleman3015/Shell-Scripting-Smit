# shell for executing script
#!/bin/bash

# variable declaration
welcome="welcome to my script"

echo "hello world"
echo "hello world $welcome"
echo $welcome


# to take input and call variable
sth_name=""
echo "enter your name"
read sth_name
echo $sth_name

# arguments
name=$1
echo "hello $name"
# echo $0

student_answer=""
echo "q1: when was pakistan founded?"
echo "a) 1947"
echo "b) 1950"
echo "c) 1945"
echo "d) 1955"
# echo "enter your answer"
read student_answer

# student_answer=${student_answer^^} # convert to upper case
student_answer=${student_answer,,} #convert to lower case


#set if condition for correct answer
if [[ "$student_answer" == "a" ]]; then
    echo "correct answer"
else
    echo "wrong answer"
fi
