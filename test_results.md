# Distributed Marketplace Pipeline Results
Run Date: Thu, May  7, 2026  7:18:38 PM

## 1. Building Docker Images
[1A[1B[0G[?25l[+] Building 0.0s (0/1)                                    docker:desktop-linux
[?25h[1A[0G[?25l[+] Building 0.2s (1/2)                                    docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.service               0.0s
[0m[36m => => transferring dockerfile: 409B                                       0.0s
[0m => [internal] load metadata for docker.io/library/python:3.11-slim        0.1s
[?25h[1A[1A[1A[1A[0G[?25l[+] Building 0.3s (1/2)                                    docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.service               0.0s
[0m[36m => => transferring dockerfile: 409B                                       0.0s
[0m => [internal] load metadata for docker.io/library/python:3.11-slim        0.3s
[?25h[1A[1A[1A[1A[0G[?25l[+] Building 0.5s (1/2)                                    docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.service               0.0s
[0m[36m => => transferring dockerfile: 409B                                       0.0s
[0m => [internal] load metadata for docker.io/library/python:3.11-slim        0.5s
[?25h[1A[1A[1A[1A[0G[?25l[+] Building 0.6s (1/2)                                    docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.service               0.0s
[0m[36m => => transferring dockerfile: 409B                                       0.0s
[0m => [internal] load metadata for docker.io/library/python:3.11-slim        0.6s
[?25h[1A[1A[1A[1A[0G[?25l[+] Building 0.7s (2/2)                                    docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.service               0.0s
[0m[36m => => transferring dockerfile: 409B                                       0.0s
[0m[36m => [internal] load metadata for docker.io/library/python:3.11-slim        0.7s
[0m[?25h[1A[1A[1A[1A[0G[?25l[+] Building 0.8s (4/10)                                   docker:desktop-linux
[36m => => transferring dockerfile: 409B                                       0.0s
[0m[36m => [internal] load metadata for docker.io/library/python:3.11-slim        0.7s
[0m[36m => [internal] load .dockerignore                                          0.0s
[0m[36m => => transferring context: 2B                                            0.0s
[0m[36m => [1/6] FROM docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m => [internal] load build context                                          0.1s
 => => transferring context: 367.59kB                                      0.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.1s (9/10)                                   docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m => [6/6] COPY . .                                                         0.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.2s (9/10)                                   docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m => [6/6] COPY . .                                                         0.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.4s (9/10)                                   docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m => [6/6] COPY . .                                                         0.5s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.4s (10/10)                                  docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.5s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     0.2s
 => => exporting layers                                                    0.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.7s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     0.3s
 => => exporting layers                                                    0.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.8s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     0.4s
 => => exporting layers                                                    0.4s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.0s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     0.6s
 => => exporting layers                                                    0.6s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.1s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     0.8s
 => => exporting layers                                                    0.7s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.3s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     0.9s
 => => exporting layers                                                    0.9s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.4s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     1.0s
 => => exporting layers                                                    1.0s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.6s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     1.2s
 => => exporting layers                                                    1.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.7s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     1.3s
 => => exporting layers                                                    1.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.9s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     1.5s
 => => exporting layers                                                    1.5s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.0s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     1.6s
 => => exporting layers                                                    1.6s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.2s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     1.8s
 => => exporting layers                                                    1.8s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.3s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     1.9s
 => => exporting layers                                                    1.9s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.5s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     2.1s
 => => exporting layers                                                    2.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.6s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     2.3s
 => => exporting layers                                                    2.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.8s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     2.4s
 => => exporting layers                                                    2.4s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.8s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m => exporting to image                                                     2.4s
[36m => => exporting layers                                                    2.4s
[0m[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.0s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     2.6s
[36m => => exporting layers                                                    2.4s
[0m[36m => => exporting manifest sha256:687186d270a54bc60ca62db7648e6174f4d58cbe  0.0s
[0m[36m => => exporting config sha256:5cf5b1193bcf8a9aa5b8c6eb4d86419423b7b46663  0.0s
[0m[36m => => exporting attestation manifest sha256:71d6a381278f4f0d06ad6ad7b32f  0.0s
[0m[36m => => exporting manifest list sha256:b62c322b4c0265c5102dd1c97e1a0bb199f  0.0s
[0m[36m => => naming to docker.io/library/kv-frontend:latest                      0.0s
[0m => => unpacking to docker.io/library/kv-frontend:latest                   0.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.1s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     2.8s
[36m => => exporting layers                                                    2.4s
[0m[36m => => exporting manifest sha256:687186d270a54bc60ca62db7648e6174f4d58cbe  0.0s
[0m[36m => => exporting config sha256:5cf5b1193bcf8a9aa5b8c6eb4d86419423b7b46663  0.0s
[0m[36m => => exporting attestation manifest sha256:71d6a381278f4f0d06ad6ad7b32f  0.0s
[0m[36m => => exporting manifest list sha256:b62c322b4c0265c5102dd1c97e1a0bb199f  0.0s
[0m[36m => => naming to docker.io/library/kv-frontend:latest                      0.0s
[0m => => unpacking to docker.io/library/kv-frontend:latest                   0.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.3s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     2.9s
[36m => => exporting layers                                                    2.4s
[0m[36m => => exporting manifest sha256:687186d270a54bc60ca62db7648e6174f4d58cbe  0.0s
[0m[36m => => exporting config sha256:5cf5b1193bcf8a9aa5b8c6eb4d86419423b7b46663  0.0s
[0m[36m => => exporting attestation manifest sha256:71d6a381278f4f0d06ad6ad7b32f  0.0s
[0m[36m => => exporting manifest list sha256:b62c322b4c0265c5102dd1c97e1a0bb199f  0.0s
[0m[36m => => naming to docker.io/library/kv-frontend:latest                      0.0s
[0m => => unpacking to docker.io/library/kv-frontend:latest                   0.5s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.4s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.1s
[36m => => exporting layers                                                    2.4s
[0m[36m => => exporting manifest sha256:687186d270a54bc60ca62db7648e6174f4d58cbe  0.0s
[0m[36m => => exporting config sha256:5cf5b1193bcf8a9aa5b8c6eb4d86419423b7b46663  0.0s
[0m[36m => => exporting attestation manifest sha256:71d6a381278f4f0d06ad6ad7b32f  0.0s
[0m[36m => => exporting manifest list sha256:b62c322b4c0265c5102dd1c97e1a0bb199f  0.0s
[0m[36m => => naming to docker.io/library/kv-frontend:latest                      0.0s
[0m => => unpacking to docker.io/library/kv-frontend:latest                   0.6s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.6s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.2s
[36m => => exporting layers                                                    2.4s
[0m[36m => => exporting manifest sha256:687186d270a54bc60ca62db7648e6174f4d58cbe  0.0s
[0m[36m => => exporting config sha256:5cf5b1193bcf8a9aa5b8c6eb4d86419423b7b46663  0.0s
[0m[36m => => exporting attestation manifest sha256:71d6a381278f4f0d06ad6ad7b32f  0.0s
[0m[36m => => exporting manifest list sha256:b62c322b4c0265c5102dd1c97e1a0bb199f  0.0s
[0m[36m => => naming to docker.io/library/kv-frontend:latest                      0.0s
[0m => => unpacking to docker.io/library/kv-frontend:latest                   0.8s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.7s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.4s
[36m => => exporting layers                                                    2.4s
[0m[36m => => exporting manifest sha256:687186d270a54bc60ca62db7648e6174f4d58cbe  0.0s
[0m[36m => => exporting config sha256:5cf5b1193bcf8a9aa5b8c6eb4d86419423b7b46663  0.0s
[0m[36m => => exporting attestation manifest sha256:71d6a381278f4f0d06ad6ad7b32f  0.0s
[0m[36m => => exporting manifest list sha256:b62c322b4c0265c5102dd1c97e1a0bb199f  0.0s
[0m[36m => => naming to docker.io/library/kv-frontend:latest                      0.0s
[0m => => unpacking to docker.io/library/kv-frontend:latest                   0.9s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.9s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.5s
[36m => => exporting layers                                                    2.4s
[0m[36m => => exporting manifest sha256:687186d270a54bc60ca62db7648e6174f4d58cbe  0.0s
[0m[36m => => exporting config sha256:5cf5b1193bcf8a9aa5b8c6eb4d86419423b7b46663  0.0s
[0m[36m => => exporting attestation manifest sha256:71d6a381278f4f0d06ad6ad7b32f  0.0s
[0m[36m => => exporting manifest list sha256:b62c322b4c0265c5102dd1c97e1a0bb199f  0.0s
[0m[36m => => naming to docker.io/library/kv-frontend:latest                      0.0s
[0m => => unpacking to docker.io/library/kv-frontend:latest                   1.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 5.0s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.6s
[36m => => exporting layers                                                    2.4s
[0m[36m => => exporting manifest sha256:687186d270a54bc60ca62db7648e6174f4d58cbe  0.0s
[0m[36m => => exporting config sha256:5cf5b1193bcf8a9aa5b8c6eb4d86419423b7b46663  0.0s
[0m[36m => => exporting attestation manifest sha256:71d6a381278f4f0d06ad6ad7b32f  0.0s
[0m[36m => => exporting manifest list sha256:b62c322b4c0265c5102dd1c97e1a0bb199f  0.0s
[0m[36m => => naming to docker.io/library/kv-frontend:latest                      0.0s
[0m[36m => => unpacking to docker.io/library/kv-frontend:latest                   1.1s
[0m[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 5.1s (11/11) FINISHED                         docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.service               0.0s
[0m[36m => => transferring dockerfile: 409B                                       0.0s
[0m[36m => [internal] load metadata for docker.io/library/python:3.11-slim        0.7s
[0m[36m => [internal] load .dockerignore                                          0.0s
[0m[36m => => transferring context: 2B                                            0.0s
[0m[36m => [1/6] FROM docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 595.59kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.5s
[0m[36m => exporting to image                                                     3.6s
[0m[36m => => exporting layers                                                    2.4s
[0m[36m => => exporting manifest sha256:687186d270a54bc60ca62db7648e6174f4d58cbe  0.0s
[0m[36m => => exporting config sha256:5cf5b1193bcf8a9aa5b8c6eb4d86419423b7b46663  0.0s
[0m[36m => => exporting attestation manifest sha256:71d6a381278f4f0d06ad6ad7b32f  0.0s
[0m[36m => => exporting manifest list sha256:b62c322b4c0265c5102dd1c97e1a0bb199f  0.0s
[0m[36m => => naming to docker.io/library/kv-frontend:latest                      0.0s
[0m[36m => => unpacking to docker.io/library/kv-frontend:latest                   1.1s
[0m[?25h[1A[1B[0G[?25l[+] Building 0.0s (0/1)                                    docker:desktop-linux
[?25h[1A[0G[?25l[+] Building 0.2s (1/2)                                    docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.storage               0.0s
[0m[36m => => transferring dockerfile: 409B                                       0.0s
[0m => [internal] load metadata for docker.io/library/python:3.11-slim        0.1s
[?25h[1A[1A[1A[1A[0G[?25l[+] Building 0.2s (2/2)                                    docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.storage               0.0s
[0m[36m => => transferring dockerfile: 409B                                       0.0s
[0m[36m => [internal] load metadata for docker.io/library/python:3.11-slim        0.2s
[0m[?25h[1A[1A[1A[1A[0G[?25l[+] Building 0.3s (4/10)                                   docker:desktop-linux
[36m => => transferring dockerfile: 409B                                       0.0s
[0m[36m => [internal] load metadata for docker.io/library/python:3.11-slim        0.2s
[0m[36m => [internal] load .dockerignore                                          0.0s
[0m[36m => => transferring context: 2B                                            0.0s
[0m[36m => [1/6] FROM docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m => [internal] load build context                                          0.1s
 => => transferring context: 350.74kB                                      0.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 0.5s (9/10)                                   docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m => [6/6] COPY . .                                                         0.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 0.7s (9/10)                                   docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m => [6/6] COPY . .                                                         0.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 0.8s (9/10)                                   docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m => [6/6] COPY . .                                                         0.5s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.0s (10/10)                                  docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.1s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.2s
 => => exporting layers                                                    0.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.3s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.3s
 => => exporting layers                                                    0.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.4s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.5s
 => => exporting layers                                                    0.5s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.6s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.6s
 => => exporting layers                                                    0.6s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.7s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.8s
 => => exporting layers                                                    0.7s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.9s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.9s
 => => exporting layers                                                    0.9s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.0s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.0s
 => => exporting layers                                                    1.0s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.2s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.2s
 => => exporting layers                                                    1.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.3s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.4s
 => => exporting layers                                                    1.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.5s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.5s
 => => exporting layers                                                    1.5s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.6s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.6s
 => => exporting layers                                                    1.6s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.8s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.8s
 => => exporting layers                                                    1.8s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.9s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.9s
 => => exporting layers                                                    1.9s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.1s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     2.1s
 => => exporting layers                                                    2.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.2s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     2.3s
 => => exporting layers                                                    2.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.4s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     2.4s
 => => exporting layers                                                    2.4s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.5s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     2.5s
 => => exporting layers                                                    2.5s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.6s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     2.6s
[36m => => exporting layers                                                    2.6s
[0m[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.8s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     2.8s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:c966656da6c9583dd986ff45d7342ba262eedd5f  0.0s
[0m[36m => => exporting config sha256:ffb90e0b5d133dbfe534db862f07157a55541bfa5b  0.0s
[0m[36m => => exporting attestation manifest sha256:05cda7a922af3665c09723e32060  0.0s
[0m[36m => => exporting manifest list sha256:35a6aa16f316962f60cffbce7c51a733e8b  0.0s
[0m[36m => => naming to docker.io/library/kv-storage:latest                       0.0s
[0m => => unpacking to docker.io/library/kv-storage:latest                    0.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.9s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.0s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:c966656da6c9583dd986ff45d7342ba262eedd5f  0.0s
[0m[36m => => exporting config sha256:ffb90e0b5d133dbfe534db862f07157a55541bfa5b  0.0s
[0m[36m => => exporting attestation manifest sha256:05cda7a922af3665c09723e32060  0.0s
[0m[36m => => exporting manifest list sha256:35a6aa16f316962f60cffbce7c51a733e8b  0.0s
[0m[36m => => naming to docker.io/library/kv-storage:latest                       0.0s
[0m => => unpacking to docker.io/library/kv-storage:latest                    0.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.1s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.1s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:c966656da6c9583dd986ff45d7342ba262eedd5f  0.0s
[0m[36m => => exporting config sha256:ffb90e0b5d133dbfe534db862f07157a55541bfa5b  0.0s
[0m[36m => => exporting attestation manifest sha256:05cda7a922af3665c09723e32060  0.0s
[0m[36m => => exporting manifest list sha256:35a6aa16f316962f60cffbce7c51a733e8b  0.0s
[0m[36m => => naming to docker.io/library/kv-storage:latest                       0.0s
[0m => => unpacking to docker.io/library/kv-storage:latest                    0.4s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.2s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.3s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:c966656da6c9583dd986ff45d7342ba262eedd5f  0.0s
[0m[36m => => exporting config sha256:ffb90e0b5d133dbfe534db862f07157a55541bfa5b  0.0s
[0m[36m => => exporting attestation manifest sha256:05cda7a922af3665c09723e32060  0.0s
[0m[36m => => exporting manifest list sha256:35a6aa16f316962f60cffbce7c51a733e8b  0.0s
[0m[36m => => naming to docker.io/library/kv-storage:latest                       0.0s
[0m => => unpacking to docker.io/library/kv-storage:latest                    0.6s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.4s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.4s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:c966656da6c9583dd986ff45d7342ba262eedd5f  0.0s
[0m[36m => => exporting config sha256:ffb90e0b5d133dbfe534db862f07157a55541bfa5b  0.0s
[0m[36m => => exporting attestation manifest sha256:05cda7a922af3665c09723e32060  0.0s
[0m[36m => => exporting manifest list sha256:35a6aa16f316962f60cffbce7c51a733e8b  0.0s
[0m[36m => => naming to docker.io/library/kv-storage:latest                       0.0s
[0m => => unpacking to docker.io/library/kv-storage:latest                    0.7s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.5s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.6s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:c966656da6c9583dd986ff45d7342ba262eedd5f  0.0s
[0m[36m => => exporting config sha256:ffb90e0b5d133dbfe534db862f07157a55541bfa5b  0.0s
[0m[36m => => exporting attestation manifest sha256:05cda7a922af3665c09723e32060  0.0s
[0m[36m => => exporting manifest list sha256:35a6aa16f316962f60cffbce7c51a733e8b  0.0s
[0m[36m => => naming to docker.io/library/kv-storage:latest                       0.0s
[0m => => unpacking to docker.io/library/kv-storage:latest                    0.9s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.7s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.7s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:c966656da6c9583dd986ff45d7342ba262eedd5f  0.0s
[0m[36m => => exporting config sha256:ffb90e0b5d133dbfe534db862f07157a55541bfa5b  0.0s
[0m[36m => => exporting attestation manifest sha256:05cda7a922af3665c09723e32060  0.0s
[0m[36m => => exporting manifest list sha256:35a6aa16f316962f60cffbce7c51a733e8b  0.0s
[0m[36m => => naming to docker.io/library/kv-storage:latest                       0.0s
[0m => => unpacking to docker.io/library/kv-storage:latest                    1.0s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.8s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.9s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:c966656da6c9583dd986ff45d7342ba262eedd5f  0.0s
[0m[36m => => exporting config sha256:ffb90e0b5d133dbfe534db862f07157a55541bfa5b  0.0s
[0m[36m => => exporting attestation manifest sha256:05cda7a922af3665c09723e32060  0.0s
[0m[36m => => exporting manifest list sha256:35a6aa16f316962f60cffbce7c51a733e8b  0.0s
[0m[36m => => naming to docker.io/library/kv-storage:latest                       0.0s
[0m[36m => => unpacking to docker.io/library/kv-storage:latest                    1.2s
[0m[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.9s (11/11) FINISHED                         docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.storage               0.0s
[0m[36m => => transferring dockerfile: 409B                                       0.0s
[0m[36m => [internal] load metadata for docker.io/library/python:3.11-slim        0.2s
[0m[36m => [internal] load .dockerignore                                          0.0s
[0m[36m => => transferring context: 2B                                            0.0s
[0m[36m => [1/6] FROM docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 623.24kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m[36m => exporting to image                                                     3.9s
[0m[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:c966656da6c9583dd986ff45d7342ba262eedd5f  0.0s
[0m[36m => => exporting config sha256:ffb90e0b5d133dbfe534db862f07157a55541bfa5b  0.0s
[0m[36m => => exporting attestation manifest sha256:05cda7a922af3665c09723e32060  0.0s
[0m[36m => => exporting manifest list sha256:35a6aa16f316962f60cffbce7c51a733e8b  0.0s
[0m[36m => => naming to docker.io/library/kv-storage:latest                       0.0s
[0m[36m => => unpacking to docker.io/library/kv-storage:latest                    1.2s
[0m[?25h[1A[1B[0G[?25l[+] Building 0.0s (0/1)                                    docker:desktop-linux
[?25h[1A[0G[?25l[+] Building 0.2s (1/2)                                    docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.controller            0.0s
[0m[36m => => transferring dockerfile: 418B                                       0.0s
[0m => [internal] load metadata for docker.io/library/python:3.11-slim        0.1s
[?25h[1A[1A[1A[1A[0G[?25l[+] Building 0.2s (2/2)                                    docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.controller            0.0s
[0m[36m => => transferring dockerfile: 418B                                       0.0s
[0m[36m => [internal] load metadata for docker.io/library/python:3.11-slim        0.2s
[0m[?25h[1A[1A[1A[1A[0G[?25l[+] Building 0.3s (4/10)                                   docker:desktop-linux
[36m => => transferring dockerfile: 418B                                       0.0s
[0m[36m => [internal] load metadata for docker.io/library/python:3.11-slim        0.2s
[0m[36m => [internal] load .dockerignore                                          0.0s
[0m[36m => => transferring context: 2B                                            0.0s
[0m[36m => [1/6] FROM docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m => [internal] load build context                                          0.1s
 => => transferring context: 340.50kB                                      0.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 0.4s (5/10)                                   docker:desktop-linux
[36m => => transferring dockerfile: 418B                                       0.0s
[0m[36m => [internal] load metadata for docker.io/library/python:3.11-slim        0.2s
[0m[36m => [internal] load .dockerignore                                          0.0s
[0m[36m => => transferring context: 2B                                            0.0s
[0m[36m => [1/6] FROM docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 651.82kB                                      0.2s
[0m[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 0.5s (9/10)                                   docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m => [6/6] COPY . .                                                         0.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 0.7s (9/10)                                   docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m => [6/6] COPY . .                                                         0.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 0.8s (9/10)                                   docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m => [6/6] COPY . .                                                         0.5s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.0s (10/10)                                  docker:desktop-linux
[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.1s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.2s
 => => exporting layers                                                    0.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.3s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.3s
 => => exporting layers                                                    0.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.4s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.5s
 => => exporting layers                                                    0.5s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.6s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.6s
 => => exporting layers                                                    0.6s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.7s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.8s
 => => exporting layers                                                    0.7s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 1.9s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     0.9s
 => => exporting layers                                                    0.9s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.0s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.0s
 => => exporting layers                                                    1.0s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.2s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.2s
 => => exporting layers                                                    1.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.3s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.4s
 => => exporting layers                                                    1.4s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.5s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.5s
 => => exporting layers                                                    1.5s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.6s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.7s
 => => exporting layers                                                    1.7s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.8s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.8s
 => => exporting layers                                                    1.8s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 2.9s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     1.9s
 => => exporting layers                                                    1.9s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.1s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     2.1s
 => => exporting layers                                                    2.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.2s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     2.2s
 => => exporting layers                                                    2.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.4s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     2.4s
 => => exporting layers                                                    2.4s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.5s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     2.6s
 => => exporting layers                                                    2.6s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.5s (10/11)                                  docker:desktop-linux
[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m => exporting to image                                                     2.6s
[36m => => exporting layers                                                    2.6s
[0m[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.7s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     2.8s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:f0c80a2f3f7ad937c38b1614a07c0b41e2f4af21  0.0s
[0m[36m => => exporting config sha256:5791caba6245f72730d35d5aaaedcb7da7c5495dd1  0.0s
[0m[36m => => exporting attestation manifest sha256:749454c206b30dd4f7b43d9b95bf  0.0s
[0m[36m => => exporting manifest list sha256:1a5a16341f90bcfe73fcb1d969164f03616  0.0s
[0m[36m => => naming to docker.io/library/kv-controller:latest                    0.0s
[0m => => unpacking to docker.io/library/kv-controller:latest                 0.1s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 3.9s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     2.9s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:f0c80a2f3f7ad937c38b1614a07c0b41e2f4af21  0.0s
[0m[36m => => exporting config sha256:5791caba6245f72730d35d5aaaedcb7da7c5495dd1  0.0s
[0m[36m => => exporting attestation manifest sha256:749454c206b30dd4f7b43d9b95bf  0.0s
[0m[36m => => exporting manifest list sha256:1a5a16341f90bcfe73fcb1d969164f03616  0.0s
[0m[36m => => naming to docker.io/library/kv-controller:latest                    0.0s
[0m => => unpacking to docker.io/library/kv-controller:latest                 0.3s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.0s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.1s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:f0c80a2f3f7ad937c38b1614a07c0b41e2f4af21  0.0s
[0m[36m => => exporting config sha256:5791caba6245f72730d35d5aaaedcb7da7c5495dd1  0.0s
[0m[36m => => exporting attestation manifest sha256:749454c206b30dd4f7b43d9b95bf  0.0s
[0m[36m => => exporting manifest list sha256:1a5a16341f90bcfe73fcb1d969164f03616  0.0s
[0m[36m => => naming to docker.io/library/kv-controller:latest                    0.0s
[0m => => unpacking to docker.io/library/kv-controller:latest                 0.4s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.2s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.2s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:f0c80a2f3f7ad937c38b1614a07c0b41e2f4af21  0.0s
[0m[36m => => exporting config sha256:5791caba6245f72730d35d5aaaedcb7da7c5495dd1  0.0s
[0m[36m => => exporting attestation manifest sha256:749454c206b30dd4f7b43d9b95bf  0.0s
[0m[36m => => exporting manifest list sha256:1a5a16341f90bcfe73fcb1d969164f03616  0.0s
[0m[36m => => naming to docker.io/library/kv-controller:latest                    0.0s
[0m => => unpacking to docker.io/library/kv-controller:latest                 0.6s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.3s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.4s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:f0c80a2f3f7ad937c38b1614a07c0b41e2f4af21  0.0s
[0m[36m => => exporting config sha256:5791caba6245f72730d35d5aaaedcb7da7c5495dd1  0.0s
[0m[36m => => exporting attestation manifest sha256:749454c206b30dd4f7b43d9b95bf  0.0s
[0m[36m => => exporting manifest list sha256:1a5a16341f90bcfe73fcb1d969164f03616  0.0s
[0m[36m => => naming to docker.io/library/kv-controller:latest                    0.0s
[0m => => unpacking to docker.io/library/kv-controller:latest                 0.7s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.5s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.5s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:f0c80a2f3f7ad937c38b1614a07c0b41e2f4af21  0.0s
[0m[36m => => exporting config sha256:5791caba6245f72730d35d5aaaedcb7da7c5495dd1  0.0s
[0m[36m => => exporting attestation manifest sha256:749454c206b30dd4f7b43d9b95bf  0.0s
[0m[36m => => exporting manifest list sha256:1a5a16341f90bcfe73fcb1d969164f03616  0.0s
[0m[36m => => naming to docker.io/library/kv-controller:latest                    0.0s
[0m => => unpacking to docker.io/library/kv-controller:latest                 0.9s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.6s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.7s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:f0c80a2f3f7ad937c38b1614a07c0b41e2f4af21  0.0s
[0m[36m => => exporting config sha256:5791caba6245f72730d35d5aaaedcb7da7c5495dd1  0.0s
[0m[36m => => exporting attestation manifest sha256:749454c206b30dd4f7b43d9b95bf  0.0s
[0m[36m => => exporting manifest list sha256:1a5a16341f90bcfe73fcb1d969164f03616  0.0s
[0m[36m => => naming to docker.io/library/kv-controller:latest                    0.0s
[0m => => unpacking to docker.io/library/kv-controller:latest                 1.0s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.8s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.8s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:f0c80a2f3f7ad937c38b1614a07c0b41e2f4af21  0.0s
[0m[36m => => exporting config sha256:5791caba6245f72730d35d5aaaedcb7da7c5495dd1  0.0s
[0m[36m => => exporting attestation manifest sha256:749454c206b30dd4f7b43d9b95bf  0.0s
[0m[36m => => exporting manifest list sha256:1a5a16341f90bcfe73fcb1d969164f03616  0.0s
[0m[36m => => naming to docker.io/library/kv-controller:latest                    0.0s
[0m => => unpacking to docker.io/library/kv-controller:latest                 1.2s
[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 4.8s (10/11)                                  docker:desktop-linux
 => exporting to image                                                     3.8s
[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:f0c80a2f3f7ad937c38b1614a07c0b41e2f4af21  0.0s
[0m[36m => => exporting config sha256:5791caba6245f72730d35d5aaaedcb7da7c5495dd1  0.0s
[0m[36m => => exporting attestation manifest sha256:749454c206b30dd4f7b43d9b95bf  0.0s
[0m[36m => => exporting manifest list sha256:1a5a16341f90bcfe73fcb1d969164f03616  0.0s
[0m[36m => => naming to docker.io/library/kv-controller:latest                    0.0s
[0m[36m => => unpacking to docker.io/library/kv-controller:latest                 1.2s
[0m[?25h[1A[1A[1A[1A[1A[1A[1A[1A[1A[0G[?25l[+] Building 5.0s (11/11) FINISHED                         docker:desktop-linux
[36m => [internal] load build definition from Dockerfile.controller            0.0s
[0m[36m => => transferring dockerfile: 418B                                       0.0s
[0m[36m => [internal] load metadata for docker.io/library/python:3.11-slim        0.2s
[0m[36m => [internal] load .dockerignore                                          0.0s
[0m[36m => => transferring context: 2B                                            0.0s
[0m[36m => [1/6] FROM docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => => resolve docker.io/library/python:3.11-slim@sha256:6d85378d88a19cd4  0.0s
[0m[36m => [internal] load build context                                          0.2s
[0m[36m => => transferring context: 651.82kB                                      0.2s
[0m[36m => CACHED [2/6] WORKDIR /app                                              0.0s
[0m[36m => CACHED [3/6] RUN apt-get update && apt-get install -y --no-install-re  0.0s
[0m[36m => CACHED [4/6] COPY requirements.txt .                                   0.0s
[0m[36m => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt        0.0s
[0m[36m => [6/6] COPY . .                                                         0.6s
[0m[36m => exporting to image                                                     3.9s
[0m[36m => => exporting layers                                                    2.6s
[0m[36m => => exporting manifest sha256:f0c80a2f3f7ad937c38b1614a07c0b41e2f4af21  0.0s
[0m[36m => => exporting config sha256:5791caba6245f72730d35d5aaaedcb7da7c5495dd1  0.0s
[0m[36m => => exporting attestation manifest sha256:749454c206b30dd4f7b43d9b95bf  0.0s
[0m[36m => => exporting manifest list sha256:1a5a16341f90bcfe73fcb1d969164f03616  0.0s
[0m[36m => => naming to docker.io/library/kv-controller:latest                    0.0s
[0m[36m => => unpacking to docker.io/library/kv-controller:latest                 1.2s
[0m[36m => => naming to docker.io/library/kv-controller:v1778199518               0.0s
[0m[36m => => unpacking to docker.io/library/kv-controller:v1778199518            0.0s
[0m[?25h## 2. Deploying to Kubernetes
service/controller unchanged
deployment.apps/controller configured
service/frontend unchanged
deployment.apps/frontend configured
horizontalpodautoscaler.autoscaling/frontend-hpa unchanged
serviceaccount/metrics-server unchanged
clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader unchanged
clusterrole.rbac.authorization.k8s.io/system:metrics-server unchanged
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader unchanged
clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator unchanged
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server unchanged
service/metrics-server unchanged
deployment.apps/metrics-server configured
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io unchanged
service/storage-primary unchanged
service/storage-headless unchanged
statefulset.apps/storage unchanged
role.rbac.authorization.k8s.io/pod-watcher-role unchanged
rolebinding.rbac.authorization.k8s.io/watch-pods-binding unchanged
Restarting deployments to pick up new images...
Waiting for pods to be ready (this may take a minute)...
