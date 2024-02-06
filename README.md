Instruction to run app:

1. Install Docker desktop
2. Open Docker desktop to start the Docker host
3. Build an docker image using the dockerfile with the command --> docker build -t 'any name' .
4. Build a docker container using the docker image using the command --> docker run -p 5000:5000 --name 'any name' 'image_name'

Notes:
- Make sure locate the terminal prompt into the local repository address before running the
commands