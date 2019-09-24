FROM alpine:latest

LABEL description="This is a cc65 Docker container intended to be used for build pipelines."

ENV BUILD_DIR="/tmp" \
    CC65_VERSION="V2.17" \
    NULIB2_VERSION="v3.1.0" \
    AC_RELEASE="v1-4-0" \
    AC_VERSION="1.4.0"

# COPY bin /usr/local/bin

WORKDIR ${BUILD_DIR}

#RUN wget https://github.com/cc65/cc65/archive/${CC65_VERSION}.tar.gz
COPY ${CC65_VERSION}.tar.gz .

RUN apk add --no-cache build-base && \
    echo "Building CC65 ${CC65_VERSION}" && \    
    tar xzf ${CC65_VERSION}.tar.gz
   
# WORKDIR /${BUILD_DIR}/cc65-2.17 

RUN cd cc65* && \
    env PREFIX=/usr/local make >/dev/null && \
    env PREFIX=/usr/local make install >&/dev/null && \
    echo "Cleaning up" && \
    cd ${BUILD_DIR} && \
    rm -rf * && \
    apk del --no-cache build-base && \
    echo "Adding other required build-tools exclusive of other C compilers!" && \
    apk add --no-cache make git 

RUN apk add --no-cache  gcc libc-dev
RUN wget https://github.com/meonwax/acme/archive/master.zip && unzip -q master && cd acme-master/src && make && make install
RUN rm -r acme-master master.zip



# Download X16 emulator + roms and compile it 

WORKDIR /
RUN git clone --depth 1 https://github.com/commanderx16/x16-emulator.git
WORKDIR /x16-emulator/
RUN apk add --no-cache sdl2-dev bash && make 


WORKDIR /
RUN git clone --depth 1 https://github.com/commanderx16/x16-rom
RUN cd /x16-rom/ && make && mv rom.bin /x16-emulator/

# Deps needed for releasing: numpy compilation is LONG 
RUN apk add --no-cache  python3 python3-dev zlib-dev jpeg-dev && pip3 install numpy==1.17.2
RUN pip3 install Pillow==6.1.0

#RUN make

