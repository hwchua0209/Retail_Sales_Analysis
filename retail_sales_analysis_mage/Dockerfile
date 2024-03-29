FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}
ARG PIP=pip3

# Add Debian Bullseye repository
RUN echo 'deb http://deb.debian.org/debian bullseye main' > /etc/apt/sources.list.d/bullseye.list

# Install OpenJDK 11
RUN apt-get update -y && \
    apt-get install -y openjdk-11-jdk

# Remove Debian Bullseye repository
RUN rm /etc/apt/sources.list.d/bullseye.list

# Note: this overwrites the requirements.txt file in your new project on first run. 
# You can delete this line for the second run :) 

COPY requirements.txt ${USER_CODE_PATH}/requirements.txt 

RUN ${PIP} install -r ${USER_CODE_PATH}/requirements.txt

RUN python3 /app/install_other_dependencies.py --path ${USER_CODE_PATH}

CMD ["/bin/sh", "-c", "/app/run_app.sh"]