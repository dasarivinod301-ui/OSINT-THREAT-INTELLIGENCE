# API Usage

- AlienVault OTX
- VirusTotal
- AbuseIPDB
## API Key Management Approach
**Security**: We store all sensitive API Keys in a '.env' file to keep them private.
**Environment Variables**: The application uses the 'python-dotenv' library to load keys securely.
**Prevention**: The '.env' file is included in '.gitignore' to prevent it from being uploadedto the public GitHub reposirory.
