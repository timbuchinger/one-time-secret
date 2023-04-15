# One-Time-Secret

## Development

See the launch.json file for debug and unit test profiles.

## Running

### Docker

docker run -p 5000:5000 -e ENCRYPTION_KEY="YOUR-ENCRYPTION-KEY" timbuchinger/one-time-secret:latest

### Local

pip install -r requirements.txt
flask run --host=0.0.0.0 --ENCRYPTION_KEY="YOUR-ENCRYPTION-KEY"
