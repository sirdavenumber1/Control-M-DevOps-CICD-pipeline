pipeline {
    agent any
    stages {
        stage('Build') {
            environment {
                CONTROLM_CREDS = credentials('controlm-qa-creds')
                ENDPOINT = 'https://ctm01d:8443/automation-api'
                CTM_ENV = 'DEV_'
            }
            steps {
                sh '''
                username=$CONTROLM_CREDS_USR
                password=$CONTROLM_CREDS_PSW

                # Login
                login=$(curl -k -s -H "Content-Type: application/json" -X POST -d \\{\\"username\\":\\"$username\\",\\"password\\":\\"$password\\"\\} "$ENDPOINT/session/login" )
                token=$(echo ${login##*token\\" : \\"} | cut -d '"' -f 1)

                # Build
                # curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@ctmjobs/MFT-conn-profiles.json" "$ENDPOINT/build"
                curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@ctmjobs/jobs.json" "$ENDPOINT/build"
                curl -k -s -H "Authorization: Bearer $token" -X POST "$ENDPOINT/session/logout"
                '''
            }
        }
        stage('Test') {
            when {
            expression {
                return env.BRANCH_NAME != 'master';
                }
            }
            environment {
                CONTROLM_CREDS = credentials('controlm-qa-creds')
                ENDPOINT = 'https://ctm01d:8443/automation-api'
                CTM_ENV = 'DEV_TEST_'
            }
            steps {
                sh '''
                # execute all .sh scripts in the tests directory
                cd ./tests/
                for f in *.sh
                do
                    bash "$f" -H || exit $?  # execute successfully or exit
                done
                cd ..
                '''
            }
        }
        stage('Deploy') {
            when{
                expression {
                return env.BRANCH_NAME != 'master';
                }
            }
            environment {
                CONTROLM_CREDS = credentials('controlm-qa-creds')
                ENDPOINT = 'https://ctm01d:8443/automation-api'
                CTM_ENV = 'DEV_PROD_'
            }
            steps {
                sh '''
                username=$CONTROLM_CREDS_USR
                password=$CONTROLM_CREDS_PSW

                # Login
 #               login=$(curl -k -s -H "Content-Type: application/json" -X POST -d \\{\\"username\\":\\"$username\\",\\"password\\":\\"$password\\"\\} "$ENDPOINT/session/login" )
 #               token=$(echo ${login##*token\\" : \\"} | cut -d '"' -f 1)

                # Deploy connection profiles and jobs
                # curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@ctmjobs/MFT-conn-profiles.json" "$ENDPOINT/deploy"
  #              curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@ctmjobs/PROD_jobs.json" "$ENDPOINT/deploy"
  #              curl -k -s -H "Authorization: Bearer $token" -X POST "$ENDPOINT/session/logout"
                
                
                
                
Temp_JobDef_path=temp_job_file.json
xTemp_JobDef_path=xtemp_job_file.json
#Temp_JobDef_path=/cygdrive/c/temp_job_file.json
#Temp_JobDef_path=/cygdrive/c/temp_job_file.json

# Login to automation API and start a session on Dev# 
# devLogin=$(curl -s --insecure --header "Content-Type: application/json" --request POST --data "{\"username\":\"$devUser\",\"password\":\"$devPasswd\"}" "$devEndPoint/session/login") 
login=$(curl -k -s -H "Content-Type: application/json" -X POST -d \\{\\"username\\":\\"$username\\",\\"password\\":\\"$password\\"\\} "$ENDPOINT/session/login" )

# Extract the token ID from session details from Dev# 
# token=$(echo ${login##*token\" : \"} | cut -d '"' -f 1)
token=$(echo ${login##*token\\" : \\"} | cut -d '"' -f 1)
#echo $token

# Download the job definitions and save on json#
tmp=$(curl -k -H "Authorization: Bearer $token" "Content-Type: application/json" "$ENDPOINT/deploy/jobs?ctm=*&folder=DEV_ABC123")

#echo -e $tmp | sed 's/\\"/"/g;s/"{/{/;s/}"/}/' > /tmp/temp_job_file.json
#echo -e $tmp | sed 's/\\"/"/g;s/"{/{/;s/}"/}/' > /cygdrive/c/temp_job_file.json
#echo -e $tmp | sed 's/\\"/"/g;s/"{/{/;s/}"/}/' > xtemp_job_file.json
echo -e $tmp > xtemp_job_file.json
#Temp_JobDef_path
sleep 10

#curl -k -s -H "Authorization: Bearer $token" --request POST --data "{\"username\":\"$username\",\"token\":\"$token\"}" "$ENDPOINT/session/logout"
curl -k -s -H "Authorization: Bearer $token" --request POST "$ENDPOINT/session/logout"

# Login to automation API and start a session on PROD# 
# PRODlogin=$(curl -s --insecure --header "Content-Type: application/json" --request POST --data "{\"username\":\"$prodUser\",\"password\":\"$prodPasswd\"}" "$prodEndPoint/session/login") 
login=$(curl -k -s -H "Content-Type: application/json" -X POST -d \\{\\"username\\":\\"$username\\",\\"password\\":\\"$password\\"\\} "$ENDPOINT/session/login" ) 

# Extract the token ID from session details from PROD# 
token=$(echo ${login##*token\\" : \\"} | cut -d '"' -f 1)
#echo $token

# dynamic job def to transform and deploy#
# curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@$Temp_JobDef_path" -F "deployDescriptorFile=@ctmjobs/DeployDescriptorPROD.json" "$ENDPOINT/deploy" 
curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@$Temp_JobDef_path" -F "deployDescriptorFile=@ctmjobs/DeployDescriptorPROD.json" "$ENDPOINT/deploy" 
#curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@ctmjobs/PP_jobs.json" -F "deployDescriptorFile=@ctmjobs/DeployDescriptorPROD.json" "$ENDPOINT/deploy" 
#curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@ctmjobs/test0001.json" -F "deployDescriptorFile=@ctmjobs/DeployDescriptorPROD.json" "$ENDPOINT/deploy" 

# Log out from the session#
#curl -k -s -H "Authorization: Bearer $token" --request POST --data "{\"username\":\"$username\",\"token\":\"$token\"}" "$ENDPOINT/session/logout"
curl -k -s -H "Authorization: Bearer $token" -X POST "$ENDPOINT/session/logout"

# Clean up temp file#
# rm -f $Temp_JobDef_path
                '''                
            }
        }
    }
}
