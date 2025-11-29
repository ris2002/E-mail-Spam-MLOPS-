pipeline{
    agent any{
        stages{
            stage('retrive files'){
             url: 'https://github.com/ris2002/E-mail-Spam-MLOPS-.git',
            }
            stage('build and docker'){
                
                sh 'docker build -t email_spam_app:latest .'
                sh 'docker run -d -p 8000:8000 --name email_spam_container email_spam_app:latest'
                
            }
            stage('Test Deployment'){
                  sh '''
                curl -X POST "http://localhost:8000/predict_ada_model" \
                -H "Content-Type: application/json" \
                -d '{"text": "Free offer!!!!"}'
                '''
            }
        }
    }
}