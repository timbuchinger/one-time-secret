# One-Time-Secret

## Development

See the launch.json file for debug and unit test profiles.

If updating the UI, run tailwindcss in watch mode.

```bash
npx tailwindcss -i ./project/static/src/input.css -o ./project/static/dist/css/output.css --watch
```

## Running

### Docker

```bash
docker run -p 5000:5000 -e ENCRYPTION_KEY="YOUR-ENCRYPTION-KEY" timbuchinger/one-time-secret:latest
```

### Local

```bash
pip install -r requirements.txt
flask run --host=0.0.0.0 --ENCRYPTION_KEY="YOUR-ENCRYPTION-KEY"
```
