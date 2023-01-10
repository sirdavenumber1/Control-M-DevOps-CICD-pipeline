pipeline {
    agent any
    stages {
        stage('Build') {
            environment {
                CONTROLM_CREDS = credentials('controlm-qa-creds')
                ENDPOINT = 'https://ctm01d:8443/automation-api'
                DescrxContent = "DEVDescriptor.json"
            }
            steps {
                sh '''         
                py UpdateJson.py DEV "ctmjobs/example001.json"
                
                sleep 3
                
                DescriptorFile=DEV_Descriptor.json
                
                echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                echo ${DescriptorFile}
                echo "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
                # var=$(<file)
                # var=$(<file)
                
                DescrContent=$(<DEV_Descriptor.json)
                echo "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
                echo ${DescrContent}
                echo "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
                
                username=$CONTROLM_CREDS_USR
                password=$CONTROLM_CREDS_PSW

                # Login
                login=$(curl -k -s -H "Content-Type: application/json" -X POST -d \\{\\"username\\":\\"$username\\",\\"password\\":\\"$password\\"\\} "$ENDPOINT/session/login" )
                token=$(echo ${login##*token\\" : \\"} | cut -d '"' -f 1)

                # Build
                #curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@ctmjobs/jobs.json" "$ENDPOINT/build"
                curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@$DescriptorFile" "$ENDPOINT/build"
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
                DescrContent = 'DEV_Descriptor.json'
            }
            steps {
                sh '''
                # execute all .sh scripts in the tests directory
                cd ./tests/
                for f in *.sh
                do
                    #bash "$f" -H || exit $?  # execute successfully or exit
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
                DescrContent = 'DEV_Descriptor.json'
            }
            steps {
                sh '''
                username=$CONTROLM_CREDS_USR
                password=$CONTROLM_CREDS_PSW
        
Temp_JobDef_path=temp_job_file.json
xTemp_JobDef_path=xtemp_job_file.json

# Login to automation API and start a session on Dev# 
login=$(curl -k -s -H "Content-Type: application/json" -X POST -d \\{\\"username\\":\\"$username\\",\\"password\\":\\"$password\\"\\} "$ENDPOINT/session/login" )

# Extract the token ID from session details from Dev# 
token=$(echo ${login##*token\\" : \\"} | cut -d '"' -f 1)

# Download the job definitions and save on json#
tmp=$(curl -k -H "Authorization: Bearer $token" "Content-Type: application/json" "$ENDPOINT/deploy/jobs?ctm=*&folder=DEV_ABC123")
echo "${tmp}" > xtemp_job_file.json 
curl -k -s -H "Authorization: Bearer $token" --request POST "$ENDPOINT/session/logout"

# Login to automation API and start a session on PROD# 
login=$(curl -k -s -H "Content-Type: application/json" -X POST -d \\{\\"username\\":\\"$username\\",\\"password\\":\\"$password\\"\\} "$ENDPOINT/session/login" ) 

# Extract the token ID from session details from PROD# 
token=$(echo ${login##*token\\" : \\"} | cut -d '"' -f 1)
#echo $token

# dynamic job def to transform and deploy#
curl -k -s -H "Authorization: Bearer $token" -X POST -F "definitionsFile=@$xTemp_JobDef_path" -F "deployDescriptorFile=@ctmjobs/DeployDescriptorPROD.json" "$ENDPOINT/deploy" 

# Log out from the session#
curl -k -s -H "Authorization: Bearer $token" -X POST "$ENDPOINT/session/logout"

# Clean up temp file#
# rm -f $Temp_JobDef_path
                '''                
            }
        }
    }
}
