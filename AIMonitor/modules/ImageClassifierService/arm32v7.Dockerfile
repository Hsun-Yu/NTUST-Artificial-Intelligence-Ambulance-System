FROM balenalib/raspberrypi3:20181025
# The balena base image for building apps on Raspberry Pi 3. 
# Raspbian Stretch required for piwheels support. https://downloads.raspberrypi.org/raspbian/images/raspbian-2019-04-09/
RUN [ "cross-build-start" ]

RUN echo "BUILD MODULE: ImageClassifierService"


# Install dependencies
RUN install_packages \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libopenjp2-7-dev \
    libtiff5-dev \
    zlib1g-dev \
    libjpeg-dev \
    libatlas-base-dev \
    wget

# Install Python packages
COPY /build/arm32v7-requirements.txt ./
RUN pip3 install --upgrade pip 
RUN pip3 install --upgrade setuptools
RUN pip3 install --index-url=https://www.piwheels.org/simple -r arm32v7-requirements.txt
#RUN pip3 install --default-timeout=1000 --index-url=https://www.piwheels.org/simple -r arm32v7-requirements.txt --no-cache-dir

#install tensorflow==1.12.0
RUN wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.12.0/tensorflow-1.12.0-cp35-none-linux_armv7l.whl
RUN pip3 install tensorflow-1.12.0-cp35-none-linux_armv7l.whl
RUN rm tensorflow-1.12.0-cp35-none-linux_armv7l.whl

# Cleanup
RUN rm -rf /var/lib/apt/lists/* \
    && apt-get -y autoremove

RUN [ "cross-build-end" ]

# Add the application
ADD app /app

# Expose the port
EXPOSE 80

# Set the working directory
WORKDIR /app

# Run the flask server for the endpoints
CMD ["python3","app.py"]
