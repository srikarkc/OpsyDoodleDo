#!/bin/bash
echo "Usage $0 <add|delete|list|check> [username]"
add_user() {
        # local variable
        local username="$1"
        sudo useradd $username
        echo "User $username has been added successfully!"
}

del_user() {
        local username="$1"
        sudo userdel -r $username
        echo "User $username has been terminated successfully!"
}

list_user() {
        for user in $(cut -d: -f1 /etc/passwd); do
                echo $user
        done
}

check_user() {
        #global_variable
        if id $username &> /dev/null; then
                echo "User $username exists"
        else
                echo "User $username does not exist"
        fi
}

command="$1"
username="$2"

case "$command" in
        add)
                add_user "$username"
                ;;
        delete)
                del_user "$username"
                ;;
        list)
                list_user
                ;;
        check)
                check_user
                ;;

        *)
                echo "Incorrect command"
                exit 1
                ;;
esac