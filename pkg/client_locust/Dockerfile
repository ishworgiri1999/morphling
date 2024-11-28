FROM  python:3.6


ENV PYTHONUNBUFFERED=0
ENV PIP_PREFER_BINARY=1

RUN if [ "$(uname -m)" = "ppc64le" ] || [ "$(uname -m)" = "aarch64" ]; then \
    apt-get -y update && \
    apt-get -y install gfortran libopenblas-dev liblapack-dev && \
    pip install cython 'numpy>=1.13.3'; \
    fi

RUN GRPC_HEALTH_PROBE_VERSION=v0.4.28 && \
    if [ "$(uname -m)" = "ppc64le" ]; then \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-ppc64le; \
    elif [ "$(uname -m)" = "aarch64" ]; then \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-arm64; \
    else \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64; \
    fi && \
    chmod +x /bin/grpc_health_probe

WORKDIR /workspace
ADD requirements.txt requirements.txt
RUN pip install  -r requirements.txt --no-build-isolation --no-cache-dir 

ADD . /workspace

ENV BATCH_SIZE=1
ENTRYPOINT ["/bin/sh", "-c", "sleep 100000"]
