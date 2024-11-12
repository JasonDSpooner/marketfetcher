pipeline {
    agent any
    
    // Run Monday-Friday at market close (4 PM EST)
    triggers {
        cron('0 16 * * 1-5')
    }
    
    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install pandas yfinance
                '''
            }
        }
        
        stage('Collect Market Data') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 collect_data.py
                '''
            }
        }
        
        stage('Display Data') {
            steps {
                // Create plot that Jenkins can display
                plotCSV()
            }
        }
        
        stage('Archive Data') {
            steps {
                // Archive the CSV file with today's date
                archiveArtifacts(
                    artifacts: 'market_data*.csv',
                    fingerprint: true,
                    onlyIfSuccessful: true
                )
            }
        }
    }
    
    post {
        cleanup {
            cleanWs()
        }
    }
}