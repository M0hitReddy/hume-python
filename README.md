
## Create a Virtual Environment

Create a virtual environment in the directory `evi-env`:
```sh
python -m venv evi-env
```

Activate the virtual environment:

On Mac/Linux:
```sh
source evi-env/bin/activate
```

## Install Dependencies

On Mac:
```sh
pip install -r requirements_mac.txt
```

(or)

On Linux:
```sh
pip install -r requirements_linux.txt
```

## Environment Variables

Create a `.env` file with the following content:
```
HUME_API_KEY="<YOUR API KEY>"
HUME_SECRET_KEY="<YOUR SECRET KEY>"
```

## Run the Application

```sh
cd src
python main.py
```
