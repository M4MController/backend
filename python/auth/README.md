# M4M Receiver Backend
The entry point for the controllers located in your home.

## API
API structure is similar to [VK API](https://vk.com/dev/methods)
structure.

### controller
#### /controller.setOnline
* controller_mac: string

### sensor
#### /sensor.setStatus
* controller_mac: string
* sensor_id: int
* error_message: string

#### /sensor.addRecord
* controller_mac: string
* sensor_id: int
* value: int
* timestamp: string

## Build and run
At first create configuration file (`config.yml`) for your case. See
[config.yml.example](config.yml.example).

### Using docker
1. Build the image
```bash
docker build -t m4m-receiver .
```

2. Run the container
```bash
docker run -p 80:5000 m4m-receiver
```

### Using virtualenv
1. Create environment and install dependencies
```bash
virtualenv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

```

2. Run the app
```bash
python3 app.py
```
