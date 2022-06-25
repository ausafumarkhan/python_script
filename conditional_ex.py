# This script will implement conditions and different datatypes

print("This IT organisation has various skill sets")
print("Find out your match")

Devops=["Jenkis=ns","Bash","Python","Ansible","Docker"."Kubernetes","Terraform"]
Development=["Java","NodeJs","Dotnet","PHP","HTML"]

cntr_emp1={"Name":"Sunny","Skill":"Blockchain","code":1024}
cntr_emp2={"Name":"Rocky","Skill":"AI","code":1018}

usr_skill=inpu("Enter your skill:")

print(usr_skill)

if (usr_skill in Devops):
    print("We have this skill in Devops.")
elif (usr_skill in Development):
    print("We have this skill in Development.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print("We have contract employees of this skills")
else:
    print("Please enter correct spelling or enter value in capitalized first letter")


